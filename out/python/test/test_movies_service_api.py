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
from embyapi.api.movies_service_api import MoviesServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestMoviesServiceApi(unittest.TestCase):
    """MoviesServiceApi unit test stubs"""

    def setUp(self):
        self.api = MoviesServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_movies_recommendations(self):
        """Test case for get_movies_recommendations

        Gets movie recommendations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
