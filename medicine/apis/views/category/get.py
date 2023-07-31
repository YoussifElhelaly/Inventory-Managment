# Internal stuff
from medicine.models import Category
from medicine.apis.serializers import CategorySerializer

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
def get_categories(request):
    try:
        categories = Category.objects.all().order_by("-added_at")
        serializer = CategorySerializer(categories, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب الاقسام من قواعد البيانات...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا القسم"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        serializer = CategorySerializer(category, many=False).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب القسم...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
