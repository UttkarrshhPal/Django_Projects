#Creating a django form

from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Your Name')
    age = forms.IntegerField(label='Your Age')
        