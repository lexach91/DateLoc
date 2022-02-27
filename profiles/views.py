from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse

from .models import UserProfile
from .forms import UserProfileForm


class ProfileListView(ListView):
    '''Home page view'''
    model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = 'profiles/profiles_list.html'


def profile(request):
    '''Home page view'''
    return render(request, "profiles/profile-detail.html")


class ProfileCreateView(CreateView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/create_profiles.html'
    fields = "__all__"
    success_message = "Profile created"
    success_url = reverse_lazy('profile')


class ProfileDetailView(DetailView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/profile-detail.html'
    fields = '__all__'


class ProfileUpdateView(UpdateView):
    '''Profile Update view'''
    model = UserProfile
    template_name = 'profiles/profile-update.html'
    form_class = UserProfileForm
    success_message = "Profile Updated"
    success_url = reverse_lazy('profile')


class ProfileDeleteView(DeleteView):
    '''
    View displays the option to delete the Profile to the user.
    '''
    model = UserProfile
    template_name = 'rprofiles/profile-delete.html'
    success_message = "Profile will be deleted"
    success_url = reverse_lazy('profile')
