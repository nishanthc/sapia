from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from users.forms import ProfileChangeForm, MerchantCreationForm, PurchaserCreationForm
from users.models import Account, Merchant, Purchaser


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

    def get(self, request, *args, **kwargs):
        if not request.user.company_name:
            messages.add_message(self.request, messages.ERROR,
                                 'You must complete your profile before you can use become a merchant.')
            return HttpResponseRedirect(reverse('account_profile'))
        return super(MerchantCreateView, self).get(request, *args, **kwargs)


class MerchantUpdateView(UpdateView):
    model = Merchant
    form_class = MerchantCreationForm
    template_name = 'account/merchant_update.html'
    success_url = reverse_lazy('account_update_merchant')

    def get_object(self, queryset=None):
        if not hasattr(self.request.user, 'merchant'):
            messages.add_message(self.request, messages.ERROR,
                                 'You must first create a merchant account')
            HttpResponseRedirect(reverse('account_create_merchant'))
        else:
            return self.request.user.merchant

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Merchant account successfully updated')
        return super(MerchantUpdateView, self).form_valid(form)


class PurchaserCreateView(CreateView):
    model = Purchaser
    form_class = PurchaserCreationForm
    template_name = 'account/purchaser_create.html'
    success_url = reverse_lazy('account_create_purchaser')

    def form_valid(self, form):
        if Purchaser.objects.filter(account_id=self.request.user.id).exists():
            messages.add_message(self.request, messages.ERROR, 'You already have a purchaser account!')
            return super(PurchaserCreateView, self).form_invalid(form)
        form.instance.account = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Purchaser successfully created')
        return super(PurchaserCreateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if not request.user.company_name:
            messages.add_message(self.request, messages.ERROR,
                                 'You must complete your profile before you can use become a purchaser.')
            return HttpResponseRedirect(reverse('account_profile'))
        if hasattr(self.request.user, 'purchaser'):

            print("test")
            messages.add_message(self.request, messages.ERROR,
                                 'You already have a purchaser account!')
            return HttpResponseRedirect(reverse('account_update_purchaser'))
        return super(PurchaserCreateView, self).get(request, *args, **kwargs)


class PurchaserUpdateView(UpdateView):
    model = Purchaser
    form_class = PurchaserCreationForm
    template_name = 'account/purchaser_update.html'
    success_url = reverse_lazy('account_update_purchaser')

    def get_object(self, queryset=None):
        if not hasattr(self.request.user, 'purchaser'):
            messages.add_message(self.request, messages.ERROR,
                                 'You must first create a purchaser account')
            HttpResponseRedirect(reverse('account_create_purchaser'))
        else:
            return self.request.user.purchaser

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Purchaser account successfully updated')
        return super(PurchaserUpdateView, self).form_valid(form)

