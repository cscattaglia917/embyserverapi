# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LibraryRemoveVirtualFolder(object):
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
        'id': 'str',
        'refresh_library': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'refresh_library': 'RefreshLibrary'
    }

    def __init__(self, id=None, refresh_library=None):  # noqa: E501
        """LibraryRemoveVirtualFolder - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._refresh_library = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if refresh_library is not None:
            self.refresh_library = refresh_library

    @property
    def id(self):
        """Gets the id of this LibraryRemoveVirtualFolder.  # noqa: E501


        :return: The id of this LibraryRemoveVirtualFolder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibraryRemoveVirtualFolder.


        :param id: The id of this LibraryRemoveVirtualFolder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def refresh_library(self):
        """Gets the refresh_library of this LibraryRemoveVirtualFolder.  # noqa: E501


        :return: The refresh_library of this LibraryRemoveVirtualFolder.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_library

    @refresh_library.setter
    def refresh_library(self, refresh_library):
        """Sets the refresh_library of this LibraryRemoveVirtualFolder.


        :param refresh_library: The refresh_library of this LibraryRemoveVirtualFolder.  # noqa: E501
        :type: bool
        """

        self._refresh_library = refresh_library

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
        if issubclass(LibraryRemoveVirtualFolder, dict):
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
        if not isinstance(other, LibraryRemoveVirtualFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
