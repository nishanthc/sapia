from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import ProfileChangeForm, MerchantCreationForm
from users.models import Account, Merchant


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


class MerchantCreateView(CreateView):
    model = Merchant
    form_class = MerchantCreationForm
    template_name = 'account/merchant_create.html'
    success_url = reverse_lazy('account_create_merchant')

    def form_valid(self, form):
        if Merchant.objects.filter(account_id=self.request.user.id).exists():
            messages.add_message(self.request, messages.ERROR, 'You already have a merchant account!')
            return super(MerchantCreateView, self).form_invalid(form)
        form.instance.account = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Merchant successfully created')
        return super(MerchantCreateView, self).form_valid(form)


class MerchantUpdateView(UpdateView):
    model = Merchant
    form_class = MerchantCreationForm
    template_name = 'account/merchant_update.html'
    success_url = reverse_lazy('account_update_merchant')

    def get_object(self, queryset=None):
        return self.request.user.merchant

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Merchant account successfully updated')
        return super(MerchantUpdateView, self).form_valid(form)
