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
from embyapi.api.configuration_service_api import ConfigurationServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestConfigurationServiceApi(unittest.TestCase):
    """ConfigurationServiceApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_configuration(self):
        """Test case for get_system_configuration

        Gets application configuration  # noqa: E501
        """
        pass

    def test_get_system_configuration_by_key(self):
        """Test case for get_system_configuration_by_key

        Gets a named configuration  # noqa: E501
        """
        pass

    def test_post_system_configuration(self):
        """Test case for post_system_configuration

        Updates application configuration  # noqa: E501
        """
        pass

    def test_post_system_configuration_by_key(self):
        """Test case for post_system_configuration_by_key

        Updates named configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
