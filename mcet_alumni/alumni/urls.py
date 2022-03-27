from django.urls import path 

from . import views

urlpatterns = [
    path('', views.alumni, name='alumni'),
    path('notable_alumni', views.notable_alumni),
    path('register', views.register),
]
