import pytest
from aioworkers.core.config import Config


@pytest.fixture
def config():
    return Config(mongo={
        'uri': 'mongodb://localhost:27017/',
    })
