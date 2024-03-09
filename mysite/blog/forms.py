from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, CharField, EmailField
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class MyForm(forms.Form):
    your = CharField(label='Your nickname', max_length=20)
    email = EmailField(label='email')
    comment = CharField(label='comment', widget=forms.Textarea)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())
