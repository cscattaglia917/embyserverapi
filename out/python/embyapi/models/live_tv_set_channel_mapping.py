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

class LiveTvSetChannelMapping(object):
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
        'tuner_channel_id': 'str',
        'provider_channel_id': 'str'
    }

    attribute_map = {
        'tuner_channel_id': 'TunerChannelId',
        'provider_channel_id': 'ProviderChannelId'
    }

    def __init__(self, tuner_channel_id=None, provider_channel_id=None):  # noqa: E501
        """LiveTvSetChannelMapping - a model defined in Swagger"""  # noqa: E501
        self._tuner_channel_id = None
        self._provider_channel_id = None
        self.discriminator = None
        if tuner_channel_id is not None:
            self.tuner_channel_id = tuner_channel_id
        if provider_channel_id is not None:
            self.provider_channel_id = provider_channel_id

    @property
    def tuner_channel_id(self):
        """Gets the tuner_channel_id of this LiveTvSetChannelMapping.  # noqa: E501


        :return: The tuner_channel_id of this LiveTvSetChannelMapping.  # noqa: E501
        :rtype: str
        """
        return self._tuner_channel_id

    @tuner_channel_id.setter
    def tuner_channel_id(self, tuner_channel_id):
        """Sets the tuner_channel_id of this LiveTvSetChannelMapping.


        :param tuner_channel_id: The tuner_channel_id of this LiveTvSetChannelMapping.  # noqa: E501
        :type: str
        """

        self._tuner_channel_id = tuner_channel_id

    @property
    def provider_channel_id(self):
        """Gets the provider_channel_id of this LiveTvSetChannelMapping.  # noqa: E501


        :return: The provider_channel_id of this LiveTvSetChannelMapping.  # noqa: E501
        :rtype: str
        """
        return self._provider_channel_id

    @provider_channel_id.setter
    def provider_channel_id(self, provider_channel_id):
        """Sets the provider_channel_id of this LiveTvSetChannelMapping.


        :param provider_channel_id: The provider_channel_id of this LiveTvSetChannelMapping.  # noqa: E501
        :type: str
        """

        self._provider_channel_id = provider_channel_id

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
        if issubclass(LiveTvSetChannelMapping, dict):
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
        if not isinstance(other, LiveTvSetChannelMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
