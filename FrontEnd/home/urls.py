from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api", views.APIrequest, name="api"),
    path("search", views.search, name="search"),
    path("cart", views.cart, name="cart")
]

