from flask import current_app as app
from ...common.http_methods import HTTPMethods


log = app.logger


class BaseClientRoutesException(Exception):
    pass


class BaseClientRoutes(object):
    @classmethod
    def from_action(cls, action):
        e_m = f'{cls.__name__} has no route for action: {action}'
        log.error(e_m)
        raise BaseClientRoutesException(e_m)

    @classmethod
    def post_actions(cls):
        n_m = f'{cls.__name__} post_actions not implemented'
        log.error(n_m)
        raise BaseClientRoutesException(n_m)

    @classmethod
    def method_from_action(cls, action):
        # FIXME: this is definitely brittle
        if action in cls.post_actions():
            return HTTPMethods.POST
        return HTTPMethods.GET
