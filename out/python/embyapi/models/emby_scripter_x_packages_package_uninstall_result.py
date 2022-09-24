# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EmbyScripterXPackagesPackageUninstallResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uninstall_result': 'str',
        'installation_id': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'uninstall_result': 'uninstallResult',
        'installation_id': 'installationId',
        'error_message': 'errorMessage'
    }

    def __init__(self, uninstall_result=None, installation_id=None, error_message=None):  # noqa: E501
        """EmbyScripterXPackagesPackageUninstallResult - a model defined in Swagger"""  # noqa: E501
        self._uninstall_result = None
        self._installation_id = None
        self._error_message = None
        self.discriminator = None
        if uninstall_result is not None:
            self.uninstall_result = uninstall_result
        if installation_id is not None:
            self.installation_id = installation_id
        if error_message is not None:
            self.error_message = error_message

    @property
    def uninstall_result(self):
        """Gets the uninstall_result of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501


        :return: The uninstall_result of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :rtype: str
        """
        return self._uninstall_result

    @uninstall_result.setter
    def uninstall_result(self, uninstall_result):
        """Sets the uninstall_result of this EmbyScripterXPackagesPackageUninstallResult.


        :param uninstall_result: The uninstall_result of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "Failed"]  # noqa: E501
        if uninstall_result not in allowed_values:
            raise ValueError(
                "Invalid value for `uninstall_result` ({0}), must be one of {1}"  # noqa: E501
                .format(uninstall_result, allowed_values)
            )

        self._uninstall_result = uninstall_result

    @property
    def installation_id(self):
        """Gets the installation_id of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501


        :return: The installation_id of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :rtype: str
        """
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id):
        """Sets the installation_id of this EmbyScripterXPackagesPackageUninstallResult.


        :param installation_id: The installation_id of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :type: str
        """

        self._installation_id = installation_id

    @property
    def error_message(self):
        """Gets the error_message of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501


        :return: The error_message of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this EmbyScripterXPackagesPackageUninstallResult.


        :param error_message: The error_message of this EmbyScripterXPackagesPackageUninstallResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EmbyScripterXPackagesPackageUninstallResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmbyScripterXPackagesPackageUninstallResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
