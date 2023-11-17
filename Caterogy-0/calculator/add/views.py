from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, "index.html")

def addition(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 + val2
    return render(request, "index.html", {"result": res})