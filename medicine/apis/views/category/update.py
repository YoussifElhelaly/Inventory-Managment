# Internal stuff
from medicine.models import Category

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
def update_category(request, category_id):
    data = request.data

    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي القسم"}, status=status.HTTP_404_NOT_FOUND
        )

    if not data:
        return Response(
            {"message": "من فضلك ادخل بيانات القسم أو الفئة"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    name = data.get("name")

    if not name:
        return Response(
            {"message": "من فضلك أدخل أسم القسم"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        if name == category.name:
            return Response({"message": "من فضلك ادخل اسم مختلف"})

        is_category_exists = Category.objects.filter(name=name).exists()

        if is_category_exists:
            return Response(
                {"message": "هناك بالفعل قسم بهذا الاسم"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category.name = name
        category.save()
        return Response({"message": "تم تعديل القسم بنجاح"}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء تعديل الفئة...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
