from datetime import datetime


async def run(worker, *args, **kwargs):
    worker.logger.info("OK")
    await worker.context.mongo.test.log.insert_one(
        {
            "created_at": datetime.utcnow(),
        }
    )
