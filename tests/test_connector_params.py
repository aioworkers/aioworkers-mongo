import pytest


@pytest.fixture
def config_yaml():
    return """
    mongo:
      cls: aioworkers_mongo.base.Connector
      client:
        host: localhost
        port: 27017
    """


async def test_connector(context, db_name):
    await context.mongo[db_name].test.insert_one({"test": "test"})
