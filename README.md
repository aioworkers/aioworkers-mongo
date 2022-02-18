# aioworkers-mongo


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/aioworkers/aioworkers-mongo/CI)](https://github.com/aioworkers/aioworkers-mongo/actions?query=workflow%3ACI)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aioworkers-mongo)](https://pypi.org/project/aioworkers-mongo)
[![PyPI](https://img.shields.io/pypi/v/aioworkers-mongo)](https://pypi.org/project/aioworkers-mongo)

Mongo plugin for `aioworkers`.


## Usage

### Connection

Add this to aioworkers config.yaml:

```yaml
mongo:
  cls: aioworkers_mongo.base.Connector
  uri: 'mongodb://localhost:27017/'
```

You can get access to mongo anywhere via context:

```python
docs = [doc async for doc in context.mongo.db.collection.find({})]
```

### Extended client config

```yaml
mongo:
  cls: aioworkers_mongo.base.Connector
  client:
    host: 'localhost'
    port: 27017
```


## Development

Run Mongo DB:

```shell
docker run --rm -p 27017:27017 --name mongo -d mongo
```

Install dev requirements:

```shell
poetry install
```

Activate env:

```shell
. .venv/bin/activate
```


Run tests:

```shell
pytest
```
