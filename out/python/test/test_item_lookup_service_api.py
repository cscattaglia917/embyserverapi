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
from embyapi.api.item_lookup_service_api import ItemLookupServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestItemLookupServiceApi(unittest.TestCase):
    """ItemLookupServiceApi unit test stubs"""

    def setUp(self):
        self.api = ItemLookupServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_items_by_id_externalidinfos(self):
        """Test case for get_items_by_id_externalidinfos

        Gets external id infos for an item  # noqa: E501
        """
        pass

    def test_get_items_remotesearch_image(self):
        """Test case for get_items_remotesearch_image

        Gets a remote image  # noqa: E501
        """
        pass

    def test_post_items_remotesearch_apply_by_id(self):
        """Test case for post_items_remotesearch_apply_by_id

        Applies search criteria to an item and refreshes metadata  # noqa: E501
        """
        pass

    def test_post_items_remotesearch_book(self):
        """Test case for post_items_remotesearch_book

        """
        pass

    def test_post_items_remotesearch_boxset(self):
        """Test case for post_items_remotesearch_boxset

        """
        pass

    def test_post_items_remotesearch_game(self):
        """Test case for post_items_remotesearch_game

        """
        pass

    def test_post_items_remotesearch_movie(self):
        """Test case for post_items_remotesearch_movie

        """
        pass

    def test_post_items_remotesearch_musicalbum(self):
        """Test case for post_items_remotesearch_musicalbum

        """
        pass

    def test_post_items_remotesearch_musicartist(self):
        """Test case for post_items_remotesearch_musicartist

        """
        pass

    def test_post_items_remotesearch_musicvideo(self):
        """Test case for post_items_remotesearch_musicvideo

        """
        pass

    def test_post_items_remotesearch_person(self):
        """Test case for post_items_remotesearch_person

        """
        pass

    def test_post_items_remotesearch_series(self):
        """Test case for post_items_remotesearch_series

        """
        pass

    def test_post_items_remotesearch_trailer(self):
        """Test case for post_items_remotesearch_trailer

        """
        pass


if __name__ == '__main__':
    unittest.main()