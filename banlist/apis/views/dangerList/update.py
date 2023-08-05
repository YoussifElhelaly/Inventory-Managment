# Internal stuff
from banlist.models import DangerList
from medicine.models import Medicine, Category

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["PUT"])
@permission_classes([permissions.IsAdminUser])
def update_dangerlist(request, category_id):
    data = request.data

    try:
        dangerlist = DangerList.objects.get(category__pk=category_id)
    except DangerList.DoesNotExist:
        return Response(
            {"message": "لا يوجد قائمة حظر لهذه الفئة"},
            status=status.HTTP_404_NOT_FOUND,
        )

    category = data.get("category")
    medicines = data.get("medicines")

    try:
        is_updated = False
        # to avoid multiple SQL updates without need
        is_sql_updated = False

        if category and category != dangerlist.category.name:
            try:
                category_instance = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response(
                    {"message": "لم يتم العثور علي الفئة"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            dangerlist.category = category_instance
            is_updated = True
            is_sql_updated = True

        if medicines:
            medicines_instances = []

            for medicine in medicines:
                try:
                    medicines_instance = Medicine.objects.get(pk=medicine["id"])
                except Medicine.DoesNotExist:
                    return Response(
                        {
                            "message": f"المنتج ذو الباركود: {medicine['barcode']} ليس موجود"
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )

                medicines_instances.append(medicines_instance)

            dangerlist.medicine.set(medicines_instances)
            is_updated = True

        if is_updated:
            if is_sql_updated:
                dangerlist.save()
            return Response(
                {"message": "تم تحديث قائمة الحظر بنجاح"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "لا يوجد شئ لتحديثه"}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception:
        return Response(
            {"message": "حدثت مشكلة اثناء تحديث القائمة"},
            status=status.HTTP_400_BAD_REQUEST,
        )
