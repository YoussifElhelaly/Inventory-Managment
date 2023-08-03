from django.urls import path
from solds.apis.views.check import check_medicine
from solds.apis.views.create import create_sale
from solds.apis.views.get import get_sold, get_solds
from solds.apis.views.delete import delete_sold

urlpatterns = [
    path("check-medicine/", check_medicine, name="check_medicine"),
    path("create/", create_sale, name="create_sale"),
    path("get/all/", get_solds, name="get_solds"),
    path("get/<sold_id>/", get_sold, name="get_sold"),
    path("delete/<sold_id>/", delete_sold, name="delete_sold"),
]
