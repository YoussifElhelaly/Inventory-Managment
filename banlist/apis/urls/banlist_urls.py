from django.urls import path
from banlist.apis.views.create import create_banlist
from banlist.apis.views.get import get_banlist
from banlist.apis.views.update import update_banlist
from banlist.apis.views.delete import delete_banlist

from banlist.apis.views.dangerList.create import create_dangerlist
from banlist.apis.views.dangerList.get import get_dangerlist
from banlist.apis.views.dangerList.update import update_dangerlist
from banlist.apis.views.dangerList.delete import delete_dangerlist

urlpatterns = [
    path("create/", create_banlist, name="create_banlist"),
    path("get/<int:disease_id>/", get_banlist, name="get_banlist"),
    path("update/<int:disease_id>/", update_banlist, name="update_banlist"),
    path("delete/<int:disease_id>/", delete_banlist, name="delete_banlist"),
]
