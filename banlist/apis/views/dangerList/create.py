# Internal stuff
from banlist.models import DangerList
from medicine.models import Medicine, Category

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_dangerlist(request):
    data = request.data

    if not data:
        return Response(
            {"message": "من فضلك ادخل البيانات"}, status=status.HTTP_400_BAD_REQUEST
        )

    category = data.get("category")
    medicines = data.get("medicines")

    if not category:
        return Response(
            {"message": "يجب ادخال الفئة"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        category_instance = Category.objects.get(name=category)
    except Category.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي الفئة"}, status=status.HTTP_404_NOT_FOUND
        )

    is_dangerlist_exists = DangerList.objects.filter(
        category=category_instance
    ).exists()

    if is_dangerlist_exists:
        return Response(
            {"message": "يوجد بالفعل قائمة حظر لهذه الفئة"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not medicines or len(list(medicines)) == 0:
        return Response(
            {"message": "من فضلك ادخل الادوية"}, status=status.HTTP_400_BAD_REQUEST
        )

    medicines_instances = []

    for medicine in medicines:
        try:
            medicines_instance = Medicine.objects.get(pk=medicine["id"])
        except Medicine.DoesNotExist:
            return Response(
                {"message": f"المنتج ذو الباركود: {medicine['barcode']} ليس مُسجل"},
                status=status.HTTP_404_NOT_FOUND,
            )

        medicines_instances.append(medicines_instance)

    try:
        dangerlist = DangerList.objects.create(category=category_instance)
        dangerlist.medicine.set(medicines_instances)
        return Response(
            {"message": "تم انشاء القائمة بنجاح"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدثت مشكلة اثناء انشاء القائمة"},
            status=status.HTTP_400_BAD_REQUEST,
        )
