# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import embyapi
from embyapi.api.playlist_log_service_api import PlaylistLogServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestPlaylistLogServiceApi(unittest.TestCase):
    """PlaylistLogServiceApi unit test stubs"""

    def setUp(self):
        self.api = PlaylistLogServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_smartplaylist_log_by_id(self):
        """Test case for get_smartplaylist_log_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
