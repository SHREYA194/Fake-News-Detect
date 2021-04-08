from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='Home'),
    path('about_us', views.about_us, name='AboutUs'),
    path('RegistrationandLogin', views.registration_login, name='LogIn/SignUp'),
    path('contact', views.contact, name='ContactUs')
]
