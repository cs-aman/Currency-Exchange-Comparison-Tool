import unittest
from unittest.mock import patch
from Currency_Exchange_Comparison_Tool.python.code_file import get_exchange_rate, compare_rates

class TestCodeFile(unittest.TestCase):

    @patch('requests.get')
    def test_get_exchange_rate_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"USD": 1.2}}
        mock_get.return_value = mock_response

        api_url = "http://fake-api.com"
        result = get_exchange_rate(api_url)

        self.assertIsNotNone(result)
        self.assertEqual(result, {"rates": {"USD": 1.2}})

    @patch('requests.get')
    def test_get_exchange_rate_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        api_url = "http://fake-api.com"
        result = get_exchange_rate(api_url)

        self.assertIsNone(result)
        self.assertEqual(result, None)

    def test_compare_rates_fixer_beacon(self):
        rate_fixer = {"USD": 1.2}
        rate_beacon = {"USD": 1.5}

        result = compare_rates(rate_fixer, rate_beacon)

        self.assertEqual(result, "The Beacon Currency Exchange Providing Best Rates")

    def test_compare_rates_equal_rates(self):
        rate_fixer = {"USD": 1.2}
        rate_beacon = {"USD": 1.2}

        result = compare_rates(rate_fixer, rate_beacon)

        self.assertEqual(result, "Both Fixer and Beacon Providing Same Rates")

