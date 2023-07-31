# Internal stuff
from banlist.models import Banlist
from medicine.models import Medicine
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_banlist(request):
    data = request.data

    if not data:
        return Response(
            {"message": "من فضلك ادخل البيانات"}, status=status.HTTP_400_BAD_REQUEST
        )

    disease = data.get("disease")
    medicines = data.get("medicines")

    if not disease:
        return Response(
            {"message": "يجب ادخال المرض"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        disease_instance = Disease.objects.get(name=disease)
    except Disease.DoesNotExist:
        return Response(
            {"message": "لم يتم العثور علي المرض"}, status=status.HTTP_404_NOT_FOUND
        )

    if not medicines or len(medicines) == 0:
        return Response({"message": "من فضلك"}, status=status.HTTP_400_BAD_REQUEST)

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
        banlist = Banlist.objects.create(disease=disease_instance)
        banlist.medicine.set(medicines_instances)
        return Response(
            {"message": "تم انشاء القائمة بنجاح"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدثت مشكلة اثناء انشاء القائمة"},
            status=status.HTTP_400_BAD_REQUEST,
        )
