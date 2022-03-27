from django.shortcuts import render

# Create your views here.
def alumni(request):
    return render(request, 'alumni/alumni.html')

def notable_alumni(request):
    return render(request, 'alumni/notable_alumni.html')

def register(request):
    return render(request, 'alumni/register.html')
