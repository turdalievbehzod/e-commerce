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

    product = Product.objects.get(id=id)

    related_products = Product.objects.exclude(id=id)[:4]

    return render(
        request,
        "products/product.html",
        {
            "product": product,
            "related_products": related_products
        }
    )
