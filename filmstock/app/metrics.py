from enum import Enum
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
from prometheus_flask_exporter import Counter, Summary, Gauge


class Labels(Enum):
    ACTIVITY_NAME = 'activity_name'

    @classmethod
    def labels(cls):
        return list([
            cls.ACTIVITY_NAME.value,
        ])


EXAMPLE_TIME = Summary(
    'example_time_seconds',
    'Time spent on example function')


EXAMPLE_EXCEPTIONS_COUNTER = Counter(
    'example_exceptions',
    'Exceptions during example function')


EXAMPLE_GAUGE = Gauge(
    'example_gauge',
    'Example gauge during function')


# https://github.com/rycus86/prometheus_flask_exporter#app-factory-pattern
# https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/gunicorn-app-factory/app_setup.py
def get_metrics_app_factory():
    return GunicornPrometheusMetrics.for_app_factory()


metrics = get_metrics_app_factory()
