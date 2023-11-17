from django.shortcuts import render
from .forms import MyForm
def my_view1(request):
    form = MyForm()
    return render(request,'index.html',{'form':form})