# Internal stuff
from banlist.models import DangerList
from medicine.models import Medicine
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["DELETE"])
@permission_classes([permissions.IsAdminUser])
def delete_dangerlist(request, category_id):
    try:
        dangerlist = DangerList.objects.get(category__pk=category_id)
    except DangerList.DoesNotExist:
        return Response(
            {"message": "لا يوجد قائمة حظر لهذه الفئة"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        dangerlist.delete()
        return Response(
            {"message": "تم حذف هذه القائمة بنجاح"}, status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء الحذف برجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
