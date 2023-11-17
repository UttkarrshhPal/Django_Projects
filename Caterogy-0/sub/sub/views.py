from django.shortcuts import render
def sub3(request):
    return render(request,'index.html')

def sub1(request):
    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    res = a-b
    return render(request,'index.html',{'r':res})
