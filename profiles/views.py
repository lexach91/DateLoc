from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse


from .models import UserProfile
from .forms import UserProfileForm


class ProfileListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    '''Home page view'''
    model = UserProfile
    template_name = 'profiles/profile.html'

    def get_user(self, request, pk):
        current_user = get_object_or_404(UserProfile, id=request.user.id)
        current_user = request.user.id

        context = {'current_user': current_user}
        return render(request, "profiles/profile.html", context)


class ProfileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/create_profile.html'
    form_class = UserProfileForm
    success_message = "Profile created"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    '''Profile Detail view'''
    model = UserProfile
    template_name = 'profiles/profile-detail.html'
    success_url = reverse_lazy('profile')


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''Profile Update view'''
    model = UserProfile
    template_name = 'profiles/profile-update.html'
    form_class = UserProfileForm
    success_message = "Profile Updated"
    success_url = reverse_lazy('profile')


class ProfileDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    View displays the option to delete the Profile to the user.
    '''
    model = UserProfile
    template_name = 'profiles/profile-delete.html'
    success_message = "Profile will be deleted"
    success_url = reverse_lazy('profile')
