from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse

from .models import UserProfile
from .forms import UserProfileForm


class ProfileListView(ListView):
    '''Home page view'''
    model = UserProfile
    template_name = 'profiles/profile.html'

    def get_user(self, user):
        queryset = self.filter(user=user)


class ProfileCreateView(CreateView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/create_profile.html'
    form_class = UserProfileForm
    success_message = "Profile created"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/profile-detail.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')


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
    template_name = 'profiles/profile-delete.html'
    success_message = "Profile will be deleted"
    success_url = reverse_lazy('profile')
