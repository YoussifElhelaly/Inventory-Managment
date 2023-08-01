from django.urls import path
from users.apis.views.login import LoginView
from users.apis.views.register import register_admin
from users.apis.views.logout import LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register-admin/", register_admin, name="register_admin"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
