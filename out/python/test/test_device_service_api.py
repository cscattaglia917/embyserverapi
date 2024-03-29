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
from embyapi.api.device_service_api import DeviceServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestDeviceServiceApi(unittest.TestCase):
    """DeviceServiceApi unit test stubs"""

    def setUp(self):
        self.api = DeviceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_devices(self):
        """Test case for delete_devices

        Deletes a device  # noqa: E501
        """
        pass

    def test_get_devices(self):
        """Test case for get_devices

        Gets all devices  # noqa: E501
        """
        pass

    def test_get_devices_camerauploads(self):
        """Test case for get_devices_camerauploads

        Gets camera upload history for a device  # noqa: E501
        """
        pass

    def test_get_devices_info(self):
        """Test case for get_devices_info

        Gets info for a device  # noqa: E501
        """
        pass

    def test_get_devices_options(self):
        """Test case for get_devices_options

        Gets options for a device  # noqa: E501
        """
        pass

    def test_post_devices_camerauploads(self):
        """Test case for post_devices_camerauploads

        Uploads content  # noqa: E501
        """
        pass

    def test_post_devices_delete(self):
        """Test case for post_devices_delete

        Deletes a device  # noqa: E501
        """
        pass

    def test_post_devices_options(self):
        """Test case for post_devices_options

        Updates device options  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
