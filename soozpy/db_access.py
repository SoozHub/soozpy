from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env.example file
load_dotenv()
# Read the database URI from the environment variable
DATABASE_URI = os.getenv('SOOZHUB_DB_URI')


def create_session():
    """ Create and return a new SQLAlchemy session """
    # Create the database engine
    engine = create_engine(DATABASE_URI)

    # Create a Session class which will be a factory for new Session objects
    session = sessionmaker(bind=engine)

    return session()
