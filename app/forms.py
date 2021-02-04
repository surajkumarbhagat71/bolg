from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    username = forms.CharField()
    class Meta:
        model  = User
        fields = ['username']


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        exclude = ('user',)