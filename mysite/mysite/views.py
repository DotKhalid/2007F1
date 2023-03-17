from django.http import HttpResponse

from django.shortcuts import render



def Home(request):
    return render(request, "index.html")

def Special_Offer(request):
    return render(request, "special_offer.html")

def Delivery(request):
    return render(request, "normal.html")

def Contact(request):
    return render(request, "contact.html")


def Message(request):
    return render(request, "message.html",{})


def aboutus(request):
    return HttpResponse("<b>Hello World!</b>")

def contact(request):
    return HttpResponse("<b>Contact Page!</b>")

def product(request):
    return HttpResponse("<b>Product Page!</b>")


def productdetail(request,p_name):
    return HttpResponse(p_name)



