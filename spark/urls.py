"""spark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views
from dates import views as dateViews
from notifications.views import (
    notification_view,
    decline_date_night_view,
    confirm_date_night_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="homepage"),
    path(
        "delete_profile/<int:profile_id>/",
        views.delete_profile_view,
        name="delete_profile",
    ),
    path(
        "update_profile/<int:profile_id>/",
        views.update_profile_view,
        name="update_profile",
    ),
    path("profile/<int:profile_id>/", views.profile_view, name="profile"),
    path("preferences/", views.preferences_view, name="preferences"),
    path("pending_dates/", notification_view, name="pending_dates"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("sign_up/", views.sign_up, name="sign_up_page"),
    path("create_a_date/", dateViews.create_a_date_view, name="create_a_date"),
    path("create_a_date/dining", dateViews.send_date_view, name="dining"),
    path(
        "create_a_date/entertainment",
        dateViews.send_date_view,
        name="entertainment",
    ),
    path("create_a_date/outdoors", dateViews.send_date_view, name="outdoors"),
    path("create_a_date/stayhome", dateViews.send_date_view, name="stayhome"),
    path(
        "datenight_detail/<int:date_id>/",
        dateViews.date_detail_view,
        name="datenight_detail",
    ),
    path("append_a_date/<int:notification_id>/", dateViews.receive_date_view),
    path("confirm_date/<int:notification_id>/", confirm_date_night_view),
    path("decline_date/<int:notification_id>/", decline_date_night_view),
]
