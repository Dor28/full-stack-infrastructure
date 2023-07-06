import urllib.parse

import requests

from settings import controller1_base_url


class RequestSender:

    def get(self, uri, query_params=None):
        req_url = urllib.parse.urljoin(controller1_base_url, uri)
        resp = requests.get(req_url, params=query_params)
        if not resp.ok:
            raise

        return resp

    def post(self, uri, query_params=None, data=None):
        req_url = urllib.parse.urljoin(controller1_base_url, uri)
        resp = requests.post(req_url, json=data)
        if not resp.ok:
            print(resp.json())
            raise

        return resp

    def delete(self, uri):
        req_url = urllib.parse.urljoin(controller1_base_url, uri)
        resp = requests.delete(req_url)
        if not resp.ok:
            print(resp.json())
            raise

        return resp