from django.urls import path
from notification.apis.views.get import get_notifications
from notification.apis.views.post import see_notification

urlpatterns = [
    path("get/all/", get_notifications, name="get_notifications"),
    path("see/<notification_id>/", see_notification, name="see_notification"),
]
