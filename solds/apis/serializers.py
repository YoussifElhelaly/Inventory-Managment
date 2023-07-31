from rest_framework import serializers
from solds.models import Sold, SoldItem
from medicine.apis.serializers import MedicineSerializer


class SoldItemSerializer(serializers.ModelSerializer):
    pharmacist = serializers.SerializerMethodField()
    medicine = MedicineSerializer(read_only=True, many=False)

    class Meta:
        model = SoldItem
        fields = "__all__"

    def get_pharmacist(self, obj):
        return obj.pharmacist.full_name


class SoldSerializer(serializers.ModelSerializer):
    pharmacist = serializers.SerializerMethodField()
    sold_items = serializers.SerializerMethodField()

    class Meta:
        model = Sold
        fields = "__all__"

    def get_pharmacist(self, obj):
        return obj.pharmacist.full_name

    def get_sold_items(self, obj):
        sold_items = obj.sold_items.all()
        sold_tiems_serializers = SoldItemSerializer(sold_items, many=True)
        return sold_tiems_serializers.data
