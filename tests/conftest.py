import pytest
from aioworkers.core.config import Config
from aioworkers.core.context import Context


@pytest.fixture
def config():
    return Config(
        mongo={
            'uri': 'mongodb://localhost:27017/',
        }
    )

@pytest.fixture
def context(config, loop):
    with Context(config, loop=loop) as ctx:
        return ctx
