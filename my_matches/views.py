from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from location_match.models import Locations

from profiles.models import UserProfile


def my_matches(request):
    current_user = request.user
    all_locations = Locations.objects.filter(liked_by=current_user)

    context = {
        'current_user': current_user,
        'all_locations': all_locations
    }

    return render(request, "my_matches/my_matches.html", context)


def my_matches_in_location(request, location_id):
    selected_location = get_object_or_404(Locations, id=location_id)

    context = {
        'selected_location': selected_location,
    }

    return render(request, "my_matches/my_matches_in_location.html", context)