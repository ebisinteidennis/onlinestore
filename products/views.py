from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products" : products})

def Offer(request):
    return HttpResponse("index.html")