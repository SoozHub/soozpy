import pandas as pd
from datetime import datetime
from soozpy.queries import get_historical_prices


def basic_test():
    # Define a date range for the test
    from_date = datetime(2023, 3, 9)
    to_date = datetime(2023, 4, 9)

    result = get_historical_prices(from_date, to_date, symbols=['BTC'])

    print(result.head())


if __name__ == "__main__":
    basic_test()
