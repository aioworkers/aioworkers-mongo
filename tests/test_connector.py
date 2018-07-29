
async def test_connect(context):
    assert await context.mongo.list_database_names()
