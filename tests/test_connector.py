async def test_bind_methods(context, db_name):
    assert await context.mongo.server_info()

    db = context.mongo.get_database(db_name)
    await db.test.insert_one({"test": "test"})
    assert db_name in (await context.mongo.list_database_names())

    await context.mongo.drop_database(db)

    assert db_name not in (await context.mongo.list_database_names())

    context.mongo.close()


async def test_close_connector(loop):
    from aioworkers.core.config import Config
    from aioworkers.core.context import Context

    c = Config()
    c.update(
        {
            "mongo": {
                "cls": "aioworkers_mongo.base.Connector",
                "uri": "mongodb://localhost:27017/",
            }
        }
    )

    async with Context(c, loop=loop) as ctx:
        assert ctx.mongo._client

    # Check that client has been stopped.
    # TODO Find better way to check that MongoClient has been closed.
    assert not ctx.mongo._client.delegate._topology._opened
