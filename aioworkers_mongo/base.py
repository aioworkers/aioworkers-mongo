import logging

from aioworkers.core.base import AbstractConnector
from aioworkers.core.config import ValueExtractor
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
        self._client_config = None

    def set_config(self, config: ValueExtractor) -> None:
        cfg = config.new_parent(logger=__package__)
        super().set_config(cfg)

        client_config = dict(self.config.get("client", {}))
        if client_config:
            self._client_config = client_config
            return

        # Support old uri only config.
        self._client_config = {
            "host": self.config.get("uri", self.default_mongo_uri),
        }

    async def connect(self):
        if self._client is None:
            self._client = AsyncIOMotorClient(**self._client_config)
            for method_name in self.__bind_methods:
                f = getattr(self._client, method_name)
                if f:
                    setattr(self, method_name, f)

    async def disconnect(self):
        self._client.close()

    def __getattr__(self, item):
        return self._client[item]

    def __getitem__(self, item):
        return self._client[item]
