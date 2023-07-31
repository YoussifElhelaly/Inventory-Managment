# Internal stuff
from medicine.models import Medicine

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes([permissions.IsAdminUser])
def delete_medicine(request, medicine_id):
    try:
        medicine = Medicine.objects.get(pk=medicine_id)
    except Medicine.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا الدواء"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        medicine.delete()
        return Response({"message": "تم حذف الدواء بنجاح"}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء حذف الدواء...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
