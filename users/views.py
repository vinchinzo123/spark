from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            authenticated_user = authenticate(data["username"], data["password"])
            if authenticated_user is not None:
                authenticated_user
            breakpoint()
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, html, {"form": form})


@login_required(login_url="login")
def profile_view(request):
    return render(request, "profile.html", {})


@login_required(login_url="login")
def create_a_date_view(request):
    return render(request, "create_A_date.html", {})


@login_required(login_url="login")
def preferences_view(request):
    return render(request, "preferences.html", {})


@login_required(login_url="login")
def pending_dates_view(request):
    return render(request, "pending_dates.html", {})


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


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "successfully logged out")
    return redirect("/")