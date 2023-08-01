from users.apis.serializers import LoginSerializer

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            access = serializer.validated_data.get("access", None)

            refresh = serializer.validated_data.get("refresh", None)

            user = serializer.validated_data.get("user", None)

            return Response(
                {"access": access, "refresh": refresh, "user": user},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"message": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
