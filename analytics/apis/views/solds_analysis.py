from solds.models import Sold

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


"""
diff = current_count - past_count
if current_count == 0:
    dividedVal = 0
else:
    dividedVal = diff / current_count
percentage = dividedVal * 100
return percentage
"""


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def monthly_sales_analysis(request):
    try:
        sales = Sold.objects.filter(sold_at__month=now.month)
        sales_count = sales.count()
        past_sales = Sold.objects.filter(
            sold_at__range=[one_month_ago, one_month_ago_end]
        ).all()
        past_sales_count = past_sales.count()
        profits = calculate_profits(sales, sales_count)
        past_profits = calculate_profits(past_sales, past_sales_count)
        print("Past profits:", past_profits)
        percentage = calculate_increase_percentage(profits, past_profits)

        return Response(
            {"profits": profits, "increase_percentage": percentage},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب الارباح الشهرية"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def monthly_sales(request):
    try:
        sales_count = Sold.objects.filter(sold_at__month=now.month).count()
        past_sales_count = Sold.objects.filter(
            sold_at__range=[one_month_ago, one_month_ago_end]
        ).count()
        percentage = calculate_increase_percentage(sales_count, past_sales_count)

        return Response(
            {"sales_count": sales_count, "increase_percentage": percentage},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب عدد المبيعات الشهرية"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def weekly_sales_analysis(request):
    try:
        sales = Sold.objects.filter(sold_at__range=[start_week, end_week])
        sales_count = sales.count()
        profits = calculate_profits(sales, sales_count)

        return Response(
            {"profits": profits},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب الارباح الاسبوعية"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def weekly_sales(request):
    try:
        sales_count = Sold.objects.filter(sold_at__range=[start_week, end_week]).count()

        return Response(
            {"sales_count": sales_count},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"message": "حدث خطأ اثناء جلب عدد المبيعات الاسبوعية"},
            status=status.HTTP_400_BAD_REQUEST,
        )
