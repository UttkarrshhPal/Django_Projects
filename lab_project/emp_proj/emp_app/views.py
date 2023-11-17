from django.shortcuts import render

def view1(request):
    return render(request,'Templates\index.html')

