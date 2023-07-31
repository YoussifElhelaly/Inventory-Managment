from django.urls import path
from .views.create import create_disease
from .views.delete import delete_disease
from .views.get import get_disease, get_diseases
from .views.update import update_disease


urlpatterns = [
    path("create/", create_disease, name="create_disease"),
    path("delete/<int:disease_id>/", delete_disease, name="delete_disease"),
    path("get/<int:disease_id>/", get_disease, name="get_disease"),
    path("get/all/", get_diseases, name="get_diseases"),
    path("update/<int:disease_id>/", update_disease, name="update_disease"),
]
