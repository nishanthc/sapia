from django.urls import path

from users.views import ProfileView

app = "users"
urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='account_profile'),
]