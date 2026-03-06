from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("category/", views.product_list, name="product_list"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
]
