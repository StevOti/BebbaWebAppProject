from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact_us.html')
