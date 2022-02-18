import pytest


@pytest.fixture
def db_name():
    return "test"


@pytest.fixture
def config_yaml():
    return """
    mongo:
      cls: aioworkers_mongo.base.Connector
      uri: mongodb://localhost:27017/
    """
