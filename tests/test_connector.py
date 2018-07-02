from aioworkers.core.context import Context

from aioworkers_mongo.base import Connector


async def test_connect(loop, config):
    context = Context({}, loop=loop)
    mongo = Connector(config, context=context, loop=loop)
    await mongo.init()
    assert await mongo.list_database_names()
