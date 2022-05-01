# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import embyapi
from embyapi.api.dlna_service_api import DlnaServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestDlnaServiceApi(unittest.TestCase):
    """DlnaServiceApi unit test stubs"""

    def setUp(self):
        self.api = DlnaServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_dlna_profiles_by_id(self):
        """Test case for delete_dlna_profiles_by_id

        Deletes a profile  # noqa: E501
        """
        pass

    def test_get_dlna_profileinfos(self):
        """Test case for get_dlna_profileinfos

        Gets a list of profiles  # noqa: E501
        """
        pass

    def test_get_dlna_profiles_by_id(self):
        """Test case for get_dlna_profiles_by_id

        Gets a single profile  # noqa: E501
        """
        pass

    def test_get_dlna_profiles_default(self):
        """Test case for get_dlna_profiles_default

        Gets the default profile  # noqa: E501
        """
        pass

    def test_post_dlna_profiles(self):
        """Test case for post_dlna_profiles

        Creates a profile  # noqa: E501
        """
        pass

    def test_post_dlna_profiles_by_id(self):
        """Test case for post_dlna_profiles_by_id

        Updates a profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()