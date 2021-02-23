from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('',views.index,name = 'home'),
    path('about',views.about,name = 'home'),
    path('contact',views.contact,name = 'home'),
    path('service',views.service,name = 'home')
]