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
from embyapi.api.user_library_service_api import UserLibraryServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestUserLibraryServiceApi(unittest.TestCase):
    """UserLibraryServiceApi unit test stubs"""

    def setUp(self):
        self.api = UserLibraryServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_by_userid_favoriteitems_by_id(self):
        """Test case for delete_users_by_userid_favoriteitems_by_id

        Unmarks an item as a favorite  # noqa: E501
        """
        pass

    def test_delete_users_by_userid_items_by_id_rating(self):
        """Test case for delete_users_by_userid_items_by_id_rating

        Deletes a user's saved personal rating for an item  # noqa: E501
        """
        pass

    def test_get_livetv_programs_by_id(self):
        """Test case for get_livetv_programs_by_id

        Gets a live tv program  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_by_id(self):
        """Test case for get_users_by_userid_items_by_id

        Gets an item from a user's library  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_by_id_intros(self):
        """Test case for get_users_by_userid_items_by_id_intros

        Gets intros to play before the main media item plays  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_by_id_localtrailers(self):
        """Test case for get_users_by_userid_items_by_id_localtrailers

        Gets local trailers for an item  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_by_id_specialfeatures(self):
        """Test case for get_users_by_userid_items_by_id_specialfeatures

        Gets special features for an item  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_latest(self):
        """Test case for get_users_by_userid_items_latest

        Gets latest media  # noqa: E501
        """
        pass

    def test_get_users_by_userid_items_root(self):
        """Test case for get_users_by_userid_items_root

        Gets the root folder from a user's library  # noqa: E501
        """
        pass

    def test_get_videos_by_id_additionalparts(self):
        """Test case for get_videos_by_id_additionalparts

        Gets additional parts for a video.  # noqa: E501
        """
        pass

    def test_post_users_by_userid_favoriteitems_by_id(self):
        """Test case for post_users_by_userid_favoriteitems_by_id

        Marks an item as a favorite  # noqa: E501
        """
        pass

    def test_post_users_by_userid_favoriteitems_by_id_delete(self):
        """Test case for post_users_by_userid_favoriteitems_by_id_delete

        Unmarks an item as a favorite  # noqa: E501
        """
        pass

    def test_post_users_by_userid_items_by_id_hidefromresume(self):
        """Test case for post_users_by_userid_items_by_id_hidefromresume

        Updates a user's hide from resume for an item  # noqa: E501
        """
        pass

    def test_post_users_by_userid_items_by_id_rating(self):
        """Test case for post_users_by_userid_items_by_id_rating

        Updates a user's rating for an item  # noqa: E501
        """
        pass

    def test_post_users_by_userid_items_by_id_rating_delete(self):
        """Test case for post_users_by_userid_items_by_id_rating_delete

        Deletes a user's saved personal rating for an item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
