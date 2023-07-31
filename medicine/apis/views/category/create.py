# Internal stuff
from medicine.models import Category

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
def create_category(request):
    data = request.data

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

    is_category_exists = Category.objects.filter(name=name).exists()

    if is_category_exists:
        return Response(
            {"message": "هناك بالفعل قسم بهذا الاسم"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Category.objects.create(name=name)
        return Response(
            {"message": "تم انشاء التصنيف بنجاح"}, status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء تسجيل التصنيف...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
