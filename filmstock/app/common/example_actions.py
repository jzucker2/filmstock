from enum import Enum


class ExampleActions(Enum):
    FOO = 'foo'
    BAR = 'bar'
    # ignore is special case
    IGNORE = 'ignore'  # spelling matters!
