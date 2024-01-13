# coding: utf-8

"""
    Emby REST API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path

CWD = Path(__file__).parent
long_description = (CWD / "README.md").read_text()

NAME = "EmbyServerAPI"
VERSION = "3.2.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Emby REST API",
    author_email="",
    url="",
    keywords=["Swagger", "Emby REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
