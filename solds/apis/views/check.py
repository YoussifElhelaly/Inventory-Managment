# Internal stuff
from solds.models import Sold, SoldItem
from medicine.models import Medicine
from banlist.models import Banlist

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "POST",
    ]
)
@permission_classes([permissions.IsAdminUser])
def check_medicine(request):
    data = request.data

    if not data:
        return Response(
            {"message": "من فضلك ادخل البيانات"}, status=status.HTTP_400_BAD_REQUEST
        )

    disease = data.get("disease")
    medicine = data.get("medicineId")

    if not disease:
        return Response(
            {"message": "من فضلك ادخل المرض"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        banlist = Banlist.objects.get(disease__name=disease)
    except Banlist.DoesNotExist:
        return Response(
            {"message": "لا يوجد لائحة حذر لهذا المرض"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if not medicine:
        return Response(
            {"message": "من فضلك ادخل الدواء لفحصه"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        medicine_instance = Medicine.objects.get(pk=medicine)
    except Medicine.DoesNotExist:
        return Response(
            {"message": "هذا الدواء ليس موجود"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        if banlist.medicine_set.contains(medicine_instance):
            return Response(
                {"message": "هذا الدواء خطر علي المريض"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "هذا الدواء مسموح به للمريض"}, status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {
                "message": "حدث خطأ اثناء فحص المنتج في قائمة المحظورات الرجاء المحاولة مرة اخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
