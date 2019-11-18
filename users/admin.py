from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm
from .models import Account, Merchant, ReferralSource, StoreType, Purchaser


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
    list_display = ['account', 'store_name', 'stockers_count', 'get_categories']
    exclude = ('slug',)


    def get_categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])

    get_categories.short_description = 'Categories'


admin.site.register(Merchant, MerchantAdmin)


class PurchaserAdmin(admin.ModelAdmin):
    model = Purchaser
    list_display = ['account', 'get_store_types', 'get_categories']

    def get_store_types(self, obj):
        return ", ".join([p.name for p in obj.store_type.all()])

    def get_categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])

    get_store_types.short_description = 'Store Types'
    get_categories.short_description = 'Categories'


admin.site.register(Purchaser, PurchaserAdmin)


class ReferralSourceAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = ReferralSource
    list_display = ['name']


admin.site.register(ReferralSource, ReferralSourceAdmin)


class StoreTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = StoreType
    list_display = ['name']


admin.site.register(StoreType, StoreTypeAdmin)
