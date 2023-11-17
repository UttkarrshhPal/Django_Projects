from django.shortcuts import render
from django.http import HttpResponse
from .forms import classform

def view1(request):
    if request.method == 'POST':
        n = int(request.POST['n_terms'])
        f1 = 0
        f2 = 1
        terms = [f1,f2]
        for i in range (3,n+1):
            f3 = f2+f1
            terms+=[f3]
            f1 = f2
            f2 = f3
        return HttpResponse(str(terms))      
    else:
        forms = classform()
        return render(request,'Templates/index.html',{'form':forms})

