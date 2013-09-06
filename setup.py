#!/usr/bin/env python
"""
memcached_rehasher
======

A pure python implementation of a consistent hasher for memcached.
Its missrate is similar to continuum, but it has O(1) per request
performane vs continiums O(lg(n)) per request performnace where n is
the number of servers in your memcached collecion.

"""

from setuptools import setup

setup(
    name='memcached_rehasher',
    version='0.0.0',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Rehasher',
    long_description=__doc__,
    py_modules = [
        "memcached_rehasher/__init__",
        ],
    packages = ["memcached_rehasher"],
    zip_safe=True,
    license='GPL',
    include_package_data=True,
    classifiers=[
        ],
    scripts = [
        ],
    url = "https://github.com/wnyc/memcached_rehasher",
    install_requires = [
        ]
)

