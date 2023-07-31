# Internal stuff
from disease.models import Disease
from disease.apis.serializers import DiseaseSerializer

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
def get_diseases(request):
    try:
        diseases = Disease.objects.all().order_by("-added_at")
        serializer = DiseaseSerializer(diseases, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب الامراض من قواعد البيانات...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_disease(request, disease_id):
    try:
        disease = Disease.objects.get(pk=disease_id)
    except Disease.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا المرض"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        serializer = DiseaseSerializer(disease, many=False).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب المرض...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
