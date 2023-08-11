from django.urls import path
from analytics.apis.views.solds_analysis import (
    monthly_sales_analysis,
    monthly_sales,
    weekly_sales_analysis,
    weekly_sales,
    daily_sales_analysis,
)
from analytics.apis.views.dangerlist_analysis import (
    monthly_danger_adds_analysis,
    weekly_danger_adds_analysis,
)

urlpatterns = [
    path("monthly-sales/", monthly_sales_analysis, name="monthly_sales_analysis"),
    path(
        "monthly-danger-adds/",
        monthly_danger_adds_analysis,
        name="monthly_danger_adds_analysis",
    ),
    path(
        "weekly-danger-adds/",
        weekly_danger_adds_analysis,
        name="weekly_danger_adds_analysis",
    ),
    path("monthly-orders/", monthly_sales, name="monthly_sales"),
    path("weekly-sales/", weekly_sales_analysis, name="weekly_sales_analysis"),
    path("weekly-orders/", weekly_sales, name="weekly_sales"),
    path("daily-sales/", daily_sales_analysis, name="daily_sales_analysis"),
]
