from soozpy.db_access import query_historical_prices
import pandas as pd


def get_historical_prices(from_date, to_date, symbols=None):
    # Call the function from db_access.py to get the query results
    results = query_historical_prices(from_date, to_date, symbols)

    # Convert the results to a DataFrame
    if results:
        df = pd.DataFrame([{
            'id': r.id,
            'symbol': r.symbol,
            'datetime': r.datetime,
            'price': r.price,
            'volume_24h': r.volume_24h
        } for r in results])
    else:
        df = pd.DataFrame()

    return df
