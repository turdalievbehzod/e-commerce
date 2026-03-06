from django.urls import path
from . import views

app_name = "shared"

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("checkout/", views.checkout, name="checkout"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
]
