from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from shop.models import Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
