# Internal stuff
from solds.models import Sold
from solds.apis.serializers import SoldSerializer

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
def get_solds(request):
    try:
        solds = Sold.objects.all().order_by("-sold_at")
        serializer = SoldSerializer(solds, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب المبيعات الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_sold(request, sold_id):
    try:
        sold = Sold.objects.get(pk=sold_id)
    except Sold.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذه المبيعة"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = SoldSerializer(sold, many=False).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب البيعة الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
