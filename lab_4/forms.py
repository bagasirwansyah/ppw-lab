from django import forms


class MessageForm(forms.Form):
    error_messages = {
        'required': 'Please fill out this form',
        'invalid': 'Invalid input',
    }
    attrs = {
        'class': 'form-control'
    }

    name = forms.CharField(label='Nama', required=False, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs), error_messages=error_messages)
    message = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True, error_messages=error_messages)
