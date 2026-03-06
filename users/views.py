from django.shortcuts import render


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "coming-soon.html")


def dashboard(request):
    return render(request, "dashboard.html")
