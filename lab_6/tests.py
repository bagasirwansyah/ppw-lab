from django.test import Client, TestCase
from django.urls import resolve

from lab_6.views import index


class Lab6UnitTest(TestCase):
    def test_lab_5_url_is_exist(self):
        response = Client().get('/lab-6/')
        self.assertEqual(response.status_code, 200)

    def test_lab5_using_index_func(self):
        found = resolve('/lab-6/')
        self.assertEqual(found.func, index)