from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = blog
        fields = ('title', 'desc',)

class NewUserForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model= User
        fields = ("username","password1", "password2")



