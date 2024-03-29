from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CheckboxSelectMultiple

from shop.models import Category
from .models import Account, Merchant, Purchaser


class AccountSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, user):
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

        required = (
            'first_name',
            'last_name',
            'company_name',
            'tel_number',
            'address1',
            'address2',
            'zip_code',
            'city',
            'country',

        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True
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
        fields = ('stockers_count', 'category', 'store_name', 'store_description')
        widgets = {
            'category': CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(primary=True)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                   <hr>
                   <p><h4>Business Details</h4></p>
               """),
            'store_name',
            'store_description',
            'stockers_count',
            HTML("""
                         <hr>
                         <p><h4>Your Products</h4></p>
                     """),
            'category',
            Submit('submit', 'Save')
        )

    def clean(self):
        category = self.cleaned_data.get('category')
        if category and category.count() > 7:
            raise forms.ValidationError("You cannot choose more than 7 categories for your products.")
        return self.cleaned_data


class PurchaserCreationForm(ModelForm):
    class Meta:
        model = Purchaser
        fields = ('store_type', 'category')
        widgets = {
            'category': CheckboxSelectMultiple,
            'store_type': CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label = "Products you'd like to purchase"
        self.fields['category'].queryset = Category.objects.filter(primary=True)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                   <hr>
                   <p><h4>Business Details</h4></p>
               """),
            'store_type',
            HTML("""
                         <hr>
                         <p><h4>Sourcing</h4></p>
                     """),

            'category',
            Submit('submit', 'Save')
        )
