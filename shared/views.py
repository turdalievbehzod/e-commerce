from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")


def cart(request):
    return render(request, "shared/cart.html")


def wishlist(request):
    return render(request, "shared/wishlist.html")


def checkout(request):
    return render(request, "shared/checkout.html")


def faq(request):
    return render(request, "pages/faq.html")


def contact(request):
    return render(request, "pages/contact.html")
