from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

# Create your views here.


@login_required()
def notification_view(request):
    """
    needs to fix when the declined note gets deleted
    and how to filter the notificaitons
    """
    sent_notifications = Notification.objects.filter(sent_user=request.user.id).filter(
        status="Sent"
    )
    active_notifications = [x for x in sent_notifications if x.status != "Declined"]
    declined_notifications = Notification.objects.filter(
        sent_user=request.user.id
    ).filter(status="Declined")
    dec_notes = []
    for note in declined_notifications:
        dec_notes.append(
            {"date_night": note.date_night, "received_user": note.received_user}
        )
        note.delete()
    received_notifications = Notification.objects.filter(
        received_user=request.user.id
    ).filter(status="Sent")
    return render(
        request,
        "pending_dates.html",
        {
            "received_notifications": received_notifications,
            "active_notifications": active_notifications,
            "declined_notifications": dec_notes,
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
