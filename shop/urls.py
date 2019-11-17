from django.urls import path

from shop import views
from shop.views import CategoryDetailView

app = "shop"
urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

]
