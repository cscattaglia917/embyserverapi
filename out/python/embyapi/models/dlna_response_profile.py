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

class DlnaResponseProfile(object):
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
        'container': 'str',
        'audio_codec': 'str',
        'video_codec': 'str',
        'type': 'str',
        'org_pn': 'str',
        'mime_type': 'str',
        'conditions': 'list[DlnaProfileCondition]'
    }

    attribute_map = {
        'container': 'Container',
        'audio_codec': 'AudioCodec',
        'video_codec': 'VideoCodec',
        'type': 'Type',
        'org_pn': 'OrgPn',
        'mime_type': 'MimeType',
        'conditions': 'Conditions'
    }

    def __init__(self, container=None, audio_codec=None, video_codec=None, type=None, org_pn=None, mime_type=None, conditions=None):  # noqa: E501
        """DlnaResponseProfile - a model defined in Swagger"""  # noqa: E501
        self._container = None
        self._audio_codec = None
        self._video_codec = None
        self._type = None
        self._org_pn = None
        self._mime_type = None
        self._conditions = None
        self.discriminator = None
        if container is not None:
            self.container = container
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if video_codec is not None:
            self.video_codec = video_codec
        if type is not None:
            self.type = type
        if org_pn is not None:
            self.org_pn = org_pn
        if mime_type is not None:
            self.mime_type = mime_type
        if conditions is not None:
            self.conditions = conditions

    @property
    def container(self):
        """Gets the container of this DlnaResponseProfile.  # noqa: E501


        :return: The container of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this DlnaResponseProfile.


        :param container: The container of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def audio_codec(self):
        """Gets the audio_codec of this DlnaResponseProfile.  # noqa: E501


        :return: The audio_codec of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this DlnaResponseProfile.


        :param audio_codec: The audio_codec of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """

        self._audio_codec = audio_codec

    @property
    def video_codec(self):
        """Gets the video_codec of this DlnaResponseProfile.  # noqa: E501


        :return: The video_codec of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this DlnaResponseProfile.


        :param video_codec: The video_codec of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """

        self._video_codec = video_codec

    @property
    def type(self):
        """Gets the type of this DlnaResponseProfile.  # noqa: E501


        :return: The type of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DlnaResponseProfile.


        :param type: The type of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["Audio", "Video", "Photo"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def org_pn(self):
        """Gets the org_pn of this DlnaResponseProfile.  # noqa: E501


        :return: The org_pn of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._org_pn

    @org_pn.setter
    def org_pn(self, org_pn):
        """Sets the org_pn of this DlnaResponseProfile.


        :param org_pn: The org_pn of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """

        self._org_pn = org_pn

    @property
    def mime_type(self):
        """Gets the mime_type of this DlnaResponseProfile.  # noqa: E501


        :return: The mime_type of this DlnaResponseProfile.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DlnaResponseProfile.


        :param mime_type: The mime_type of this DlnaResponseProfile.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def conditions(self):
        """Gets the conditions of this DlnaResponseProfile.  # noqa: E501


        :return: The conditions of this DlnaResponseProfile.  # noqa: E501
        :rtype: list[DlnaProfileCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DlnaResponseProfile.


        :param conditions: The conditions of this DlnaResponseProfile.  # noqa: E501
        :type: list[DlnaProfileCondition]
        """

        self._conditions = conditions

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
        if issubclass(DlnaResponseProfile, dict):
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
        if not isinstance(other, DlnaResponseProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
