from django.urls import path
from . import views
from django.http import HttpResponse




urlpatterns = [

    path('', views.home),
    path('api/', views.getEndpoints),
    path('result/', views.getResult),
    
]