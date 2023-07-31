# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView

# simplejwt stuff
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            data = self.request.data

            refresh = data.get("refresh")
            print(refresh)
            token = RefreshToken(token=refresh)
            print(token)
            token.blacklist()
            return Response(
                {"message": "تم تسجيل الخروج بنجاح"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"message": "حدث خطأ ما...ربما تحتاج لاعادة تسجيل الدخول"},
                status=status.HTTP_400_BAD_REQUEST,
            )
