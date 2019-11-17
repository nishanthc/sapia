from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm
from .models import Account, Merchant


class UserAdmin(UserAdmin):
    form = AccountChangeForm
    model = Account
    list_display = ['email', 'company_name', 'first_name', 'last_name']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'company_name',
                'website_url',
                'tel_number',
                'mob_number',
            )}),
        (('Address'), {
            'fields': (
                'address1',
                'address2',
                'zip_code',
                'city',
                'country'
            )}),
        (('Bio'), {
            'fields': (
                'story',
                'referral_source',
            )}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Account, UserAdmin)


class MerchantAdmin(admin.ModelAdmin):
    model = Merchant
    list_display = ['account', 'stockers_count']


admin.site.register(Merchant, MerchantAdmin)
