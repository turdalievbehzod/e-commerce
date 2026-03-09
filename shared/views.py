from django.shortcuts import render

from products.models import Product
from blogs.models import BlogPost

def home(request):
    products = Product.objects.filter(is_active=True)[:8]
    blogs = BlogPost.objects.filter(is_published=True)[:3]

    context = {
        "products": products,
        "blogs": blogs,
    }

    return render(request, "shared/index.html", context)


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
