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
from embyapi.api.media_info_service_api import MediaInfoServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestMediaInfoServiceApi(unittest.TestCase):
    """MediaInfoServiceApi unit test stubs"""

    def setUp(self):
        self.api = MediaInfoServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_items_by_id_playbackinfo(self):
        """Test case for get_items_by_id_playbackinfo

        Gets live playback media info for an item  # noqa: E501
        """
        pass

    def test_get_playback_bitratetest(self):
        """Test case for get_playback_bitratetest

        """
        pass

    def test_post_items_by_id_playbackinfo(self):
        """Test case for post_items_by_id_playbackinfo

        Gets live playback media info for an item  # noqa: E501
        """
        pass

    def test_post_livestreams_close(self):
        """Test case for post_livestreams_close

        Closes a media source  # noqa: E501
        """
        pass

    def test_post_livestreams_mediainfo(self):
        """Test case for post_livestreams_mediainfo

        Closes a media source  # noqa: E501
        """
        pass

    def test_post_livestreams_open(self):
        """Test case for post_livestreams_open

        Opens a media source  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
