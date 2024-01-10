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
