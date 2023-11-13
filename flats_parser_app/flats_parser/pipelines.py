# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from sqlalchemy.orm import scoped_session

from greenlet import getcurrent
from database import create_table, SessionLocal
from .items import FlatItem
from models import Flat


class FlatsParserPipeline:
    """
    A class representing Scrapy pipeline for parsing flats from sreality.cz

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    process_item(self, item: FlatItem, spider):
        Process single item from sreality.cz
    """
    def __init__(self):
        """
        Initializes session and creates table in database.

        Parameters
        ----------
        """
        create_table()
        self.Session = scoped_session(SessionLocal, scopefunc=getcurrent)

    def process_item(self, item: FlatItem, spider):
        """
        Process single item from sreality.cz

        Parameters
        ----------
            itemm : FlatItem
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """
        logging.debug('process_item')
        session = self.Session()

        flat = Flat(**item)
        try:
            session.add(flat)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

