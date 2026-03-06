from django.shortcuts import render


def product_list(request):
    return render(request, "products/category.html")


def product_detail(request, id):
    return render(request, "products/product.html")
