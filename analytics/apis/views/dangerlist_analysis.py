from solds.models import Sold
from banlist.models import CountSaleDanger

# DRF stuff
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from globals.utils import (
    calculate_increase_percentage,
    calculate_profits,
    one_month_ago,
    one_month_ago_end,
    now,
    start_week,
    end_week,
)


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def monthly_danger_adds_analysis(request):
    try:
        danger_count = CountSaleDanger.objects.filter(
            attempted_at__month=now.month
        ).count()
        past_danger_count = CountSaleDanger.objects.filter(
            attempted_at__range=[one_month_ago, one_month_ago_end]
        ).count()
        percentage = calculate_increase_percentage(danger_count, past_danger_count)

        return Response(
            {"count": danger_count, "increase_percentage": percentage},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب عدد مرات بيع دواء محظور بموجب لائحة طبية"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def weekly_danger_adds_analysis(request):
    try:
        danger_count = CountSaleDanger.objects.filter(
            attempted_at__range=[start_week, end_week]
        ).count()

        return Response(
            {"count": danger_count},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب الارباح الشهرية"},
            status=status.HTTP_400_BAD_REQUEST,
        )
