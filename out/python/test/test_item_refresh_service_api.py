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
from embyapi.api.item_refresh_service_api import ItemRefreshServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestItemRefreshServiceApi(unittest.TestCase):
    """ItemRefreshServiceApi unit test stubs"""

    def setUp(self):
        self.api = ItemRefreshServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_items_by_id_refresh(self):
        """Test case for post_items_by_id_refresh

        Refreshes metadata for an item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()