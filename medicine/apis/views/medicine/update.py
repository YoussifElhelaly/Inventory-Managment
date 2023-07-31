# Internal stuff
from medicine.models import Medicine, Category

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
def update_medicine(request, medicine_id):
    data = request.data

    try:
        medicine = Medicine.objects.get(pk=medicine_id)
    except Medicine.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي الدواء"}, status=status.HTTP_404_NOT_FOUND
        )

    if not data:
        return Response(
            {"message": "من فضلك ادخل بيانات الدواء او المنتج للتعديل"},
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

    try:
        # indicator to indicate whether an modification happened or not
        is_updated = False
        if name and name != medicine.name:
            medicine.name = name
            is_updated = True

        if price and price != medicine.price:
            medicine.price = price
            is_updated = True

        if category and category != medicine.category.name:
            try:
                category_instance = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response(
                    {"message": "لا يوجد صنف مسجل بهذا الأسم"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            medicine.category = category_instance
            is_updated = True

        if description and description != medicine.description:
            medicine.description = description
            is_updated = True

        if prod_date and prod_date != medicine.prod_date:
            medicine.prod_date = prod_date
            is_updated = True

        if exp_date and exp_date != medicine.exp_date:
            medicine.exp_date = exp_date
            is_updated = True

        if medicine_img:
            medicine.medicine_img = medicine_img
            is_updated = True

        if stock and stock != medicine.stock:
            medicine.stock = stock
            is_updated = True

        if stock_warn_limit and stock_warn_limit != medicine.stock_warn_limit:
            medicine.stock_warn_limit = stock_warn_limit
            is_updated = True

        if bar_code and bar_code != medicine.bar_code:
            medicine.bar_code = bar_code
            is_updated = True

        if is_updated:
            medicine.save()
            return Response(
                {"message": "تم تحديث الدواء بنجاح"}, status=status.HTTP_200_OK
            )

        return Response(
            {"message": "لا يوجد شئ لتحديث"}, status=status.HTTP_400_BAD_REQUEST
        )

    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء تحديث الدواء الرجاء المحاولة مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
