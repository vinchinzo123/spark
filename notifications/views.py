from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

# Create your views here.


@login_required()
def notification_view(request):
    sent_notifications = Notification.objects.filter(sent_user=request.user.id)
    received_notifications = Notification.objects.filter(received_user=request.user.id)
    return render(
        request,
        "pending_dates.html",
        {
            "received_notifications": received_notifications,
            "sent_notifications": sent_notifications,
        },
    )
