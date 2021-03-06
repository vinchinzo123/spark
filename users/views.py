from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from users.forms import (
    LoginForm,
    UpdateProfileForm,
    ImageForm,
    SignUpForm,
    PreferencesUpdateForm,
)
from users.models import User
from dates.models import DatesNightModel
from dates.forms import ChooseDateCategory
from notifications.models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View


def index(request):
    confirmed_dates = Notification.objects.filter(
        status="Confirmed",
        sent_user=request.user.id,
        archived=False,
        notified_sent_user=False,
    ).union(
        Notification.objects.filter(
            status="Confirmed",
            received_user=request.user.id,
            archived=False,
            notified_received_user=False,
        )
    )

    active_notifications = Notification.objects.filter(
        sent_user=request.user.id
    ).filter(status="Sent", notified_sent_user=False)

    received_notifications = Notification.objects.filter(
        received_user=request.user.id, status="Sent", notified_received_user=False
    )

    declined_notifications = Notification.objects.filter(
        sent_user=request.user.id,
        status="Declined",
        archived=False,
        notified_sent_user=False,
    ) | (
        Notification.objects.filter(
            received_user=request.user.id,
            status="Declined",
            notified_received_user=False,
            archived=False,
        )
    )

    no_match_notifications = (
        Notification.objects.filter(
            sent_user=request.user.id,
            status="No Match",
            archived=False,
            notified_sent_user=False,
        )
    ).union(
        Notification.objects.filter(
            received_user=request.user.id,
            status="No Match",
            archived=False,
            notified_received_user=False,
        )
    )

    cancelled_notifications = Notification.objects.filter(
        sent_user=request.user.id,
        status="Cancelled",
        archived=False,
        notified_sent_user=False,
    ) | (
        Notification.objects.filter(
            received_user=request.user.id,
            status="Cancelled",
            archived=False,
            notified_received_user=False,
        )
    )
    # breakpoint()
    expired_notifications = []

    for note in received_notifications:
        if note.date_night.when_date_time < timezone.now():
            note.notified_received_user = True
            expired_notifications.append(note)
        if note.notified_sent_user and note.notified_received_user:
            expired_notifications.append(note)
            note.archived = True
            note.status = "Cancelled"
        note.save()

    for note in active_notifications:
        if note.date_night.when_date_time < timezone.now():
            note.notified_sent_user = True
            expired_notifications.append(note)
        if note.notified_sent_user and note.notified_received_user:
            note.archived = True
            note.status = "Cancelled"
            expired_notifications.append(note)
        note.save()

    for note in confirmed_dates:
        if note.date_night.when_date_time < timezone.now():
            if note.received_user == request.user:
                note.notified_received_user = True
            else:
                note.notified_sent_user = True
            if note.notified_sent_user and note.notified_received_user:
                note.archived = True
            expired_notifications.append(note)
            note.save()

    for note in cancelled_notifications:
        if note.received_user == request.user:
            note.notified_received_user = True
        else:
            note.notified_sent_user = True
        if note.notified_sent_user and note.notified_received_user:
            note.archived = True
        note.save()

    for note in declined_notifications:
        if note.received_user == request.user:
            note.notified_received_user = True
        else:
            note.notified_sent_user = True
        if note.notified_sent_user and note.notified_received_user:
            note.archived = True
        note.save()

    for note in no_match_notifications:
        if note.received_user == request.user:
            note.notified_received_user = True
        else:
            note.notified_sent_user = True
        if note.notified_sent_user and note.notified_received_user:
            note.archived = True
        note.save()

    # the following is to allow users to login from the landing page
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
    date_type_form = ChooseDateCategory()
    date_night_choices = [
        {"instance": x[0], "value": x[1]}
        for x in date_type_form.fields["choice"].choices
    ][1:]
    return render(
        request,
        "index.html",
        {
            "expired_notifications": expired_notifications,
            "confirmed_dates": confirmed_dates,
            "cancelled_notifications": cancelled_notifications,
            "no_match_notifications": no_match_notifications,
            "received_notifications": received_notifications,
            "active_notifications": active_notifications,
            "declined_notifications": declined_notifications,
            "form": form,
            "date_type_form": date_type_form,
            "date_night_choices": date_night_choices,
        },
    )


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
    template = "index.html"

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
    dates_sender = len(DatesNightModel.objects.filter(users_one=profile_id))
    dates_reciever = len(DatesNightModel.objects.filter(users_two=profile_id))
    dates_night = dates_reciever + dates_sender
    user_profile = User.objects.filter(id=profile_id).first()
    update_profile_form = UpdateProfileForm(instance=request.user)
    update_preferences_form = PreferencesUpdateForm(instance=request.user)
    update_pic_form = ImageForm()
    return render(
        request,
        "profile.html",
        {
            "datesnight": dates_night,
            "userprofile": user_profile,
            "update_pic_form": update_pic_form,
            "update_profile_form": update_profile_form,
            "update_preferences_form": update_preferences_form,
        },
    )


def delete_profile_view(request, profile_id):
    # go to a pre-delete page/modal
    delete_profile = User.objects.get(id=profile_id)
    delete_profile.delete()

    return HttpResponseRedirect(reverse("homepage"))


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


def user_photo_view(request):

    if request.method == "GET":
        user_image = User.objects.all()

    return render(request, "profile.html", {"user_image": user_image})


def profile_image_view(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            current_user = User.objects.get(id=request.user.id)
            current_user.picture = data["picture"]
            current_user.save()
            # breakpoint()
            messages.info(request, "successfully upload!")
            return HttpResponseRedirect(f"/profile/{current_user.id}/")
    else:
        form = ImageForm()
    return render(request, "generic_form.html", {"form": form})


def success(request):
    return HttpResponse("successfully uploaded")


class PreferencesUpdateView(LoginRequiredMixin, View):
    form_class = PreferencesUpdateForm
    template = "form.html"

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            current_user = User.objects.get(id=request.user.id)
            current_user.dining_preference.set(data["dining_preference"])
            current_user.entertainment_preference.set(data["entertainment_preference"])
            current_user.out_doors_preference.set(data["out_doors_preference"])
            current_user.stay_home_preference.set(data["stay_home_preference"])
            return redirect(f"/profile/{request.user.id}/")


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
    template = "index.html"

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


def about_us_view(request):
    return render(request, 'about_us.html', {})