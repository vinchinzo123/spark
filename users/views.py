from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import LoginForm
from users.models import User
from dates.models import DatesNightModel


def index(request):
    return render (request, "index.html", {})

def profile_view(request, profile_id):
    dates_night = DatesNightModel.objects.filter(id=profile_id).first()
    user_profile = User.objects.filter(id=profile_id).first()
    return render(request, "profile.html",{"datesnight":dates_night, "userprofile":user_profile})

def create_a_date_view(request):
    return render (request, "create_A_date.html", {})



def preferences_view(request):
    return render (request, "preferences.html", {})


def pending_dates_view(request):
    return render (request, "pending_dates.html", {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            form = LoginForm()
            return render(request, "form.html", {"form": form})
    form = LoginForm()
    return render(request, "form.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "successfully logged out")
    return redirect("/")