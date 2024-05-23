from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request,'productApp/home.html',{"products":products})

def detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request,'productApp/detail.html',{"product":product})