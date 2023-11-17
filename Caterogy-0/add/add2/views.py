from django.shortcuts import render

def Addition(request):
    return render(request,'Template\index.html')

def add_logic(request):
    no1 = int(request.GET["num1"])
    no2 = int(request.GET["num2"])
    res = no1+no2
    return render(request,'Template\index.html',{'key':res}) 
