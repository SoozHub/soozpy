import unittest
from soozpy.queries import get_historical_prices
from datetime import datetime
import pandas as pd


class TestSoozPy(unittest.TestCase):

    def test_get_historical_prices_normal(self):
        """ Test get_historical_prices with standard parameters """
        from_date = datetime(2023, 3, 9)
        to_date = datetime(2023, 6, 9)
        symbols = ['BTC', 'ETH']

        result = get_historical_prices(from_date, to_date, symbols)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertNotEqual(len(result), 0)
        self.assertTrue(all(symbol in symbols for symbol in result['symbol'].unique()))

    def test_get_historical_prices_all_symbols(self):
        """ Test get_historical_prices with 'all' symbols """
        from_date = datetime(2023, 3, 9)
        to_date = datetime(2023, 6, 9)

        result = get_historical_prices(from_date, to_date)
        self.assertIsInstance(result, pd.DataFrame)

        # Check if DataFrame is not empty and has 'symbol' column
        if not result.empty and 'symbol' in result.columns:
            self.assertTrue(len(result['symbol'].unique()) > 1)
        else:
            self.fail("DataFrame is empty or missing 'symbol' column")

    def test_get_historical_prices_no_results(self):
        """ Test get_historical_prices with a date range having no results """
        from_date = datetime(2030, 1, 1)
        to_date = datetime(2030, 1, 31)

        result = get_historical_prices(from_date, to_date)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 0)

    # Add more test cases as needed, for example, testing invalid date ranges,
    # testing the handling of invalid symbol inputs, etc.


if __name__ == '__main__':
    unittest.main()
