from abc import ABCMeta, abstractstaticmethod
import requests

class IRequestException(Exception):
    pass

class IRequest(metaclass=ABCMeta):

    @abstractstaticmethod
    def request_method():
        """ Interface Method """

    def as_json():
        """ Interface Method """
    
    def as_text():
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

class RequestFactory:

    @staticmethod
    def build_request(request_type: str, header: dict, params: dict, data: dict):
        if (request_type == "Get"):
            return Get(header=header, params=params)
        raise IRequestException("Invalid request type")

#req = RequestFactory.build_request("Get", header=None, params=None)
#req_method = req.request_method("https://steamcommunity.com")
#req.as_json(req_method)