from django.shortcuts import render, reverse, HttpResponseRedirect
from dates.models import DatesNightModel
from dates.forms import (
    ChooseDateCategory,
    CreateADiningDate,
    CreateAnEntertainmentDate,
    CreateAnOutdoorsDate,
    CreateAStayHomeDate,
    Preferences,
)
from datetime import datetime
from notifications.models import Notification
from preferences.models import Preferences, Dining, OutDoors, StayHome, Entertainment
from users.models import User


def create_a_date_view(request):
    if request.method == "POST":
        form = ChooseDateCategory(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_category = data["choice"]
            if date_category == "Dining":
                return HttpResponseRedirect(reverse("dining"))
            elif date_category == "Entertainment":
                return HttpResponseRedirect(reverse("entertainment"))
            elif date_category == "Outdoors":
                return HttpResponseRedirect(reverse("outdoors"))
            elif date_category == "Stay_At_Home":
                return HttpResponseRedirect(reverse("stayhome"))
    # prefered = Preferences.objects.all()
    # choice = prefered.get_choice_display()
    form = ChooseDateCategory()
    date_night_choices = ["Dining", "Outdoors", "Stay_At_Home", "Entertainment"]
    return render(
        request,
        "date_night_type_form.html",
        {"form": form, "date_night_choices": date_night_choices},
    )


def dining_date(request):
    form = CreateADiningDate()
    if request.method == "POST":
        form = CreateADiningDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            day = data["date_day"]
            time = data["date_time"]
            breakpoint()
            new_date = DatesNightModel.objects.create(
                users_one=request.user,
                users_two=data["users_two"],
                location=data["location"],
                when_date_time=datetime.strptime((day + time), "%m/%d/%Y%I:%M %p"),
            )
            new_date.dining_category.set(data["dining_category"])

            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data["users_two"],
            )
            return HttpResponseRedirect(reverse("homepage"))
    date_night_users = [
        {"instance": x[0], "value": x[1]} for x in form.fields["users_two"].choices
    ][1:]
    dates_to_pick = [
        {"instance": x[0], "value": x[1]}
        for x in form.fields["dining_category"].choices
    ][1:]

    return render(
        request,
        "date_night_activity_form.html",
        {
            "form": form,
            "dates_to_pick": dates_to_pick,
            "date_night_users": date_night_users,
        },
    )


def entertainment_date(request):
    if request.method == "POST":
        form = CreateAnEntertainmentDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                users_one=request.user,
                users_two=data["users_two"],
                location=data["location"],
                when_date_time=data["when_date_time"],
            )
            new_date.entertainment_category.set(data["entertainment_category"])
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data["users_two"],
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = CreateAnEntertainmentDate()
    return render(request, "form.html", {"form": form})


def outdoors_date(request):
    if request.method == "POST":
        form = CreateAnOutdoorsDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                out_doors_category=data["out_doors_category"],
                users_one=request.user,
                users_two=data["users_two"],
                location=data["location"],
                when_data_time=data["when_date_time"],
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data["users_two"],
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = CreateAnOutdoorsDate()
    return render(request, "form.html", {"form": form})


def stay_home_date(request):
    if request.method == "POST":
        form = CreateAStayHomeDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                stay_home_category=data["stay_home_category"],
                users_one=request.user,
                users_two=data["users_two"],
                location=data["location"],
                when_data_time=data["when_date_time"],
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data["users_two"],
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = CreateAStayHomeDate()
    return render(request, "form.html", {"form": form})
