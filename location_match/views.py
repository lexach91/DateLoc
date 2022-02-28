from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Locations

from profiles.models import UserProfile


def location_match(request):
    '''Location Match page view'''
    all_locations = Locations.objects.all()
    current_user = request.user.id

    context = {
        'all_locations': all_locations,
        'current_user': current_user
    }

    return render(request, "location_match/location_match.html", context)


def liked_location(request, location_id):
    selected_location = get_object_or_404(Locations, id=location_id)
    current_user = request.user

    selected_location.liked_by.add(current_user)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return render(request, "location_match/location_match.html")
