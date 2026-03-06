from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def cart_view(request):
    return render(request, "cart.html")


def checkout_view(request):
    return render(request, "checkout.html")


def wishlist(request):
    return render(request, "wishlist.html")


def faq(request):
    return render(request, "faq.html")


def contact(request):
    return render(request, "contact.html")
