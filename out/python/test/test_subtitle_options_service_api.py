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
from embyapi.api.subtitle_options_service_api import SubtitleOptionsServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestSubtitleOptionsServiceApi(unittest.TestCase):
    """SubtitleOptionsServiceApi unit test stubs"""

    def setUp(self):
        self.api = SubtitleOptionsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_encoding_subtitleoptions(self):
        """Test case for get_encoding_subtitleoptions

        Gets the subtitle options  # noqa: E501
        """
        pass

    def test_post_encoding_subtitleoptions(self):
        """Test case for post_encoding_subtitleoptions

        Updates the subtitle options  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()