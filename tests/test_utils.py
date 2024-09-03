import json
from unittest.mock import mock_open, patch

from src.utils import list_from_json


def test_list_from_json_valid_file(transactions):
    json_data = json.dumps(transactions)
    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            result = list_from_json("test_path.json")
            assert result == transactions
            mocked_open.assert_called_once_with("test_path.json", "r", encoding="utf-8")
