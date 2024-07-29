from unittest.mock import Mock, patch

from src.external_api import API_KEY, amount_transaction_in_rubles


def test_amount_transaction_in_rubles(transactions):
    transaction = transactions[2]
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "result": "616804.0"}
        mock_get.return_value = mock_response
        result = amount_transaction_in_rubles(transaction)

        assert result == 616804.0
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?from=USD&to=RUB&amount=9824.07",
            headers={"apikey": API_KEY},
        )
