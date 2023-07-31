from django.urls import path
from medicine.apis.views.category.create import create_category
from medicine.apis.views.category.update import update_category
from medicine.apis.views.category.get import get_categories, get_category
from medicine.apis.views.category.delete import delete_category


urlpatterns = [
    path("create/", create_category, name="create_category"),
    path("get/<int:category_id>/", get_category, name="get_category"),
    path("get/all/", get_categories, name="get_categories"),
    path("update/<category_id>/", update_category, name="update_category"),
    path("delete/<category_id>/", delete_category, name="delete_category"),
]
