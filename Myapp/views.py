from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def innerpage(request):
    return render(request, 'innerpage.html')

# Create your views here.
