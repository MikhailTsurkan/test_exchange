from django.conf import settings
from requests import get


def get_anyapi_exchange(_from, _to):
    """
    func for retrieving rate from anyapi exchange
    """
    currencies = {
        "base": _from,
        "to": _to,
    }

    query_params = settings.EXCHANGE_DEFAULT_PARAMS | currencies
    response = get(url=settings.EXCHANGE_BASE_URL, params=query_params)
    response.raise_for_status()
    response_dict = response.json()

    assert isinstance(response_dict, dict)

    rate = response_dict.get("rate")

    return rate


def exchange(value, _from, _to, exchange_func=get_anyapi_exchange):
    """
    func for performing exchange
    """
    return value * exchange_func(_from, _to)
