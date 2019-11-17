from django.urls import path

from users.views import ProfileView, MerchantCreateView, MerchantUpdateView

app = "users"
urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='account_profile'),
    path('accounts/merchant/create/', MerchantCreateView.as_view(), name="account_create_merchant"),
    path('accounts/merchant/update/', MerchantUpdateView.as_view(), name="account_update_merchant")

]
