from django.urls import path
from medicine.apis.views.medicine.create import create_medicine
from medicine.apis.views.medicine.get import (
    get_medicine,
    get_medicine_bycode,
    get_medicines,
    get_best_seller_medicines,
    get_expire_soon_medicines,
)
from medicine.apis.views.medicine.update import update_medicine
from medicine.apis.views.medicine.delete import delete_medicine

urlpatterns = [
    path("create/", create_medicine, name="create_medicine"),
    path("get/<int:medicine_id>/", get_medicine, name="get_medicine"),
    path(
        "get-barcode/<int:medicine_barcode>/",
        get_medicine_bycode,
        name="get_medicine_bycode",
    ),
    path("get/all/", get_medicines, name="get_medicines"),
    path(
        "get/expire-soon/", get_expire_soon_medicines, name="get_expire_soon_medicines"
    ),
    path("update/<int:medicine_id>/", update_medicine, name="update_medicine"),
    path("delete/<int:medicine_id>/", delete_medicine, name="delete_medicine"),
]
