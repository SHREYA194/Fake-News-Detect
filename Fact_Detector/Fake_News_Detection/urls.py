from django.conf.urls import url
from django.urls import path
from .import views

'''
urlpatterns =[
    path('',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('Registration.html',views.register,name='Registration'),
    path('Registration.html',views.login,name='Registration'),
    path('contact.html',views.contact,name='contact'),
]
'''

urlpatterns =[
    url(r'^$',views.home,name='home'),
    url(r'^about$',views.about,name='about'),
    url(r'^register$',views.register,name='Registration'),
    url(r'^login$',views.login,name='Registration'),
    url(r'^contact$',views.contact,name='contact'),
    path('search.html',views.search,name='search'),
    path('result.html',views.result,name='result'), 
    path("logout",views.logout,name="logout"),
]

'''
url(r'^search$',views.search,name='search'),
    url(r'^result$',views.result,name='result'),
'''