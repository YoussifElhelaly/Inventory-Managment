# Internal stuff
from notification.models import Notification

# from notification.apis.serializers import NotificationSerilaizer

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
def see_notification(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا الاشعار"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        notification.seen = True
        notification.save()
        return Response({"message": "تم قراءة الرسالة"}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء قراءة الرسالة الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
