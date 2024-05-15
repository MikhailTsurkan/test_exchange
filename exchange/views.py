from requests import RequestException
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from exchange.services import exchange
from json import loads


@api_view(http_method_names=["GET"])
def exchange_view(request):
    """
    get from, to, value quey params and return result of exchange
    """
    _from = request.GET.get("from")
    _to = request.GET.get("to")
    value = request.GET.get("value")

    try:
        value = float(value)
    except ValueError:
        return Response({"error": "bad data for request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        result = exchange(value, _from, _to)
        return Response({"result": result})
    except RequestException as e:
        return Response(loads(e.response.content), status=e.response.status_code)
