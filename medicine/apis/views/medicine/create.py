# Internal stuff
from medicine.models import Medicine, Category

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
def create_medicine(request):
    data = request.data

    if not data:
        return Response(
            {"message": "من فضلك ادخل بيانات الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    name = data.get("name")
    price = data.get("price")
    category = data.get("category")
    description = data.get("description")
    prod_date = data.get("prodDate")
    exp_date = data.get("expDate")
    medicine_img = data.get("medicineImg")
    stock = data.get("stock")
    stock_warn_limit = data.get("stockWarnLimit")
    bar_code = data.get("barCode")

    if not name:
        return Response(
            {"message": "من فضلك ادخل اسم الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not price:
        return Response(
            {"message": "من فضلك ادخل سعر الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not category:
        return Response(
            {"message": "من فضلك ادخل صنف الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        category_instance = Category.objects.get(name=category)
    except Category.DoesNotExist:
        return Response(
            {"message": "لا يوجد صنف مسجل بهذا الأسم"}, status=status.HTTP_404_NOT_FOUND
        )

    if not prod_date:
        return Response(
            {"message": "من فضلك ادخل تاريخ انتاج الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not exp_date:
        return Response(
            {"message": "من فضلك ادخل ناريخ انتهاء صالحية الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not medicine_img:
        return Response(
            {"message": "من فضلك ادخل صورة الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not medicine_img:
        return Response(
            {"message": "من فضلك ادخل صورة الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not stock:
        return Response(
            {"message": "من فضلك ادخل المخزون المتوفر من الدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not stock_warn_limit:
        return Response(
            {
                "message": "من فضلك ادخل الحد الادني لمخزون الدواء او المنتج وسيتم ارسال اشعار لك عند وصول المخزون لهذا الحد"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not bar_code:
        return Response(
            {"message": "من فضلك ادخل الباركود الخاص بالدواء او المنتج"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Medicine.objects.create(
            name=name,
            price=price,
            category=category_instance,
            description=description,
            prod_date=prod_date,
            exp_date=exp_date,
            medicine_img=medicine_img,
            stock=stock,
            stock_warn_limit=stock_warn_limit,
            bar_code=bar_code,
        )
        return Response({"message": "تم انشاء الدواء بنجاح"}, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء انشاء الدواء الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
