# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FlatItem(Item):
    """
        A class to represent a person.
        ...

        Attributes
        ----------
        name : str
            title of ad for selling the flat
        image_url : int
            URL of the first image in ad

        Methods
        -------
        """
    name = Field()
    image_url = Field()
