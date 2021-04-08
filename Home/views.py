from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) :
    return render(request, 'home.html')

def about_us(request) :
    return render(request, 'about_us.html')

def registration_login(request) :
    return render(request, 'Registration and Login.html')

def contact(request) :
    return render(request, 'contact.html')
    