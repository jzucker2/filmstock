import asyncio
from flask import current_app as app
from ..base.base_client import (BaseClientException,
                                BaseClient)
from .example_routes import ExampleRoutes


log = app.logger


class ExampleClientException(Exception):
    pass


EXAMPLE_HOST = app.config.get('EXAMPLE_HOST')
EXAMPLE_PORT = app.config.get('EXAMPLE_PORT')


EXAMPLE_PATH =\
    f'http://{EXAMPLE_HOST}:{EXAMPLE_PORT}'


class ExampleException(BaseClientException):
    pass


class ExampleRequestException(ExampleException):
    pass


class ExampleClient(BaseClient):
    @classmethod
    def should_use_example(cls):
        config_value = app.config.get("SHOULD_USE_EXAMPLE")
        log.debug(f'for SHOULD_USE_EXAMPLE: {config_value}')
        return bool(str(config_value) == "1")

    @classmethod
    def root_path(cls):
        return EXAMPLE_PATH

    @classmethod
    def route_class(cls):
        return ExampleRoutes

    def get_example_response(self, action, data=None):
        route = self.route_from_action(action)
        method = self.method_from_action(action)
        g_m = f'action: {action} using route: {route} ' \
              f'with method: {method}'
        log.debug(g_m)
        url = self.get_final_url(route)
        log.debug(f'example get_example_response => using url: {url}')
        return self.handle_request(
            url,
            method=method,
            json=data)

    # this is the prod way

    async def example_request(self, action, data=None):
        await asyncio.sleep(0)
        s_m = f'example_client example_request ' \
              f'start for action: {action}'
        log.debug(s_m)
        try:
            result = self.get_example_response(action, data=data)
        except Exception as e:
            e_m = f'example_request for action: {action} ' \
                  f'got exception e: {e}'
            log.error(e_m)
            raise ExampleRequestException(e_m)
        else:
            f_m = f'example_client example_request for ' \
                  f'action: {action} ends with result: {result}'
            log.debug(f_m)
            return result

    async def perform_example_request(self, action, data=None):
        await asyncio.sleep(0)
        try:
            result = await self.example_request(action, data=data)
        except ExampleException as be:
            e_m = f'example_request for action: {action} ' \
                  f'got exception e: {be}'
            log.error(e_m)
            return False
        else:
            return result
