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
from embyapi.api.scripter_xapi_api import ScripterXAPIApi  # noqa: E501
from embyapi.rest import ApiException


class TestScripterXAPIApi(unittest.TestCase):
    """ScripterXAPIApi unit test stubs"""

    def setUp(self):
        self.api = ScripterXAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_scripterx_packages_by_installationid_by_function(self):
        """Test case for delete_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_get_scripterx_changelog(self):
        """Test case for get_scripterx_changelog

        """
        pass

    def test_get_scripterx_packages_by_installationid_by_function(self):
        """Test case for get_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_get_scripterx_packages_getconfiginterface_by_installationid(self):
        """Test case for get_scripterx_packages_getconfiginterface_by_installationid

        """
        pass

    def test_get_scripterx_packages_info_by_installationid(self):
        """Test case for get_scripterx_packages_info_by_installationid

        Get Installed Package Information  # noqa: E501
        """
        pass

    def test_get_scripterx_packages_instances_by_packageid(self):
        """Test case for get_scripterx_packages_instances_by_packageid

        Get a list of Installed Packages with PackageId  # noqa: E501
        """
        pass

    def test_get_scripterx_packages_reload_by_installationid(self):
        """Test case for get_scripterx_packages_reload_by_installationid

        """
        pass

    def test_get_scripterx_packages_remove_by_installationid(self):
        """Test case for get_scripterx_packages_remove_by_installationid

        """
        pass

    def test_head_scripterx_packages_by_installationid_by_function(self):
        """Test case for head_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_options_scripterx_packages_by_installationid_by_function(self):
        """Test case for options_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_patch_scripterx_packages_by_installationid_by_function(self):
        """Test case for patch_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_post_scripterx_packages_by_installationid_by_function(self):
        """Test case for post_scripterx_packages_by_installationid_by_function

        """
        pass

    def test_post_scripterx_packages_saveconfig_by_installationid(self):
        """Test case for post_scripterx_packages_saveconfig_by_installationid

        Save Package Configuration  # noqa: E501
        """
        pass

    def test_post_scripterx_packages_upload(self):
        """Test case for post_scripterx_packages_upload

        Upload ZIP Package to ScripterX  # noqa: E501
        """
        pass

    def test_put_scripterx_packages_by_installationid_by_function(self):
        """Test case for put_scripterx_packages_by_installationid_by_function

        """
        pass


if __name__ == '__main__':
    unittest.main()
