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
from embyapi.api.playstate_service_api import PlaystateServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestPlaystateServiceApi(unittest.TestCase):
    """PlaystateServiceApi unit test stubs"""

    def setUp(self):
        self.api = PlaystateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_by_userid_playeditems_by_id(self):
        """Test case for delete_users_by_userid_playeditems_by_id

        Marks an item as unplayed  # noqa: E501
        """
        pass

    def test_delete_users_by_userid_playingitems_by_id(self):
        """Test case for delete_users_by_userid_playingitems_by_id

        Reports that a user has stopped playing an item  # noqa: E501
        """
        pass

    def test_post_sessions_playing(self):
        """Test case for post_sessions_playing

        Reports playback has started within a session  # noqa: E501
        """
        pass

    def test_post_sessions_playing_ping(self):
        """Test case for post_sessions_playing_ping

        Pings a playback session  # noqa: E501
        """
        pass

    def test_post_sessions_playing_progress(self):
        """Test case for post_sessions_playing_progress

        Reports playback progress within a session  # noqa: E501
        """
        pass

    def test_post_sessions_playing_stopped(self):
        """Test case for post_sessions_playing_stopped

        Reports playback has stopped within a session  # noqa: E501
        """
        pass

    def test_post_users_by_userid_playeditems_by_id(self):
        """Test case for post_users_by_userid_playeditems_by_id

        Marks an item as played  # noqa: E501
        """
        pass

    def test_post_users_by_userid_playingitems_by_id(self):
        """Test case for post_users_by_userid_playingitems_by_id

        Reports that a user has begun playing an item  # noqa: E501
        """
        pass

    def test_post_users_by_userid_playingitems_by_id_progress(self):
        """Test case for post_users_by_userid_playingitems_by_id_progress

        Reports a user's playback progress  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()