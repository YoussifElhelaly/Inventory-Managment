from django.urls import path
from analytics.apis.views.solds_analysis import (
    monthly_sales_analysis,
    monthly_sales,
    weekly_sales_analysis,
    weekly_sales,
)

urlpatterns = [
    path("monthly-sales/", monthly_sales_analysis, name="monthly_sales_analysis"),
    path("monthly-orders/", monthly_sales, name="monthly_sales"),
    path("weekly-sales/", weekly_sales_analysis, name="weekly_sales_analysis"),
    path("weekly-orders/", weekly_sales, name="weekly_sales"),
]
