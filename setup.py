#!/usr/bin/env python
"""
memcache_rehasher
======

A pure python implementation of a consistent hasher for memcache.
Its missrate is similar to continuum, but it has O(1) per request
performane vs continiums O(lg(n)) per request performnace where n is
the number of servers in your memcache collecion.

"""

from setuptools import setup

setup(
    name='python_consistent_memcache',
    version='0.0.0',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='python-memcache with consistent hashing',
    long_description=__doc__,
    py_modules = [
        "consistent_memcache/__init__",
        ],
    packages = ["consistent_memcache"],
    zip_safe=True,
    license='GPL',
    include_package_data=True,
    classifiers=[
        ],
    scripts = [
        ],
    url = "https://github.com/wnyc/python_consistent_memcache",
    install_requires = [
        'python_memcache',
        ]
)

