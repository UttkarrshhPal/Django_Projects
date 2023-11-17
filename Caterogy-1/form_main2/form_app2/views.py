from django.shortcuts import render

#Displaying the form via a view
from .forms import MyForm

def my_view(request):
    if request.method=="POST":
        form = MyForm(request.POST)
        if form.is_valid():
            #Process the form data here
            name=form.cleaned_data ['name']
            age = form.cleaned_data['age']
    else:
        form = MyForm() 
    
    return render(request,'index.html',{'form':form})
    

