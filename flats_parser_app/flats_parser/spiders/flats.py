import scrapy
from scrapy_playwright.page import PageMethod
import logging


class FlatsSpider(scrapy.Spider):
    name = "flats"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz"]
    pages_count = 20
    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.sreality.cz/hledani/prodej/byty?strana={page}'
            yield scrapy.Request(url, callback=self.parse_pages, meta={
                'playwright': True,
                'playwright_include_page': True,                'playwright_page_methods': [
                    # This where we can implement scrolling if we want
                    PageMethod(
                        'wait_for_selector', '.property')
                ]
            })

    async def parse_pages(self, response, **kwargs):
        for flat_element in response.css('.property'):
            yield {
                'name': flat_element.css('.name::text').get(),
                'image_url': flat_element.css('img')[0].attrib["src"]
            }