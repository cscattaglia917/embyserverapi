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
from embyapi.api.dashboard_service_api import DashboardServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestDashboardServiceApi(unittest.TestCase):
    """DashboardServiceApi unit test stubs"""

    def setUp(self):
        self.api = DashboardServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_web_configurationpage(self):
        """Test case for get_web_configurationpage

        """
        pass

    def test_get_web_configurationpages(self):
        """Test case for get_web_configurationpages

        """
        pass

    def test_get_web_strings(self):
        """Test case for get_web_strings

        """
        pass


if __name__ == '__main__':
    unittest.main()
