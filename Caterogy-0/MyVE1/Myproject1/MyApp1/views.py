from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    msg1 = '<h1>Hello Sastra</h1>'
    return HttpResponse(msg1)
def view2(request):
    return render(request,'Template/index.html')    
 
 
 