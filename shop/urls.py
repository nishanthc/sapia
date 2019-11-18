from django.urls import path

from shop import views
from shop.views import CategoryDetailView, MerchantDetailView

app = "shop"
urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('merchant/<slug:slug>/', MerchantDetailView.as_view(), name='merchant-detail'),

]
