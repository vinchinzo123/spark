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
from users.views import handler404, handler500
from dates import views as dateViews
from notifications.views import (
    notification_view,
    decline_date_night_view,
    confirm_date_night_view,
    cancel_date_view,
)
from preferences.views import (
    AddADateOptionView,
    AddToCategoriesView,
    AddToEntertainmentOptionsView,
    AddToDiningOptionsView,
    AddToOutdoorsOptionsView,
    AddToStayHomeOptionsView,
)
from django.conf import settings
from django.conf.urls.static import static


handler404 = "users.views.handler404"
handler500 = "users.views.handler500"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="homepage"),
    path("user_image/", views.user_photo_view, name="user_image"),
    path("image_upload/", views.profile_image_view, name="image_upload"),
    path("success/", views.success, name="success"),
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
    path("preferences/", views.PreferencesUpdateView.as_view(), name="preferences"),
    path('add_a_date_option/', AddADateOptionView.as_view(), name='add_a_date_option'),
    path('add_a_category/', AddToCategoriesView.as_view()),
    path('entertainment/add_option/', AddToEntertainmentOptionsView.as_view(), name='add_to_entertainment'),
    path('dining/add_option/', AddToDiningOptionsView.as_view(), name='add_to_dining'),
    path('outdoors/add_option/', AddToOutdoorsOptionsView.as_view(), name='add_to_outdoors'),
    path('stayhome/add_option/', AddToStayHomeOptionsView.as_view(), name='add_to_stayhome'),
    # the following paths allows us to reroute the user back to the date_night form after adding an option
    path('create_a_date/entertainment/add_option/', AddToEntertainmentOptionsView.as_view(), name='add_entertainment_option'),
    path('create_a_date/dining/add_option/', AddToDiningOptionsView.as_view(), name='add_dining_option'),
    path('create_a_date/outdoors/add_option/', AddToOutdoorsOptionsView.as_view(), name='add_outdoors_option'),
    path('create_a_date/stayhome/add_option/', AddToStayHomeOptionsView.as_view(), name='add_stayhome_option'),

    path("pending_dates/", notification_view, name="pending_dates"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("sign_up/", views.SignupView.as_view(), name="sign_up_page"),
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
    path("cancel_date/<int:date_id>/", cancel_date_view),
    path("date_history/", dateViews.date_history_view),
    path("500error/", views.error500_view, name="500_error"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
