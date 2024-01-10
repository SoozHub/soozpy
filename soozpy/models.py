from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CoinMarketCapData(Base):
    __tablename__ = 'coinmarketcap_data'

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    datetime = Column(DateTime)
    price = Column(Float)
    volume_24h = Column(Float)
