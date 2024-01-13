# coding: utf-8

"""
    Emby REST API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LibraryLibraryOptionInfo(object):
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
        'name': 'str',
        'default_enabled': 'bool',
        'features': 'list[ConfigurationMetadataFeatures]'
    }

    attribute_map = {
        'name': 'Name',
        'default_enabled': 'DefaultEnabled',
        'features': 'Features'
    }

    def __init__(self, name=None, default_enabled=None, features=None):  # noqa: E501
        """LibraryLibraryOptionInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._default_enabled = None
        self._features = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if default_enabled is not None:
            self.default_enabled = default_enabled
        if features is not None:
            self.features = features

    @property
    def name(self):
        """Gets the name of this LibraryLibraryOptionInfo.  # noqa: E501


        :return: The name of this LibraryLibraryOptionInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LibraryLibraryOptionInfo.


        :param name: The name of this LibraryLibraryOptionInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def default_enabled(self):
        """Gets the default_enabled of this LibraryLibraryOptionInfo.  # noqa: E501


        :return: The default_enabled of this LibraryLibraryOptionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._default_enabled

    @default_enabled.setter
    def default_enabled(self, default_enabled):
        """Sets the default_enabled of this LibraryLibraryOptionInfo.


        :param default_enabled: The default_enabled of this LibraryLibraryOptionInfo.  # noqa: E501
        :type: bool
        """

        self._default_enabled = default_enabled

    @property
    def features(self):
        """Gets the features of this LibraryLibraryOptionInfo.  # noqa: E501


        :return: The features of this LibraryLibraryOptionInfo.  # noqa: E501
        :rtype: list[ConfigurationMetadataFeatures]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this LibraryLibraryOptionInfo.


        :param features: The features of this LibraryLibraryOptionInfo.  # noqa: E501
        :type: list[ConfigurationMetadataFeatures]
        """

        self._features = features

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
        if issubclass(LibraryLibraryOptionInfo, dict):
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
        if not isinstance(other, LibraryLibraryOptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
