from dataclasses import dataclass, asdict
from flask import current_app as app


log = app.logger


@dataclass(frozen=True)
class ClientResponse:
    response_body: dict

    def get_info(self):
        return asdict(self)

    @property
    def has_response(self):
        # FIXME: this is NOT pythonic
        response = self.response_body.get('response')
        if response is not None:
            return True
        return False

    def get_response(self):
        return self.response_body.get('response', {})

    def __str__(self):
        return f'{self.__class__.__name__} => ' \
               f'has_response: {self.has_response} with ' \
               f'response_body: {self.response_body}'
