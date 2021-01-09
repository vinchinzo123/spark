from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import LoginForm, SignUpForm
from users.models import User


def index(request):
    return render(request, "index.html", {})


def sign_up(request):
    html = "sign_up_form.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data["username"],
                full_name=data["display_name"],
                email=data["email"],
                password=data["password"],
                location=data["location"],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, html, {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "form.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "successfully logged out")
    return redirect("/")