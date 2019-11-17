from django.urls import path

from users.views import ProfileView, MerchantCreateView, MerchantUpdateView, PurchaserCreateView, PurchaserUpdateView

app = "users"
urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='account_profile'),
    path('accounts/merchant/create/', MerchantCreateView.as_view(), name="account_create_merchant"),
    path('accounts/merchant/update/', MerchantUpdateView.as_view(), name="account_update_merchant"),
    path('accounts/purchaser/create/', PurchaserCreateView.as_view(), name="account_create_purchaser"),
    path('accounts/purchaser/update/', PurchaserUpdateView.as_view(), name="account_update_purchaser")

]
