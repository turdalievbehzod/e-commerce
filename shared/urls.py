from django.urls import path

from . import views

app_name = "shared"

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
]
