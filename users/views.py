from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import ProfileChangeForm
from users.models import Account


class ProfileView(UpdateView):
    model = Account
    form_class = ProfileChangeForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Profile successfully updated')

        return super(ProfileView, self).form_valid(form)

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass
