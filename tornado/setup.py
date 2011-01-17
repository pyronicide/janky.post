#
# Copyright (c) 2011 Thomas Rampelberg
#

"""
Make doing janky cross domain communication easy.
"""

__author__ = 'Thomas Rampelberg'
__author_email__ = 'thomas@saunter.org'

from setuptools import setup

setup(
    name = "janky_post",
    version = "0.1",
    author = __author__,
    author_email = __author_email__,
    description = "Makes janky cross-domain communication easy",
    install_requires = [ "pycurl", "tornado" ],
    py_modules = ['janky_post']
)
