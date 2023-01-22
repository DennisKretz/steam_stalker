from abc import ABCMeta, abstractstaticmethod
from bs4 import BeautifulSoup

class IScraperException(Exception):
    pass

class IScraper(metaclass=ABCMeta):

    @abstractstaticmethod
    def scraper_method():
        """ Interface Method"""

    @abstractstaticmethod
    def by_class():
        """ Interface Method """

    @abstractstaticmethod
    def by_id():
        """ Interface Method """

    @abstractstaticmethod
    def text():
        """ Interface Method """

class Find(IScraper):

    def __init__(self, element: str):
        self._element = element

    def scraper_method(self, request_content: str):
        return BeautifulSoup(request_content, 'html.parser')

    def by_class(self, soup: BeautifulSoup):
        return soup.find(class_=self._element)

    def by_id(self, soup: BeautifulSoup):
        return soup.find(id=self._element)

    def text(self, soup_content: str):
        return soup_content.get_text()

class ScraperFactory:
    
    @staticmethod
    def find_data(data_type: int, element: str):
        if (data_type == 0):
            return Find(element=element)
        raise IScraperException("Invalid data type")