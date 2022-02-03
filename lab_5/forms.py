from django import forms


class TodoForm(forms.Form):
    error_messages = {
        'required': 'Please insert a valid input',
    }
    title_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder': 'Insert title...'
    }
    description_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'todo-form-textarea',
        'placeholder': 'Insert description...'
    }

    title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs), error_messages=error_messages)
    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs), error_messages=error_messages)
