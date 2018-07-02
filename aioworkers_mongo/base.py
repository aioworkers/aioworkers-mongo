import logging

from aioworkers.core.base import AbstractEntity
from motor.motor_asyncio import AsyncIOMotorClient

logger = logging.getLogger('aioworkers_mongo')


class Connector(AbstractEntity):

    async def init(self):
        await super().init()
        uri = self.config.get('uri', 'mongodb://localhost:27017/')
        self._client = AsyncIOMotorClient(uri)
        self.list_database_names = self._client.list_database_names

    def __getattr__(self, item):
        return self._client[item]

    def __getitem__(self, item):
        return self._client[item]
