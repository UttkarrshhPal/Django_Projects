from django.shortcuts import render
def multiply(request):
    return render(request,'Templates/index.html')
def compute(request):
    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    res = a*b
    return render(request,'Templates/index.html',{'key':res})
