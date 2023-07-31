# Internal stuff
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "PUT",
    ]
)
@permission_classes([permissions.IsAdminUser])
def update_disease(request, disease_id):
    data = request.data

    try:
        disease = Disease.objects.get(pk=disease_id)
    except Disease.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي المرض"}, status=status.HTTP_404_NOT_FOUND
        )

    if not data:
        return Response(
            {"message": "من فضلك ادخل بيانات المرض"}, status=status.HTTP_400_BAD_REQUEST
        )

    name = data.get("name")

    if not name:
        return Response(
            {"message": "من فضلك أدخل أسم المرض"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        if disease.name == name:
            return Response(
                {"message": "ادخل اسم مختلف"}, status=status.HTTP_400_BAD_REQUEST
            )

        is_disease_exists = Disease.objects.filter(name=name).exists()

        if is_disease_exists:
            return Response(
                {"message": "بالفعل هناك مرض مُسجل بهذا الأسم"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        disease.name = name
        disease.save()
        return Response({"message": "تم تعديل المرض بنجاح"}, status=status.HTTP_200_OK)

    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء تعديل المرض...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
