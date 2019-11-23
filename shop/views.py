# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import DetailView, CreateView, UpdateView

from shop.forms import ProductCreationForm
from shop.models import Category, Product
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


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'account/product_create.html'

    def form_valid(self, form):
        form.instance.merchant = self.request.user.merchant
        messages.add_message(self.request, messages.SUCCESS, 'Product successfully added')

        return super(ProductCreateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return super(ProductCreateView, self).get(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'account/product_update.html'

    def form_valid(self, form):
        form.instance.merchant = self.request.user.merchant
        print(form.instance.slug)
        messages.add_message(self.request, messages.SUCCESS, 'Product successfully created')
        print("didnt redirect")
        return super(ProductUpdateView, self).form_valid(form)
