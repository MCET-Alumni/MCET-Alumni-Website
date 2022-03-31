from django.urls import path 

from . import views

urlpatterns = [
    path('', views.alumni, name='alumni'),
    path('alumni_speaks', views.alumni_speaks, name='alumni_speaks'),
    path('register', views.register, name='register'),
    path('gallery', views.gallery, name='gallery'),
]
