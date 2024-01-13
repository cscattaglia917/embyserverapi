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

class ThemeMediaResult(object):
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
        'owner_id': 'int',
        'items': 'list[BaseItemDto]',
        'total_record_count': 'int'
    }

    attribute_map = {
        'owner_id': 'OwnerId',
        'items': 'Items',
        'total_record_count': 'TotalRecordCount'
    }

    def __init__(self, owner_id=None, items=None, total_record_count=None):  # noqa: E501
        """ThemeMediaResult - a model defined in Swagger"""  # noqa: E501
        self._owner_id = None
        self._items = None
        self._total_record_count = None
        self.discriminator = None
        if owner_id is not None:
            self.owner_id = owner_id
        if items is not None:
            self.items = items
        if total_record_count is not None:
            self.total_record_count = total_record_count

    @property
    def owner_id(self):
        """Gets the owner_id of this ThemeMediaResult.  # noqa: E501


        :return: The owner_id of this ThemeMediaResult.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ThemeMediaResult.


        :param owner_id: The owner_id of this ThemeMediaResult.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def items(self):
        """Gets the items of this ThemeMediaResult.  # noqa: E501


        :return: The items of this ThemeMediaResult.  # noqa: E501
        :rtype: list[BaseItemDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ThemeMediaResult.


        :param items: The items of this ThemeMediaResult.  # noqa: E501
        :type: list[BaseItemDto]
        """

        self._items = items

    @property
    def total_record_count(self):
        """Gets the total_record_count of this ThemeMediaResult.  # noqa: E501


        :return: The total_record_count of this ThemeMediaResult.  # noqa: E501
        :rtype: int
        """
        return self._total_record_count

    @total_record_count.setter
    def total_record_count(self, total_record_count):
        """Sets the total_record_count of this ThemeMediaResult.


        :param total_record_count: The total_record_count of this ThemeMediaResult.  # noqa: E501
        :type: int
        """

        self._total_record_count = total_record_count

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
        if issubclass(ThemeMediaResult, dict):
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
        if not isinstance(other, ThemeMediaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
