from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormForRegister (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'kemail', 'password1', 'password2')