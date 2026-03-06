from django.shortcuts import render


def home(request):
    return render(request, "shared/index.html")


def cart_view(request):
    return render(request, "shared/cart.html")


def checkout_view(request):
    return render(request, "shared/checkout.html")


def wishlist(request):
    return render(request, "shared/wishlist.html")


def faq(request):
    return render(request, "shared/faq.html")


def contact(request):
    return render(request, "shared/contact.html")
