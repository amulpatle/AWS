from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email Address')
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove any fields that are not required manually if they still appear
        self.fields.pop('enabled', None)
        self.fields.pop('disabled', None)