from django.shortcuts import render


def home(request):
    '''Home page view'''
    return render(request, "home/home.html")
