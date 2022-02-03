from django.test import Client, TestCase
from django.urls import resolve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions

from lab_5.forms import TodoForm
from lab_5.models import Todo
from lab_5.views import index


class Lab5UnitTest(TestCase):
    def test_lab_5_url_is_exist(self):
        response = Client().get('/lab-5/')
        self.assertEqual(response.status_code, 200)

    def test_lab5_using_index_func(self):
        found = resolve('/lab-5/')
        self.assertEqual(found.func, index)

    def test_model_can_create_new_todo(self):
        # Creating a new activity
        new_activity = Todo.objects.create(title='mengerjakan lab ppw', description='mengerjakan lab_5 ppw')

        # Retrieving all available activity
        counting_all_available_todo = Todo.objects.all().count()
        self.assertEqual(counting_all_available_todo, 1)

    def test_form_todo_input_has_placeholder_and_css_classes(self):
        form = TodoForm()
        self.assertIn('class="todo-form-input', form.as_p())
        self.assertIn('id="id_title"', form.as_p())
        self.assertIn('class="todo-form-textarea', form.as_p())
        self.assertIn('id="id_description', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = TodoForm(data={'title': '', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['description'],
            ["Please insert a valid input"]
        )

    def test_lab5_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/lab-5/add_todo/', {'title': test, 'description': test})
        self.assertEqual(response_post.status_code, 302)

        response = Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)

    def test_lab5_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/lab-5/add_todo/', {'title': '', 'description': ''})
        self.assertEqual(response_post.status_code, 302)

        response = Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_lab5_delete_todo_and_render_the_result(self):
        Todo.objects.create(title="Sleep", description="Resting your body and refreshing your minds")
        response = Client().get('/lab-5/delete_todo/1/')
        self.assertEqual(response.status_code, 302)

        response = Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertNotIn("Sleep", html_response)

    def test_lab5_fails_delete_todo_and_render_the_result(self):
        Todo.objects.create(title="Sleep", description="Resting your body and refreshing your minds")
        response = Client().get('/lab-5/delete_todo/2/')
        self.assertEqual(response.status_code, 302)

        response = Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertIn("Sleep", html_response)


class Lab5FunctionalTest(TestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(Lab5FunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(Lab5FunctionalTest, self).tearDown()

    def test_input_todo(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/lab-5/')

        # find the form element
        title = selenium.find_element(By.ID, 'id_title')
        description = selenium.find_element(By.ID, 'id_description')
        submit = selenium.find_element(By.ID, 'submit')

        # Fill the form with data
        title.send_keys('Working on PPW-LABS')
        description.send_keys('Today\'s Lab is talking about CSS with functional test using selenium')

        # submitting the form
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Successfully added Todo' in selenium.page_source

        # Hover on description
        todo_desc = WebDriverWait(selenium, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'to-do-list-description')))
        hover = ActionChains(selenium).move_to_element(todo_desc)
        hover.perform()

        # Hover oh the button
        button = WebDriverWait(selenium, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "to-do-list-delete-button")))
        hover = ActionChains(selenium).move_to_element(button)
        hover.perform()

        # Click
        button.click()

        # check the returned result
        assert 'Successfully remove Todo' in selenium.page_source