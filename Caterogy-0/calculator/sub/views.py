from django.shortcuts import render

# Create your views here.
def sub(request):
    return render(request, "index.html")

def subtract(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 - val2
    return render(request, "index.html", {"result": res})