from django.shortcuts import render


def profile(request):
    '''Profile page view'''
    return render(request, "profiles/profiles.html")
