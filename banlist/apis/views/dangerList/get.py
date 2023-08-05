# Internal stuff
from banlist.models import DangerList
from banlist.apis.serializers import DangerListSerializer
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def get_dangerlist(request, category_id):
    try:
        dangerlist = DangerList.objects.get(category__pk=category_id)
    except DangerList.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي لائحة لهذه الفئة"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = DangerListSerializer(dangerlist, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "حدث خطأ اثناء جلب قائمة الحظر لهذه الفئة.رجاءً أعد المحاولة مرةاخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
