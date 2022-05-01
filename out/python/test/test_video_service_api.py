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
from embyapi.api.video_service_api import VideoServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestVideoServiceApi(unittest.TestCase):
    """VideoServiceApi unit test stubs"""

    def setUp(self):
        self.api = VideoServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_items_file(self):
        """Test case for get_items_file

        Gets the original file of an item  # noqa: E501
        """
        pass

    def test_get_videos_by_id_by_container(self):
        """Test case for get_videos_by_id_by_container

        Gets a video stream  # noqa: E501
        """
        pass

    def test_get_videos_by_id_stream(self):
        """Test case for get_videos_by_id_stream

        Gets a video stream  # noqa: E501
        """
        pass

    def test_head_videos_by_id_by_container(self):
        """Test case for head_videos_by_id_by_container

        Gets a video stream  # noqa: E501
        """
        pass

    def test_head_videos_by_id_stream(self):
        """Test case for head_videos_by_id_stream

        Gets a video stream  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
