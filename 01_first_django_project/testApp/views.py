from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"testApp/home.html")

def about(request):
    return render(request, 'testApp/about.html')

def contact(request):
    return render(request, 'testApp/contact.html')