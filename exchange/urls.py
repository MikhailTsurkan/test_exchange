from django.urls import path

from exchange import views
from exchange.apps import ExchangeConfig


app_name = ExchangeConfig.name


urlpatterns = [
    path("perform/", views.exchange_view, name="perform"),
]
