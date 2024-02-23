from django import forms
from django.forms import ModelForm
from .models import Post

class MyForm(forms.Form):
    your = forms.CharField(label='Your nickname', max_length=20)
    email = forms.EmailField(label='email')
    comment = forms.CharField(label='comment', widget=forms.Textarea)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"