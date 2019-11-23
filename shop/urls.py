from django.urls import path
from shop.views import CategoryDetailView, MerchantDetailView, ProductCreateView, ProductUpdateView, ProductDetailView

app = "shop"
urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('merchant/<slug:slug>/', MerchantDetailView.as_view(), name='merchant-detail'),
    path('merchant/<slug:slug>/', MerchantDetailView.as_view(), name='merchant-detail'),
    path('/product/<slug:slug>/', ProductDetailView.as_view(), name="product-detail"),


    path('accounts/merchant/product/create/', ProductCreateView.as_view(), name="create-product"),
    path('accounts/merchant/product/update/<slug:slug>/', ProductUpdateView.as_view(), name="update-product")

]
