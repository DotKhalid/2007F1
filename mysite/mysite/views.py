from django.http import HttpResponse

from django.shortcuts import render



def Home(request):
    data = {
    "title":"Home"
            }
    return render(request, "index.html",data)


def aboutus(request):
    return HttpResponse("<b>Hello World!</b>")

def contact(request):
    return HttpResponse("<b>Contact Page!</b>")

def product(request):
    return HttpResponse("<b>Product Page!</b>")


def productdetail(request,p_name):
    return HttpResponse(p_name)



