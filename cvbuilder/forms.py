from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#built-in login k liy
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
#built-in login import         
class LoginForm(AuthenticationForm):
    pass