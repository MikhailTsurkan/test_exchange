from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchange/', include("exchange.urls", namespace="exchange"))
]
