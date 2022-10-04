import os
import logging


basedir = os.path.abspath(os.path.dirname(__file__))


def engine_options(is_sqlite):
    if is_sqlite:
        return {
            'pool_recycle': int(os.environ.get('DB_POOL_RECYCLE', 240)),
            'pool_pre_ping': True,
        }
    return {
        'pool_size': int(os.environ.get('DB_POOL_SIZE', 40)),
        'pool_recycle': 240,
        # https://docs.sqlalchemy.org/en/14/core/pooling.html#reset-on-return
        # options: `True`, `False`, or `'debug'`
        'echo_pool': os.environ.get('DB_ECHO_POOL', False),
        'max_overflow': int(os.environ.get('DB_MAX_OVERFLOW', 80)),
    }


ENV_FILMSTOCK_HOST = os.getenv(
    "FILMSTOCK_HOST",
    default="0.0.0.0")
ENV_FILMSTOCK_PORT = int(os.getenv(
    "FILMSTOCK_PORT",
    default=1915))


class base_config(object):
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'FILMSTOCK')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secrets')

    # WARNING: messing with the below breaks routing
    # SERVER_NAME = os.getenv("FILMSTOCK_HOST", default="0.0.0.0")
    FILMSTOCK_HOST = ENV_FILMSTOCK_HOST
    FILMSTOCK_PORT = ENV_FILMSTOCK_PORT

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail')
    MAIL_PORT = os.environ.get('MAIL_PORT', 1025)

    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)

    CACHE_HOST = os.environ.get('MEMCACHED_HOST', 'memcached')
    CACHE_PORT = os.environ.get('MEMCACHED_PORT', 11211)

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'postgres')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
    #                                          DEFAULT_DB_URI)
    # https://stackoverflow.com/questions/34009296/using-sqlalchemy-session-from-flask-raises-sqlite-objects-created-in-a-thread-c  # noqa: E501
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,
                                                          "app.db") + "?check_same_thread=False"  # noqa: E501
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SUPPORTED_LOCALES = ['en']

    IS_SQLITE = SQLALCHEMY_DATABASE_URI.startswith('sqlite:///')

    # https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine
    SQLALCHEMY_ENGINE_OPTIONS = engine_options(IS_SQLITE)

    FILMSTOCK_LOGGING_LEVEL = os.environ.get(
        'FILMSTOCK_LOGGING_LEVEL',
        logging.INFO)

    APP_DIR = os.path.dirname(__file__)
    MIGRATION_DIRECTORY = os.path.join(APP_DIR, "migrations")

    # custom client code
    # example (sound effects)
    # FIXME: what's the best way to do routing?
    EXAMPLE_HOST = os.getenv("EXAMPLE_HOST",
                             default="10.0.1.128")
    EXAMPLE_PORT = int(os.getenv("EXAMPLE_PORT",
                                 default=1929))
    SHOULD_USE_EXAMPLE = os.getenv("SHOULD_USE_EXAMPLE",
                                   default="1")


class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
