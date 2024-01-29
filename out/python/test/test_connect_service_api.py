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
from embyapi.api.connect_service_api import ConnectServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestConnectServiceApi(unittest.TestCase):
    """ConnectServiceApi unit test stubs"""

    def setUp(self):
        self.api = ConnectServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_by_id_connect_link(self):
        """Test case for delete_users_by_id_connect_link

        Removes a Connect link for a user  # noqa: E501
        """
        pass

    def test_get_connect_exchange(self):
        """Test case for get_connect_exchange

        Gets the corresponding local user from a connect user id  # noqa: E501
        """
        pass

    def test_get_connect_pending(self):
        """Test case for get_connect_pending

        Creates a Connect link for a user  # noqa: E501
        """
        pass

    def test_post_users_by_id_connect_link(self):
        """Test case for post_users_by_id_connect_link

        Creates a Connect link for a user  # noqa: E501
        """
        pass

    def test_post_users_by_id_connect_link_delete(self):
        """Test case for post_users_by_id_connect_link_delete

        Removes a Connect link for a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
