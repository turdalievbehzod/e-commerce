from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("shared:home")

    return render(request, "users/login.html")



def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("users:login")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("users:login")

        user = User.objects.create_user(
            username=username,
            password=password1
        )

        login(request, user)

        return redirect("shared:home")

    return redirect("users:login")

def dashboard_view(request):
    return render(request, "users/dashboard.html")
