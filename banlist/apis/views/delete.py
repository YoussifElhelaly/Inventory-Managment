# Internal stuff
from banlist.models import Banlist
from medicine.models import Medicine
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["DELETE"])
@permission_classes([permissions.IsAdminUser])
def delete_banlist(request, disease_id):
    try:
        banlist = Banlist.objects.get(disease__pk=disease_id)
    except Banlist.DoesNotExist:
        return Response(
            {"message": "لا يوجد قائمة حظر لهذا المرض"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        banlist.delete()
        return Response(
            {"message": "تم حذف هذه القائمة بنجاح"}, status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء الحذف برجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
