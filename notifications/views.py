from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

# Create your views here.


@login_required()
def notification_view(request):
    sent_notifications = Notification.objects.filter(sent_user=request.user.id)
    active_notifications = [x for x in sent_notifications if x.status != "Declined"]
    declined_notifications = []
    for note in sent_notifications:
        if note.status == "Declined":
            declined_notifications.append(
                {"date_night": note.date_night, "received_user": note.received_user}
            )
            note.delete()
    received_notifications = Notification.objects.filter(received_user=request.user.id)
    return render(
        request,
        "pending_dates.html",
        {
            "received_notifications": received_notifications,
            "active_notifications": active_notifications,
            "declined_notifications": declined_notifications,
        },
    )


@login_required()
def decline_date_night_view(path, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.status = "Declined"
    notification.received_user = None
    notification.save()
    return redirect("/pending_dates/")


@login_required()
def confirm_date_night_view(path, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.status = "Confirmed"
    notification.save()
    return redirect(f"/append_a_date/{notification.date_night.id}")
