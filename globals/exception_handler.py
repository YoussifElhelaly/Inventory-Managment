from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    """
    this mainly used to add a customized unauthorized error messages
    """
    if isinstance(exc, NotAuthenticated):
        return Response(
            {
                "message": "لم يتم توفير أوراق اعتماد المصادقة...حاول تسجيل الدخول من ثم القيام بنفس الفعل"
            },
            status=401,
        )

    # else
    # default case
    return exception_handler(exc, context)
