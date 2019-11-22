from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

# Register your models here.
from shop.models import Category, Product


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Category
    search_fields = ['name']
    list_display = ['name', 'primary']
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ['name', 'merchant']
    list_display = ['name', 'merchant']


admin.site.register(Product, ProductAdmin)
