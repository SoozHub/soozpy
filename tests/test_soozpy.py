import unittest
from soozpy.queries import get_historical_prices, get_latest_prices
from datetime import datetime
import pandas as pd


class TestSoozPy(unittest.TestCase):

    # get_historical_prices tests

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

    # get_latest_price tests

    def test_get_latest_prices_specific_symbols(self):
        """ Test get_latest_price with specific symbols """
        symbols = ['BTC', 'ETH']

        result = get_latest_prices(symbols)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertNotEqual(len(result), 0)
        self.assertTrue(all(symbol in symbols for symbol in result['symbol'].unique()))

    def test_get_latest_prices_all_symbols(self):
        """ Test get_latest_price with 'all' symbols """
        result = get_latest_prices()
        self.assertIsInstance(result, pd.DataFrame)

        # Check if DataFrame is not empty and has 'symbol' column
        if not result.empty and 'symbol' in result.columns:
            self.assertTrue(len(result['symbol'].unique()) > 1)
        else:
            self.fail("DataFrame is empty or missing 'symbol' column")

    def test_get_latest_prices_no_results(self):
        """ Test get_latest_price when there are no results """
        # Assuming a scenario where no results would be returned
        # This may depend on the setup of your database and data availability
        symbols = ['NON_EXISTENT_SYMBOL']

        result = get_latest_prices(symbols)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
