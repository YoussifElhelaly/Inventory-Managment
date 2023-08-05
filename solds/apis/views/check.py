# Internal stuff
from solds.models import Sold, SoldItem
from medicine.models import Medicine
from banlist.models import Banlist, DangerList

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
        pass

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
        danger_list = DangerList.objects.get(category=medicine_instance.category)
    except DangerList.DoesNotExist:
        pass

    try:
        is_banned = False
        is_dangerous = False

        if type(banlist) != None:
            if banlist.medicine.contains(medicine_instance):
                is_banned = True

        if type(danger_list) != None:
            if danger_list.medicine.contains(medicine_instance):
                is_dangerous = True

        if is_banned:
            return Response(
                {"message": "هذا الدواء خطر علي المريض"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if is_dangerous:
            return Response(
                {"message": "هذا الدواء محظور بموجب لائحة طبية"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "هذا الدواء مسموح به للمريض"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return Response(
            {
                "message": "حدث خطأ اثناء فحص المنتج في قائمة المحظورات الرجاء المحاولة مرة اخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
