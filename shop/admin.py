from django.contrib import admin

# Register your models here.
from shop.models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name']
    exclude = ('slug',)


admin.site.register(Category,CategoryAdmin)