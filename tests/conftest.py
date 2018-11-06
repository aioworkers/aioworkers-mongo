import pytest


@pytest.fixture
def db_name():
    return 'test'


@pytest.fixture
def config():
    from aioworkers.core.config import Config
    return Config(
        mongo={
            'cls': 'aioworkers_mongo.base.Connector',
            'uri': 'mongodb://localhost:27017/',
        }
    )


@pytest.fixture
def context(config, loop):
    from aioworkers.core.context import Context
    with Context(config, loop=loop) as ctx:
        return ctx
