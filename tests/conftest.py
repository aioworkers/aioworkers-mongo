import pytest
from aioworkers.core.config import MergeDict


@pytest.fixture
def config():
    return MergeDict({
        'uri': 'mongodb://localhost:27017/',
    })
