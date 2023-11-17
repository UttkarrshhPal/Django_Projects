from django import forms  
class MyForm(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label = 'Your Email')