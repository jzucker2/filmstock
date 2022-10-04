from flask import current_app as app
import requests
from ...common.http_methods import HTTPMethods
from .client_response import ClientResponse


log = app.logger


class BaseClientException(Exception):
    pass


class BaseClient(object):
    def __repr__(self):
        return f'{self.__class__.__name__}'

    @classmethod
    def headers(cls):
        return {
            'Content-Type': 'application/json',
        }

    @classmethod
    def root_path(cls):
        raise BaseClientException('not implemented!')

    @classmethod
    def route_class(cls):
        raise BaseClientException('not implemented!')

    @classmethod
    def route_from_action(cls, action):
        return cls.route_class().from_action(action)

    @classmethod
    def method_from_action(cls, action):
        return cls.route_class().method_from_action(action)

    @classmethod
    def get_final_url(cls, url, root_path=None):
        if not root_path:
            root_path = cls.root_path()
        return f'{root_path}/{url}'

    def handle_request(
            self,
            url,
            method=HTTPMethods.DEFAULT,
            json=None):
        hr_m = f'{self} handle_request => ' \
               f'url: {url} with json: {json}'
        log.debug(hr_m)
        r = None
        if method == HTTPMethods.GET:
            r = requests.get(url)
        elif method == HTTPMethods.POST:
            r = requests.post(url, json=json, headers=self.headers())
        else:
            n_m = f'Not implemented for method: {method}'
            log.error(n_m)
            raise BaseClientException(n_m)
        status = r.status_code
        response_body = r.json()
        log.debug(f'{self}: {status}, response_body: {response_body}')
        response = ClientResponse(response_body=response_body)
        r_m = f'request: {url} got response: {response}'
        log.debug(r_m)
        return response
