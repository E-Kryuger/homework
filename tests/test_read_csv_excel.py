from unittest.mock import patch

import pandas as pd

from src.read_csv_excel import read_transactions_csv, read_transactions_excel


def test_read_transactions_csv_valid_file(transactions):
    data = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    with patch("pandas.read_csv", return_value=data) as mock_read_csv:
        with patch("os.path.exists", return_value=True):
            result = read_transactions_csv("dummy_path.csv")
            expected_result = data.to_dict(orient="records")
            assert result == expected_result
            mock_read_csv.assert_called_once_with("dummy_path.csv", delimiter=";")


def test_read_transactions_excel_valid_file(transactions):
    data = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    with patch("pandas.read_excel", return_value=data) as mock_read_excel:
        with patch("os.path.exists", return_value=True):
            result = read_transactions_excel("dummy_path.xlsx")
            expected_result = data.to_dict(orient="records")
            assert result == expected_result
            mock_read_excel.assert_called_once_with("dummy_path.xlsx")
