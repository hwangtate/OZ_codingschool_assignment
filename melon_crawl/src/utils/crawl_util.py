import requests
from bs4 import BeautifulSoup, ResultSet
from requests import Response


class CrawlUtil:
    __soup: BeautifulSoup
    __html: str
    __req: Response
    __url: object

    def __init__(self, url, header_user):
        self.__url = url
        self.__header_user = {"User-Agent": header_user}
        self.__req = requests.get(url, headers=self.__header_user)
        self.__html = self.__req.text
        self.__soup = BeautifulSoup(self.__html, 'html.parser')

    @property
    def url(self) -> object:
        return self.__url

    @property
    def request(self) -> Response:
        return self.__req

    @property
    def html(self) -> str:
        return self.__html

    @property
    def soup(self) -> BeautifulSoup:
        return self.__soup

    def select(self, var: str) -> ResultSet:
        query = self.__soup.select(var)
        return query


class CrawlInform:
    def __init__(self, url,header):
        self.__url = url
        self.__header = header

    @property
    def url(self) -> str:
        return self.__url

    @property
    def header(self):
        return self.__header


