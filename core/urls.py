"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.apis.urls")),
    path("disease/", include("disease.apis.urls")),
    path("medicine/", include("medicine.apis.urls.medicine_urls")),
    path("category/", include("medicine.apis.urls.categories_urls")),
    path("notification/", include("notification.apis.urls")),
    path("solds/", include("solds.apis.urls")),
    path("banlist/", include("banlist.apis.urls.banlist_urls")),
    path("dangerlist/", include("banlist.apis.urls.dangerlist_urls")),
    path("analytics/", include("analytics.apis.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
