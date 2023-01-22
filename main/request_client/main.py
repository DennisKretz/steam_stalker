from abc import ABCMeta, abstractstaticmethod
import requests
import json

class IRequestException(Exception):
    pass

class IRequest(metaclass=ABCMeta):

    @abstractstaticmethod
    def request_method():
        """ Interface Method """

    @abstractstaticmethod
    def as_json():
        """ Interface Method """

    @abstractstaticmethod
    def as_content():
        """ Interface Method """

class Get(IRequest):

    def __init__(self, params: dict, header: dict):
        self._params = params
        self._header = header

    def request_method(self, url: str):
        print("Get request")
        return requests.get(url, headers=self._header, params=self._params)

    def as_json(self, request_content):
        return request_content.json()

    def as_content(self, request_content):
        return request_content.content

class Post(IRequest):

    def __init__(self, data: dict, header: dict):
        self._data = data
        self._header = header

    def request_method(self, url: str):
        print("Post request")
        return requests.post(url, headers=self._header, data=json.loads(self._data))

    def as_json(self, request_content):
        return request_content.json()

    def as_content(self, request_content):
        return request_content.content

class RequestFactory:

    @staticmethod
    def build_request(request_type: str, header: dict, params: dict, data: dict):
        if (request_type == 0):
            return Get(header=header, params=params)
        if (request_type == 1):
            return Post(header=header, data=data)
        raise IRequestException("Invalid request type")
