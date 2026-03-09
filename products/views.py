from django.shortcuts import render

from .models import Product, Category

def product_list(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "products/category.html", context)


def product_detail(request, id):
    return render(request, "products/product.html")
