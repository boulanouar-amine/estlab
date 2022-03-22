import numpy as np
from django.urls import path
from . import views

urlpatterns = [
    path('index',views.run, name='index'),
    path('documentation',views.doc, name='documentation'),
    path('', views.Home, name='Home'),
    path('Matrice/', views.Matrice, name='Matrice'),
    path('Contact/', views.Contact, name='Contact'),
    path('Services/', views.Services, name='Services'),


]
