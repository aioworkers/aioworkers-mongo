#!/usr/bin/env python
import pathlib

from setuptools import setup, find_packages

version = __import__('aioworkers_mongo').__version__

requirements = [
    'aioworkers>=0.8.0',
    'motor >=1.3, < 2.0',
]

test_requirements = [
    'pytest',
    'pytest-runner',
    'pytest-aioworkers',
    'pytest-flake8',
    'flake8-isort',
    'pyyaml',
    'aiohttp<4.0.0',
]

readme = pathlib.Path('README.rst').read_text()

setup(
    name='aioworkers-mongo',
    version=version,
    description='Module for working with Mongo DB',
    long_description=readme,
    author='Alexander Bogushov',
    author_email='abogushov@gmail.com',
    url='https://github.com/aioworkers/aioworkers-mongo',
    packages=[i for i in find_packages() if i.startswith('aioworkers_mongo')],
    include_package_data=True,
    install_requires=requirements,
    license='Apache Software License 2.0',
    keywords='aioworkers mongo motor',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
