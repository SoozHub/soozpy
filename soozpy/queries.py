from soozpy.db_access import query_historical_prices, query_latest_prices
import pandas as pd


def get_historical_prices(from_date, to_date, symbols=None):
    # Call the function from db_access.py to get the query results
    results = query_historical_prices(from_date, to_date, symbols)

    # Convert the results to a DataFrame
    if results:
        df = pd.DataFrame([{
            'symbol': r.symbol,
            'datetime': r.datetime,
            'price': r.price,
            'volume': r.volume_24h
        } for r in results])
    else:
        df = pd.DataFrame()

    return df


def get_latest_prices(symbols=None):
    """
    Retrieve the latest price data for given symbols or all symbols if none are specified,
    and return the data as a pandas DataFrame.

    :param symbols: Optional list of symbols to query for. If None, queries for all symbols.
    :return: pandas DataFrame containing the latest price data.
    """
    # Call the function to get the latest prices
    results = query_latest_prices(symbols)

    # Convert the results to a DataFrame
    if results:
        df = pd.DataFrame([{
            'symbol': r.symbol,
            'datetime': r.datetime,
            'price': r.price,
            'volume': r.volume_24h
        } for r in results])
    else:
        df = pd.DataFrame()

    return df
