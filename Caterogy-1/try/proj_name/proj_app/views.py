from django.shortcuts import render

def my_view(request):
    return render(request,"Templates/index.html")
# Create your views here.
