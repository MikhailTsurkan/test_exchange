# functionality of standard unittest.TestCase  is sufficient
from unittest import TestCase

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from conf import settings
import time


class ExchangeAPITestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()

    def setUp(self):
        # api has permission 1 request/second for free plan,
        # change this setting to False, if you use paid tariff
        if settings.TEST_WAIT_FOR_NEXT_QUERY:
            time.sleep(1)

    def test_exchange_ok(self):
        data = {
            "from": "USD",
            "to": "EUR",
            "value": "3"
        }
        response = self.client.get(reverse("exchange:perform"), data=data, format="json")

        self.assertEqual(
            response.json(),
            {
                "result": 2.7696
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
            )

    def test_exchange_bad_value_type(self):
        data = {
            "from": "USD",
            "to": "EUR",
            "value": "f"
        }

        response = self.client.get(reverse("exchange:perform"), data=data, format="json")

        self.assertEqual(
            response.json(),
            {
                "error": "bad data for request"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_bad_request_to_exchange_api(self):
        data = {
            "from": "USD",
            "to": "TEST_BAD_CURRENCY",
            "value": "4.53"
        }

        response = self.client.get(reverse("exchange:perform"), data=data, format="json")

        self.assertEqual(
            response.json(),
            {
                "errors": [
                    "Target currency TEST_BAD_CURRENCY is not known"
                ]
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
