from django.shortcuts import render

# Create your views here.
def mul(request):
    return render(request, "index.html")

def multiplication(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 * val2
    return render(request, "index.html", {"result": res})