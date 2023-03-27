from django.shortcuts import render

# Create your views here.


def home__page(request):
    return render(request, 'index.html')


def about__page(request):
    return render(request, 'about.html')


def contact__page(request):
    return render(request, 'contact.html')
