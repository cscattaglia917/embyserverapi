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

class SmartPlaylistContractsSmartPlaylistNewItemOrderDto(object):
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
        'has_sort': 'bool',
        'order_by': 'str'
    }

    attribute_map = {
        'has_sort': 'HasSort',
        'order_by': 'OrderBy'
    }

    def __init__(self, has_sort=None, order_by=None):  # noqa: E501
        """SmartPlaylistContractsSmartPlaylistNewItemOrderDto - a model defined in Swagger"""  # noqa: E501
        self._has_sort = None
        self._order_by = None
        self.discriminator = None
        if has_sort is not None:
            self.has_sort = has_sort
        if order_by is not None:
            self.order_by = order_by

    @property
    def has_sort(self):
        """Gets the has_sort of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501


        :return: The has_sort of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_sort

    @has_sort.setter
    def has_sort(self, has_sort):
        """Sets the has_sort of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.


        :param has_sort: The has_sort of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501
        :type: bool
        """

        self._has_sort = has_sort

    @property
    def order_by(self):
        """Gets the order_by of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501


        :return: The order_by of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.


        :param order_by: The order_by of this SmartPlaylistContractsSmartPlaylistNewItemOrderDto.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

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
        if issubclass(SmartPlaylistContractsSmartPlaylistNewItemOrderDto, dict):
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
        if not isinstance(other, SmartPlaylistContractsSmartPlaylistNewItemOrderDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
