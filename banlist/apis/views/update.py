# Internal stuff
from banlist.models import Banlist
from medicine.models import Medicine
from disease.models import Disease

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["PUT"])
@permission_classes([permissions.IsAdminUser])
def update_banlist(request, disease_id):
    data = request.data

    try:
        banlist = Banlist.objects.get(disease__pk=disease_id)
    except Banlist.DoesNotExist:
        return Response(
            {"message": "لا يوجد قائمة حظر لهذا المرض"},
            status=status.HTTP_404_NOT_FOUND,
        )

    disease = data.get("disease")
    medicines = data.get("medicines")

    try:
        is_updated = False
        # to avoid multiple SQL updates without need
        is_sql_updated = False

        if disease and disease != banlist.disease.name:
            try:
                disease_instance = Disease.objects.get(name=disease)
            except Disease.DoesNotExist:
                return Response(
                    {"message": "لم يتم العثور علي المرض"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            banlist.disease = disease_instance
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

            banlist.medicine.set(medicines_instances)
            is_updated = True

        if is_updated:
            if is_sql_updated:
                banlist.save()
            return Response(
                {"message": "تم تحديث قائمة الحظر بنجاح"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "لا يوجد شئ لتحديثه"}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception:
        return Response(
            {"message": "حدثت مشكلة اثناء انشاء القائمة"},
            status=status.HTTP_400_BAD_REQUEST,
        )
