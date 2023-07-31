# Internal stuff
from notification.models import Notification
from notification.apis.serializers import NotificationSerilaizer

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_notifications(request):
    try:
        notifications = Notification.objects.all().order_by("-sent_at")
        serializer = NotificationSerilaizer(notifications, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب الاشعارات الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
