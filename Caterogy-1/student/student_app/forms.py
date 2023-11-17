from django import forms 

class MyForm(forms.Form):
    regno = forms.CharField(label="Enter Regno:",max_length=10)
    name = forms.CharField(label="Enter Name",max_length=10)
    m1 = forms.CharField(label="Enter Mark1:",max_length=3)
    m2 = forms.CharField(label="Mark2:",max_length=2)
    m3 = forms.CharField(label="Marks3:",max_length=2)
    
