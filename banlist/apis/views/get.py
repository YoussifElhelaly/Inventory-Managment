# Internal stuff
from banlist.models import Banlist
from banlist.apis.serializers import BanlistSerializer
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def get_banlist(request, disease_id):
    try:
        banlist = Banlist.objects.get(disease__pk=disease_id)
    except Banlist.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي لائحة لهذا المرض"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = BanlistSerializer(banlist, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "حدث خطأ اثناء جلب قائمة الحظر لهذا المرض...رجاءً أعد المحاولة مرةاخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
