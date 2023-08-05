from rest_framework import serializers
from banlist.models import Banlist, DangerList
from medicine.apis.serializers import MedicineSerializer, CategorySerializer


class BanlistSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True, many=True)

    class Meta:
        model = Banlist
        fields = "__all__"


class DangerListSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = DangerList
        fields = "__all__"
