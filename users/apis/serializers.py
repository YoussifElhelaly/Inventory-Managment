from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone
from datetime import date


def update_last_login(user):
    user.last_login = date.today()
    user.save(update_fields=["last_login"])


class UserSerializer(serializers.ModelSerializer):
    date_created = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions")

    def get_date_created(self, obj):
        return humanize.naturaltime(obj.date_created)


class LoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": "لم نتمكن من العثور علي اي حساب بهذا البريد الالكتروني او كلمة المرور"
    }

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        # when the user logs in, we should update his last login to today's date
        update_last_login(self.user)
        data["user"] = UserSerializer(self.user).data
        return data
