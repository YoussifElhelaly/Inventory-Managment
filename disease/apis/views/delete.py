# Internal stuff
from disease.models import Disease

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
def delete_disease(request, disease_id):
    try:
        disease = Disease.objects.get(pk=disease_id)
    except Disease.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا المرض"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        disease.delete()
        return Response({"message": "تم حذف المرض بنجاح"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء حذف المرض...الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
