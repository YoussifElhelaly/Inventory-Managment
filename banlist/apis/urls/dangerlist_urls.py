from django.urls import path

from banlist.apis.views.dangerList.create import create_dangerlist
from banlist.apis.views.dangerList.get import get_dangerlist
from banlist.apis.views.dangerList.update import update_dangerlist
from banlist.apis.views.dangerList.delete import delete_dangerlist

urlpatterns = [
    path("create/", create_dangerlist, name="create_dangerlist"),
    path("get/<int:category_id>/", get_dangerlist, name="get_dangerlist"),
    path("update/<int:category_id>/", update_dangerlist, name="update_dangerlist"),
    path("delete/<int:category_id>/", delete_dangerlist, name="delete_dangerlist"),
]
