from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple

from shop.models import Category, Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'stock')
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
                   <p><h4>Product Details</h4></p>
               """),
            'name',
            'description',
            'price',
            'category',
            'stock',
            Submit('submit', 'Save')
        )

    def clean(self):
        category = self.cleaned_data.get('category')
        if category and category.count() > 7:
            raise forms.ValidationError("You cannot choose more than 7 categories for your products.")
        return self.cleaned_data
