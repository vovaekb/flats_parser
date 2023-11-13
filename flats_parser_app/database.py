from scrapy.utils.project import get_project_settings
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL


Base = declarative_base()
engine = sa.create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def create_table():
    """
    Creates table in database.

    Parameters
    ----------
    """
    Base.metadata.create_all(engine)
