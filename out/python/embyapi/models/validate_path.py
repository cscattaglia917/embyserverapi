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

class ValidatePath(object):
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
        'validate_writeable': 'bool',
        'is_file': 'bool'
    }

    attribute_map = {
        'validate_writeable': 'ValidateWriteable',
        'is_file': 'IsFile'
    }

    def __init__(self, validate_writeable=None, is_file=None):  # noqa: E501
        """ValidatePath - a model defined in Swagger"""  # noqa: E501
        self._validate_writeable = None
        self._is_file = None
        self.discriminator = None
        if validate_writeable is not None:
            self.validate_writeable = validate_writeable
        if is_file is not None:
            self.is_file = is_file

    @property
    def validate_writeable(self):
        """Gets the validate_writeable of this ValidatePath.  # noqa: E501


        :return: The validate_writeable of this ValidatePath.  # noqa: E501
        :rtype: bool
        """
        return self._validate_writeable

    @validate_writeable.setter
    def validate_writeable(self, validate_writeable):
        """Sets the validate_writeable of this ValidatePath.


        :param validate_writeable: The validate_writeable of this ValidatePath.  # noqa: E501
        :type: bool
        """

        self._validate_writeable = validate_writeable

    @property
    def is_file(self):
        """Gets the is_file of this ValidatePath.  # noqa: E501


        :return: The is_file of this ValidatePath.  # noqa: E501
        :rtype: bool
        """
        return self._is_file

    @is_file.setter
    def is_file(self, is_file):
        """Sets the is_file of this ValidatePath.


        :param is_file: The is_file of this ValidatePath.  # noqa: E501
        :type: bool
        """

        self._is_file = is_file

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
        if issubclass(ValidatePath, dict):
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
        if not isinstance(other, ValidatePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
