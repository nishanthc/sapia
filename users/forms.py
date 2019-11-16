from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Account


class AccountSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username', 'email')


class ProfileChangeForm(ModelForm):
    class Meta:
        model = Account
        fields = ('company_name', 'website_url', 'tel_number', 'mob_number', "address1", 'address2', 'zip_code', 'city',
                  'country', 'story', 'referral_source')
