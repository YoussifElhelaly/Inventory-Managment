# Internal suff
from users.models import User
from users.apis.serializers import UserSerializer
from django.contrib.auth.hashers import make_password

# DRF stuff
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import permissions

# simplejwt stuff
from rest_framework_simplejwt.tokens import RefreshToken

from email_validator import validate_email, EmailNotValidError


def generate_token_for_user(user):
    """
    function return an access and refresh token for particular user

    """
    token = RefreshToken.for_user(user)

    return {
        "access": str(token.access_token),
        "refresh": str(token),
    }


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def register_admin(request):
    data = request.data

    if not data:
        return Response(
            {"message": "برجاء ادخال بيانات"}, status=status.HTTP_400_BAD_REQUEST
        )

    full_name = data.get("fullName")
    email = data.get("email")
    password = data.get("password")

    if not full_name:
        return Response(
            {"message": "برجاء ادخال اسم الصيدلي بالكامل"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    is_name_exists = User.objects.filter(full_name=full_name).exists()

    if is_name_exists:
        return Response(
            {"message": "هناك بالفعل صيدلي بهذالأسم"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not email:
        return Response(
            {"message": "يجب ادخال البريد الالكتروني الخاص بالصيدلي"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        is_email_valid = validate_email(email=email, check_deliverability=False)
    except EmailNotValidError:
        return Response(
            {"message": "رجاءً أدخل بريد الكتروني صالح"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    is_email_exists = User.objects.filter(email=email).exists()

    if is_email_exists:
        return Response(
            {"message": "هناك بالفعل صيدلي بهذالبريد الالكتروني"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not password:
        return Response(
            {"message": "من فضلك أدخل كلمة مرور للصيدلي"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(password) < 6:
        return Response(
            {"message": "يجب أن تكون كلمة المرور أكبر من ستة احرف او ارقام"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(password) > 16:
        return Response(
            {"message": "لا يمكن أن تكون كلمة المرور اكثر من 16 حرفاً او رقم"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = User.objects.create(
            full_name=full_name,
            email=email,
            password=make_password(password),
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        serializer = UserSerializer(user, many=False)

        return Response(
            {
                "user": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {"message": "حدث خطأ غير متوقع"}, status=status.HTTP_400_BAD_REQUEST
        )
