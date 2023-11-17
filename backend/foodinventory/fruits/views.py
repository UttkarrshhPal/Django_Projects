from django.shortcuts import render
from django import forms
# Create your views here.
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields =('title', 'body',)