from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import LoginForm, UpdateProfileForm, ImageForm, SignUpForm
from users.models import User, ImageModel
from dates.models import DatesNightModel
from notifications.models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View


def index(request):
    confirmed_dates = (
        Notification.objects.filter(status="Confirmed")
        .filter(sent_user=request.user.id)
        .union(
            Notification.objects.filter(status="Confirmed").filter(
                received_user=request.user.id
            )
        )
    )
    return render(request, "index.html", {"confirmed_dates": confirmed_dates})


# def sign_up(request):
#     html = "sign_up_form.html"
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = User.objects.create_user(
#                 username=data["username"],
#                 full_name=data["display_name"],
#                 email=data["email"],
#                 password=data["password"],
#                 location=data["location"],
#             )
#             user = authenticate(
#                 request, username=data["username"], password=data["password"]
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("homepage"))
#     form = SignUpForm()
#     return render(request, html, {"form": form})


class SignupView(View):
    form_class = SignUpForm
    template = "sign_up_form.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
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


@login_required(login_url="login")
def profile_view(request, profile_id):
    """
     look at the profile.html ensure we are NOT using 'request.user'
    but the variable 'userprofile' defined on line 54.

    for the number of dates night we will not just want to filter on user_one,
    but also on (users_two=profile_id),
    perhapes we can use .intersetcion( ) to get a query sets with unique values

    additionally consider calling User.objects.get(id=profile_id)
     as this will return the specific object we want instead of queryset

     if user_profile is None then we can throw a 404 or user not found
    """
    dates_night = len(DatesNightModel.objects.filter(users_one=profile_id))
    user_profile = User.objects.filter(id=profile_id).first()
    return render(
        request,
        "profile.html",
        {"datesnight": dates_night, "userprofile": user_profile},
    )


def delete_profile_view(request, profile_id):
    # go to a pre-delete page/modal
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
            update_profile.full_name = data["full_name"]
            update_profile.email = data["email"]
            update_profile.location = data["location"]
            update_profile.save()
        return HttpResponseRedirect(f"/profile/{profile_id}/")
    form = UpdateProfileForm()
    return render(request, html, {"form": form})


def add_photo_view(request):
    # needs to be complete
    if request.method == "POST":
        userImageForm = ImageForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True


def create_a_date_view(request):
    return render(request, "create_A_date.html", {})


@login_required(login_url="login")
def preferences_view(request):
    return render(request, "preferences.html", {})


# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request, username=data["username"], password=data["password"]
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("homepage"))
#     form = LoginForm()
#     return render(request, "form.html", {"form": form})


class LoginView(View):
    form_class = LoginForm
    template = "form.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))


# @login_required(login_url="login")
# def logout_view(request):
#     logout(request)
#     messages.info(request, "successfully logged out")
#     return redirect("/")


class LogoutView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get(self, request):
        logout(request)
        return redirect("/")


def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response


def error500_view(request):
    raise Exception("Make response code 500!")
