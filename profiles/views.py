from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse
from .models import UserProfile


def profile(request):
    '''Home page view'''
    return render(request, "profiles/profile.html")


class ProfileCreateView(CreateView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/create_profiles.html'
    fields = ['display_name', 'email', 'bio', 'image', 'job_title', 'phone_number',
              'town_or_city', 'county']
    success_message = "Profile created"
    success_url = reverse_lazy('profile')


# class ProfileDetailView(DetailView):
#     '''Profile Detail view'''
#     model = UserProfile
#     template_name = 'profiles/profile.html'
#     fields = '__all__'
