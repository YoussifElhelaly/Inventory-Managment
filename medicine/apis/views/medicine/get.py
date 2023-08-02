# Internal stuff
from medicine.models import Medicine
from medicine.apis.serializers import MedicineSerializer

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_medicines(request):
    try:
        medicines = Medicine.objects.all().order_by("-added_at")
        serializer = MedicineSerializer(medicines, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "حدث خطأ اثناء جلب الادوية والمنتجات من قواعد البيانات...حاول مرة اخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_best_seller_medicines(request):
    try:
        medicines = Medicine.objects.all().order_by("-solds_count")
        serializer = MedicineSerializer(medicines, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "حدث خطأ اثناء جلب الادوية والمنتجات من قواعد البيانات...حاول مرة اخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_expire_soon_medicines(request):
    try:
        medicines = Medicine.objects.all().order_by("exp_date")
        serializer = MedicineSerializer(medicines, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {
                "message": "حدث خطأ اثناء جلب الادوية والمنتجات من قواعد البيانات...حاول مرة اخري"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_medicine(request, medicine_id):
    try:
        medicine = Medicine.objects.get(pk=medicine_id)
    except Medicine.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا الدواء"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = MedicineSerializer(medicine, many=False).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب الدواء...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_medicine_bycode(request, medicine_barcode):
    try:
        medicine = Medicine.objects.get(bar_code=medicine_barcode)
    except Medicine.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي هذا الدواء"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = MedicineSerializer(medicine, many=False).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
    except Exception:
        return Response(
            {"message": "حدث خطأ اثناء جلب الدواء...حاول مرة اخري"},
            status=status.HTTP_400_BAD_REQUEST,
        )
