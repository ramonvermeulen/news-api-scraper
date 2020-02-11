import requests
import logging
import sys
import datetime


class APIProvider:
    def __init__(self, api_uri, api_key, api_key_query_keyword, api_route, query_keyword, query_search):
        self.api_uri = api_uri
        self.api_key = api_key
        self.api_key_query_keyword = api_key_query_keyword
        self.api_route = api_route
        self.query_keyword = query_keyword
        self.query_search = query_search
        self.request_failed_counter = 0
        self._setup_logger()

    @staticmethod
    def _setup_logger():
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    def fetch_data(self):
        try:
            request_url = f'{self.api_uri}/{self.api_route}?{self.api_key_query_keyword}={self.api_key}' \
                          f'&{self.query_keyword}={self.query_search}'
            print(request_url)
            response = requests.get(request_url)
            if response.ok:
                self.request_failed_counter = 0
                return [response.json(), self.request_failed_counter]
            else:
                self.request_failed_counter += 1
                return [None, self.request_failed_counter]
        except Exception as e:
            self.request_failed_counter += 1
            logging.exception(f'[{datetime.datetime.now()}] - Error during network request in APIProvider class')
