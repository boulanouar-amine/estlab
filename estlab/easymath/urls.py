from django.urls import path

from . import views

urlpatterns = [
    path('',views.run, name='index'),
    path('documentation',views.doc, name='documentation'),

]
