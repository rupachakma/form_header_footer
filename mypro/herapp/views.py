from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import people

def r(request):
    return HttpResponse("Hello Rupa from herapp")
def dex(request):
    return render(request,"index.html")
def port(request):
    return render(request,"portfolio-details.html")
def form(request):
    if request.method == "GET":
        a = request.GET.get("n1")
        b = request.GET.get("a1")
        c = request.GET.get("n2")

        info= people()
        info.name= a
        info.adress= b
        info.number= c
        info.save()
     


    return render(request,"form.html",{'x':a,'y':b,'z':c})