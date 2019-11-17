from django.urls import path

from users.views import ProfileView, MerchantCreateView

app = "users"
urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='account_profile'),
    path('accounts/merchant/create/', MerchantCreateView.as_view(), name="account_create_merchant")
]
