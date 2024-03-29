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
from embyapi.api.playlist_service_api import PlaylistServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestPlaylistServiceApi(unittest.TestCase):
    """PlaylistServiceApi unit test stubs"""

    def setUp(self):
        self.api = PlaylistServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_playlists_by_id_items(self):
        """Test case for delete_playlists_by_id_items

        Removes items from a playlist  # noqa: E501
        """
        pass

    def test_get_playlists_by_id_items(self):
        """Test case for get_playlists_by_id_items

        Gets the original items of a playlist  # noqa: E501
        """
        pass

    def test_post_playlists(self):
        """Test case for post_playlists

        Creates a new playlist  # noqa: E501
        """
        pass

    def test_post_playlists_by_id_items(self):
        """Test case for post_playlists_by_id_items

        Adds items to a playlist  # noqa: E501
        """
        pass

    def test_post_playlists_by_id_items_by_itemid_move_by_newindex(self):
        """Test case for post_playlists_by_id_items_by_itemid_move_by_newindex

        Moves a playlist item  # noqa: E501
        """
        pass

    def test_post_playlists_by_id_items_delete(self):
        """Test case for post_playlists_by_id_items_delete

        Removes items from a playlist  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
