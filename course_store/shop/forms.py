from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-form', 
                                                     'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'input-form',
                                                      'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input-form',
                                                      'placeholder':'Confirm Password'})
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-form', 
                                                     'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class': 'input-form',
                                                      'placeholder':'Password'})