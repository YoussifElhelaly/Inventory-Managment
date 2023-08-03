# Internal stuff
from solds.models import Sold, SoldItem

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["DELETE"])
@permission_classes([permissions.IsAdminUser])
def delete_sold(request, sold_id):
    try:
        sold = Sold.objects.get(pk=sold_id)
    except Sold.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي المبيعة"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        sold.delete()
        return Response({"message": "تم حذف المبيعة بنجاح"}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء حذف المبيعة الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
