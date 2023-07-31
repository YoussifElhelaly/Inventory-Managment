# Internal stuff
from medicine.models import Category

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes([permissions.IsAdminUser])
def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا القسم"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        category.delete()
        return Response(
            {"message": "تم حذف القسم بنجاح"}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء حذف القسم"}, status=status.HTTP_400_BAD_REQUEST
        )
