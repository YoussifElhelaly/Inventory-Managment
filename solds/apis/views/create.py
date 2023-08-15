# Internal stuff
from solds.models import Sold, SoldItem
from medicine.models import Medicine
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_sale(request):
    data = request.data
    user = request.user

    if not data:
        return Response(
            {"message": "من فضلك ادخل البيانات"}, status=status.HTTP_400_BAD_REQUEST
        )

    medicines = data.get("medicines")
    disease = data.get("disease")

    if not medicines or len(list(medicines)) < 1:
        return Response(
            {"message": "الرجاء ادخال الادوية المراد بيعها"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not disease:
        return Response(
            {"message": "الرجاء ادخال المرض"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        disease_instance = Disease.objects.get(name=disease)
    except Disease.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي مرض بهذا الاسم"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        # establish a sold for the sold items items
        sold = Sold.objects.create(
            pharmacist=user,
            disease=disease_instance,
        )
        total_price = 0
        total_quantities = 0
        for medicine in medicines:
            try:
                item = Medicine.objects.get(pk=medicine["id"])
            except Medicine.DoesNotExist:
                return Response(
                    {"message": f"الدواء ذو الباركود {medicine['bar_code']} ليس مُسجل"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if medicine["quantity"] > item.stock:
                return Response(
                    {"message": "المخزون الحالي اقل من الكمية المراد بيعها"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            sold_item = SoldItem.objects.create(
                medicine=item,
                quantity=int(medicine["quantity"]),
                pharmacist=user,
                sold=sold,
            )
            item.stock -= int(medicine["quantity"])
            item.solds_count += 1
            item.save()
            total_price += sold_item.total
            total_quantities += int(medicine["quantity"])

        sold.total = total_price
        sold.quantities = total_quantities
        sold.save()
        return Response({"message": "تم انشاء مبيعة بنجاح"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"message": f"حدث خطأ اثناء انشاء المبيعة...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
