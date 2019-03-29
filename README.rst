aioworkers-mongo
================

.. image:: https://travis-ci.org/aioworkers/aioworkers-mongo.svg?branch=master
    :target: https://travis-ci.org/aioworkers/aioworkers-mongo

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-mongo.svg
  :target: https://pypi.python.org/pypi/aioworkers-mongo
  :alt: Python versions

.. image:: https://img.shields.io/pypi/v/aioworkers-mongo.svg
  :target: https://pypi.org/project/aioworkers-mongo


Mongo plugin for `aioworkers`.


Add this to aioworkers config.yaml:

.. code-block:: yaml

    mongo:
        cls: aioworkers_mongo.base.Connector
        uri: 'mongodb://localhost:27017/'

You can get access to mongo anywhere via context:

.. code-block:: python

    docs = [doc async for doc in context.mongo.db.collection.find({})]


Development
-----------

Install dev requirements:


.. code-block:: shell

    pipenv install --dev --skip-lock


Run tests:

.. code-block:: shell

    pytest
