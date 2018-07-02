#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'aioworkers>=0.8.0',
    'motor==1.2.2',
]

test_requirements = [
    'pytest',
    'pytest-aiohttp',
]

setup(
    name='aioworkers-mongo',
    version='0.0.1',
    description='Module for working with Mongo DB',
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
