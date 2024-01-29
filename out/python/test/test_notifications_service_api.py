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
from embyapi.api.notifications_service_api import NotificationsServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestNotificationsServiceApi(unittest.TestCase):
    """NotificationsServiceApi unit test stubs"""

    def setUp(self):
        self.api = NotificationsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_notifications_by_userid(self):
        """Test case for get_notifications_by_userid

        Gets notifications  # noqa: E501
        """
        pass

    def test_get_notifications_by_userid_summary(self):
        """Test case for get_notifications_by_userid_summary

        Gets a notification summary for a user  # noqa: E501
        """
        pass

    def test_get_notifications_services(self):
        """Test case for get_notifications_services

        Gets notification types  # noqa: E501
        """
        pass

    def test_get_notifications_types(self):
        """Test case for get_notifications_types

        Gets notification types  # noqa: E501
        """
        pass

    def test_post_notifications_admin(self):
        """Test case for post_notifications_admin

        Sends a notification to all admin users  # noqa: E501
        """
        pass

    def test_post_notifications_by_userid_read(self):
        """Test case for post_notifications_by_userid_read

        Marks notifications as read  # noqa: E501
        """
        pass

    def test_post_notifications_by_userid_unread(self):
        """Test case for post_notifications_by_userid_unread

        Marks notifications as unread  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
