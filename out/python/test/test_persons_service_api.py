# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import embyapi
from embyapi.api.persons_service_api import PersonsServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestPersonsServiceApi(unittest.TestCase):
    """PersonsServiceApi unit test stubs"""

    def setUp(self):
        self.api = PersonsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_persons(self):
        """Test case for get_persons

        Gets all persons from a given item, folder, or the entire library  # noqa: E501
        """
        pass

    def test_get_persons_by_name(self):
        """Test case for get_persons_by_name

        Gets a person, by name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
