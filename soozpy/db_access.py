from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from soozpy.models import CoinMarketCapData


def create_session():
    """ Create and return a new SQLAlchemy session """
    # Load environment variables from .env.example file
    load_dotenv()
    # Read the database URI from the environment variable
    DATABASE_URI = os.getenv('SOOZHUB_DB_URI')

    # Create the database engine
    engine = create_engine(DATABASE_URI)

    # Create a Session class which will be a factory for new Session objects
    session = sessionmaker(bind=engine)

    return session()


def query_historical_prices(from_date, to_date, symbols=None):
    session = create_session()
    try:
        query = session.query(CoinMarketCapData)

        # Check if a specific list of symbols is provided
        if symbols is not None:
            query = query.filter(CoinMarketCapData.symbol.in_(symbols))

        query = query.filter(
            CoinMarketCapData.datetime >= from_date,
            CoinMarketCapData.datetime <= to_date
        )

        return query.all()
    finally:
        session.close()


def query_latest_prices(symbols=None):
    """
    Query and return the latest prices for given symbols, or all symbols if none are specified.

    :param symbols: Optional list of symbols to query for. If None, queries all symbols.
    :return: List of CoinMarketCapData objects representing the latest prices.
    """
    session = create_session()
    try:
        # Start with a base query
        query = session.query(CoinMarketCapData)

        # Filter by symbols if provided
        if symbols is not None:
            query = query.filter(CoinMarketCapData.symbol.in_(symbols))

        # Order by datetime descending and get the first record for each symbol
        query = query.order_by(CoinMarketCapData.symbol, CoinMarketCapData.datetime.desc())

        # Using distinct on symbol to get the latest record per symbol
        latest_prices = query.distinct(CoinMarketCapData.symbol).all()

        return latest_prices
    finally:
        session.close()
