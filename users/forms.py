from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Account, Merchant


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
        fields = (
            'first_name', 'last_name', 'company_name', 'website_url', 'tel_number', 'mob_number', "address1",
            'address2',
            'zip_code', 'city',
            'country', 'story', 'referral_source')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                   <hr>
                   <p><h4>Your Personal Details</h4></p>
               """),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ), HTML("""
                   <hr>
                   <p><h4>Your Company</h4></p>
               """),
            'company_name',
            'website_url',
            HTML("""
            <hr>
        """),
            Row(
                Column('tel_number', css_class='form-group col-md-6 mb-0'),
                Column('mob_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML("""
                   <hr>
               """),
            Row(
                Column('address1', css_class='form-group col-md-6 mb-0'),
                Column('address2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML("""
                   <hr>
               """),
            Row(
                Column('zip_code', css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            'country',
            'story',
            'referral_source',
            Submit('submit', 'Save')
        )


class MerchantCreationForm(ModelForm):
    class Meta:
        model = Merchant
        fields = ('stockers_count',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                   <hr>
                   <p><h4>Business Details</h4></p>
               """),
            'stockers_count',
            Submit('submit', 'Save')
        )