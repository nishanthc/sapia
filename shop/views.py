# Create your views here.
from django.views.generic import DetailView

from shop.models import Category
from users.models import Merchant


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MerchantDetailView(DetailView):
    model = Merchant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
