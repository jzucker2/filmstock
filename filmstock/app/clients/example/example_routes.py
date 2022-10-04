from flask import current_app as app
from ...common.example_actions import ExampleActions
from ..base.base_client_routes import (BaseClientRoutesException,
                                       BaseClientRoutes)


log = app.logger


class ExampleRouteException(BaseClientRoutesException):
    pass


class ExampleRoutes(BaseClientRoutes):
    FOO = 'api/v1/foo'
    BAR = 'api/v1/bar'

    @classmethod
    def from_action(cls, action):
        # FIXME: this is definitely brittle
        if action == ExampleActions.FOO:
            return cls.FOO
        elif action == ExampleActions.BAR:
            return cls.BAR
        else:
            e_m = f'No route for action: {action}'
            log.error(e_m)
            raise ExampleRouteException(e_m)

    @classmethod
    def post_actions(cls):
        return []
