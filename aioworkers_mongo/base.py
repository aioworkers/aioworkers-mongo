import logging

from aioworkers.core.base import AbstractConnector
from motor.motor_asyncio import AsyncIOMotorClient

logger = logging.getLogger("aioworkers_mongo")


class Connector(AbstractConnector):
    default_mongo_uri = "mongodb://localhost:27017/"

    # List of methods that will be bind to connector from AsyncIOMotorClient
    __bind_methods = (
        "list_databases",
        "list_database_names",
        "server_info",
        "start_session",
        "end_session",
        "drop_database",
        "get_database",
        "close",
    )

    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)
        self._client = None

    async def init(self):
        await super().init()
        uri = self.config.get("uri", self.default_mongo_uri)
        self._client = AsyncIOMotorClient(uri)
        for method_name in self.__bind_methods:
            f = getattr(self._client, method_name)
            if f:
                setattr(self, method_name, f)

    async def connect(self):
        pass

    async def disconnect(self):
        self._client.close()

    def __getattr__(self, item):
        return self._client[item]

    def __getitem__(self, item):
        return self._client[item]
