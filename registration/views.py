from django.shortcuts import render
from .forms import UserRegistrationForm

def registration(request):

    form = UserRegistrationForm()

    context = {
        'test_message': 'Hello from registration app',
        'form': form,
    }

    return render(request, "registration/registration.html", context)
