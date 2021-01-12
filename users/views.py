from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import LoginForm, UpdateProfileForm, SignUpForm
from users.models import User
from dates.models import DatesNightModel


def index(request):
    return render(request, "index.html", {})


def sign_up(request):
    html = "sign_up_form.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data["username"],
                full_name=data["display_name"],
                email=data["email"],
                password=data["password"],
                location=data["location"],
            )
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, html, {"form": form})


@login_required(login_url="login")
def profile_view(request, profile_id):
    dates_night = len(DatesNightModel.objects.filter(users_one=profile_id))
    user_profile = User.objects.filter(id=profile_id).first()
    return render(
        request,
        "profile.html",
        {"datesnight": dates_night, "userprofile": user_profile},
    )


def delete_profile_view(request, profile_id):

    delete_profile = User.objects.get(id=profile_id)
    delete_profile.delete()

    return render(request, "index.html", {"delete_profile": delete_profile})


def update_profile_view(request, profile_id):
    html = "generic_form.html"
    update_profile = User.objects.get(id=profile_id)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            update_profile.full_name = (data["full_name"],)
            update_profile.email = (data["email"],)
            update_profile.location = (data["location"],)
            update_profile.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = UpdateProfileForm()
    return render(request, html, {"form": form})


@login_required(login_url="login")
def preferences_view(request):
    return render(request, "preferences.html", {})


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