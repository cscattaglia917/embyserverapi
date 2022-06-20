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

class GlobalizationCountryInfo(object):
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
        'display_name': 'str',
        'english_name': 'str',
        'two_letter_iso_region_name': 'str',
        'three_letter_iso_region_name': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'display_name': 'DisplayName',
        'english_name': 'EnglishName',
        'two_letter_iso_region_name': 'TwoLetterISORegionName',
        'three_letter_iso_region_name': 'ThreeLetterISORegionName'
    }

    def __init__(self, name=None, display_name=None, english_name=None, two_letter_iso_region_name=None, three_letter_iso_region_name=None):  # noqa: E501
        """GlobalizationCountryInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._display_name = None
        self._english_name = None
        self._two_letter_iso_region_name = None
        self._three_letter_iso_region_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if english_name is not None:
            self.english_name = english_name
        if two_letter_iso_region_name is not None:
            self.two_letter_iso_region_name = two_letter_iso_region_name
        if three_letter_iso_region_name is not None:
            self.three_letter_iso_region_name = three_letter_iso_region_name

    @property
    def name(self):
        """Gets the name of this GlobalizationCountryInfo.  # noqa: E501


        :return: The name of this GlobalizationCountryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalizationCountryInfo.


        :param name: The name of this GlobalizationCountryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this GlobalizationCountryInfo.  # noqa: E501


        :return: The display_name of this GlobalizationCountryInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GlobalizationCountryInfo.


        :param display_name: The display_name of this GlobalizationCountryInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def english_name(self):
        """Gets the english_name of this GlobalizationCountryInfo.  # noqa: E501


        :return: The english_name of this GlobalizationCountryInfo.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this GlobalizationCountryInfo.


        :param english_name: The english_name of this GlobalizationCountryInfo.  # noqa: E501
        :type: str
        """

        self._english_name = english_name

    @property
    def two_letter_iso_region_name(self):
        """Gets the two_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501


        :return: The two_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501
        :rtype: str
        """
        return self._two_letter_iso_region_name

    @two_letter_iso_region_name.setter
    def two_letter_iso_region_name(self, two_letter_iso_region_name):
        """Sets the two_letter_iso_region_name of this GlobalizationCountryInfo.


        :param two_letter_iso_region_name: The two_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501
        :type: str
        """

        self._two_letter_iso_region_name = two_letter_iso_region_name

    @property
    def three_letter_iso_region_name(self):
        """Gets the three_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501


        :return: The three_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_iso_region_name

    @three_letter_iso_region_name.setter
    def three_letter_iso_region_name(self, three_letter_iso_region_name):
        """Sets the three_letter_iso_region_name of this GlobalizationCountryInfo.


        :param three_letter_iso_region_name: The three_letter_iso_region_name of this GlobalizationCountryInfo.  # noqa: E501
        :type: str
        """

        self._three_letter_iso_region_name = three_letter_iso_region_name

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
        if issubclass(GlobalizationCountryInfo, dict):
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
        if not isinstance(other, GlobalizationCountryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
