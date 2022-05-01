# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DlnaSubtitleProfile(object):
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
        'format': 'str',
        'method': 'str',
        'didl_mode': 'str',
        'language': 'str',
        'container': 'str'
    }

    attribute_map = {
        'format': 'Format',
        'method': 'Method',
        'didl_mode': 'DidlMode',
        'language': 'Language',
        'container': 'Container'
    }

    def __init__(self, format=None, method=None, didl_mode=None, language=None, container=None):  # noqa: E501
        """DlnaSubtitleProfile - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._method = None
        self._didl_mode = None
        self._language = None
        self._container = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if method is not None:
            self.method = method
        if didl_mode is not None:
            self.didl_mode = didl_mode
        if language is not None:
            self.language = language
        if container is not None:
            self.container = container

    @property
    def format(self):
        """Gets the format of this DlnaSubtitleProfile.  # noqa: E501


        :return: The format of this DlnaSubtitleProfile.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DlnaSubtitleProfile.


        :param format: The format of this DlnaSubtitleProfile.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def method(self):
        """Gets the method of this DlnaSubtitleProfile.  # noqa: E501


        :return: The method of this DlnaSubtitleProfile.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this DlnaSubtitleProfile.


        :param method: The method of this DlnaSubtitleProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["Encode", "Embed", "External", "Hls"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def didl_mode(self):
        """Gets the didl_mode of this DlnaSubtitleProfile.  # noqa: E501


        :return: The didl_mode of this DlnaSubtitleProfile.  # noqa: E501
        :rtype: str
        """
        return self._didl_mode

    @didl_mode.setter
    def didl_mode(self, didl_mode):
        """Sets the didl_mode of this DlnaSubtitleProfile.


        :param didl_mode: The didl_mode of this DlnaSubtitleProfile.  # noqa: E501
        :type: str
        """

        self._didl_mode = didl_mode

    @property
    def language(self):
        """Gets the language of this DlnaSubtitleProfile.  # noqa: E501


        :return: The language of this DlnaSubtitleProfile.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DlnaSubtitleProfile.


        :param language: The language of this DlnaSubtitleProfile.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def container(self):
        """Gets the container of this DlnaSubtitleProfile.  # noqa: E501


        :return: The container of this DlnaSubtitleProfile.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this DlnaSubtitleProfile.


        :param container: The container of this DlnaSubtitleProfile.  # noqa: E501
        :type: str
        """

        self._container = container

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
        if issubclass(DlnaSubtitleProfile, dict):
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
        if not isinstance(other, DlnaSubtitleProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
