import numpy as np
from django.urls import path
from . import views

urlpatterns = [
    path('index',views.run, name='index'),
    path('',views.Home, name='Home'),
    path('Matrice/', views.Matrice, name='Matrice'),
    path('Contact/', views.Contact, name='Contact'),
    path('Services/', views.Services, name='Services'),
    path('Statistique/', views.Statistique, name='Statistique'),
    path('Fraction/', views.Fraction, name='Fraction'),
    path('NombreAmi/', views.NombreAmi, name='NombreAmi'),
    path('NombreParfait/', views.NombreParfait, name='NombreParfait'),
    path('NombrePremier/', views.NombrePremier, name='NombrePremier'),
    path('Probabilite/', views.Probabilite, name='Probabilite'),
    path('Syntax/', views.Syntax, name='Syntax'),


    #path('About/', views.Services, name='About'),

]
