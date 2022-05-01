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
from embyapi.api.image_by_name_service_api import ImageByNameServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestImageByNameServiceApi(unittest.TestCase):
    """ImageByNameServiceApi unit test stubs"""

    def setUp(self):
        self.api = ImageByNameServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_images_general(self):
        """Test case for get_images_general

        Gets all general images by name  # noqa: E501
        """
        pass

    def test_get_images_general_by_name_by_type(self):
        """Test case for get_images_general_by_name_by_type

        Gets a general image by name  # noqa: E501
        """
        pass

    def test_get_images_mediainfo(self):
        """Test case for get_images_mediainfo

        Gets all media info image by name  # noqa: E501
        """
        pass

    def test_get_images_mediainfo_by_theme_by_name(self):
        """Test case for get_images_mediainfo_by_theme_by_name

        Gets a media info image by name  # noqa: E501
        """
        pass

    def test_get_images_ratings(self):
        """Test case for get_images_ratings

        Gets all rating images by name  # noqa: E501
        """
        pass

    def test_get_images_ratings_by_theme_by_name(self):
        """Test case for get_images_ratings_by_theme_by_name

        Gets a rating image by name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()