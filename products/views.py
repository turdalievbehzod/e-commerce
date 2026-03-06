from django.shortcuts import render


def product_list(request):
    return render(request, "category.html")


def product_detail(request, id):
    return render(request, "product.html", {"product_id": id})
