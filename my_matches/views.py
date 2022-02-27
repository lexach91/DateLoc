from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# from .models import Locations

from profiles.models import UserProfile


def my_matches(request):
    # current_user = request.user.id
    # # current_user2 = get_object_or_404(UserProfile, id=current_user)

    # context = {
    #     'current_user': current_user,
    #     # 'current_user2': current_user2
    # }

    return render(request, "my_matches/my_matches.html", context)