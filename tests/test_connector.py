
async def test_bind_methods(context, db_name):
    assert await context.mongo.server_info()

    db = context.mongo.get_database(db_name)
    await db.test.insert_one({'test': 'test'})
    assert db_name in (await context.mongo.list_database_names())

    await context.mongo.drop_database(db)

    assert db_name not in (await context.mongo.list_database_names())

    context.mongo.close()
