# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SmartPlaylistContractsOperatorDto(object):
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
        'type': 'str',
        'default_value': 'SmartPlaylistDomainValuesValue'
    }

    attribute_map = {
        'name': 'Name',
        'type': 'Type',
        'default_value': 'DefaultValue'
    }

    def __init__(self, name=None, type=None, default_value=None):  # noqa: E501
        """SmartPlaylistContractsOperatorDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._default_value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if default_value is not None:
            self.default_value = default_value

    @property
    def name(self):
        """Gets the name of this SmartPlaylistContractsOperatorDto.  # noqa: E501


        :return: The name of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmartPlaylistContractsOperatorDto.


        :param name: The name of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SmartPlaylistContractsOperatorDto.  # noqa: E501


        :return: The type of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SmartPlaylistContractsOperatorDto.


        :param type: The type of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this SmartPlaylistContractsOperatorDto.  # noqa: E501


        :return: The default_value of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :rtype: SmartPlaylistDomainValuesValue
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this SmartPlaylistContractsOperatorDto.


        :param default_value: The default_value of this SmartPlaylistContractsOperatorDto.  # noqa: E501
        :type: SmartPlaylistDomainValuesValue
        """

        self._default_value = default_value

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
        if issubclass(SmartPlaylistContractsOperatorDto, dict):
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
        if not isinstance(other, SmartPlaylistContractsOperatorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
