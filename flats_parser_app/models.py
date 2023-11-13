from scrapy.utils.project import get_project_settings
import sqlalchemy as sa
from database import Base


class Flat(Base):
    """
    A class to represent a person.
    ...
    Attributes
    ----------
    id : str
        ID of flat
    name : str
        title of ad for selling the flat
    image_url : int
        URL of the first image in ad

    Methods
    -------
    """
    __tablename__ = "flats"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), index=True, nullable=False)
    image_url = sa.Column(sa.String(255), index=True, nullable=False)
