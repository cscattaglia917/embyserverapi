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

class DlnaProfileCondition(object):
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
        'condition': 'DlnaProfileConditionType',
        '_property': 'DlnaProfileConditionValue',
        'value': 'str',
        'is_required': 'bool'
    }

    attribute_map = {
        'condition': 'Condition',
        '_property': 'Property',
        'value': 'Value',
        'is_required': 'IsRequired'
    }

    def __init__(self, condition=None, _property=None, value=None, is_required=None):  # noqa: E501
        """DlnaProfileCondition - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self.__property = None
        self._value = None
        self._is_required = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if _property is not None:
            self._property = _property
        if value is not None:
            self.value = value
        if is_required is not None:
            self.is_required = is_required

    @property
    def condition(self):
        """Gets the condition of this DlnaProfileCondition.  # noqa: E501


        :return: The condition of this DlnaProfileCondition.  # noqa: E501
        :rtype: DlnaProfileConditionType
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this DlnaProfileCondition.


        :param condition: The condition of this DlnaProfileCondition.  # noqa: E501
        :type: DlnaProfileConditionType
        """

        self._condition = condition

    @property
    def _property(self):
        """Gets the _property of this DlnaProfileCondition.  # noqa: E501


        :return: The _property of this DlnaProfileCondition.  # noqa: E501
        :rtype: DlnaProfileConditionValue
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this DlnaProfileCondition.


        :param _property: The _property of this DlnaProfileCondition.  # noqa: E501
        :type: DlnaProfileConditionValue
        """

        self.__property = _property

    @property
    def value(self):
        """Gets the value of this DlnaProfileCondition.  # noqa: E501


        :return: The value of this DlnaProfileCondition.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DlnaProfileCondition.


        :param value: The value of this DlnaProfileCondition.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def is_required(self):
        """Gets the is_required of this DlnaProfileCondition.  # noqa: E501


        :return: The is_required of this DlnaProfileCondition.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this DlnaProfileCondition.


        :param is_required: The is_required of this DlnaProfileCondition.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

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
        if issubclass(DlnaProfileCondition, dict):
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
        if not isinstance(other, DlnaProfileCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
