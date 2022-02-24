from django.shortcuts import render


def location_match(request):
    '''Location Match page view'''
    return render(request, "location_match/location_match.html")
