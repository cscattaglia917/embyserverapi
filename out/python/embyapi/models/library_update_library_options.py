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

class LibraryUpdateLibraryOptions(object):
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
        'library_options': 'ConfigurationLibraryOptions'
    }

    attribute_map = {
        'id': 'Id',
        'library_options': 'LibraryOptions'
    }

    def __init__(self, id=None, library_options=None):  # noqa: E501
        """LibraryUpdateLibraryOptions - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._library_options = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if library_options is not None:
            self.library_options = library_options

    @property
    def id(self):
        """Gets the id of this LibraryUpdateLibraryOptions.  # noqa: E501


        :return: The id of this LibraryUpdateLibraryOptions.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibraryUpdateLibraryOptions.


        :param id: The id of this LibraryUpdateLibraryOptions.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def library_options(self):
        """Gets the library_options of this LibraryUpdateLibraryOptions.  # noqa: E501


        :return: The library_options of this LibraryUpdateLibraryOptions.  # noqa: E501
        :rtype: ConfigurationLibraryOptions
        """
        return self._library_options

    @library_options.setter
    def library_options(self, library_options):
        """Sets the library_options of this LibraryUpdateLibraryOptions.


        :param library_options: The library_options of this LibraryUpdateLibraryOptions.  # noqa: E501
        :type: ConfigurationLibraryOptions
        """

        self._library_options = library_options

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
        if issubclass(LibraryUpdateLibraryOptions, dict):
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
        if not isinstance(other, LibraryUpdateLibraryOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
