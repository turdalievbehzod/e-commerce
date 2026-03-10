from django.urls import path
from .views import dashboard_view, login_view, register_view

app_name = "users"

urlpatterns = [

    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
