from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html')

def donation(request):
    return render(request, 'home/donation.html') 

def gallery(request):
    return render(request, 'home/gallery.html') 
    