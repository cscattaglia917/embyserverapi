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
from embyapi.api.video_hls_service_api import VideoHlsServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestVideoHlsServiceApi(unittest.TestCase):
    """VideoHlsServiceApi unit test stubs"""

    def setUp(self):
        self.api = VideoHlsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(self):
        """Test case for get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer

        """
        pass

    def test_get_videos_by_id_live_m3u8(self):
        """Test case for get_videos_by_id_live_m3u8

        """
        pass


if __name__ == '__main__':
    unittest.main()
