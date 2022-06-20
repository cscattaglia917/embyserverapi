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

class QueueItem(object):
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
        'id': 'int',
        'playlist_item_id': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'playlist_item_id': 'PlaylistItemId'
    }

    def __init__(self, id=None, playlist_item_id=None):  # noqa: E501
        """QueueItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._playlist_item_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if playlist_item_id is not None:
            self.playlist_item_id = playlist_item_id

    @property
    def id(self):
        """Gets the id of this QueueItem.  # noqa: E501


        :return: The id of this QueueItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueItem.


        :param id: The id of this QueueItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def playlist_item_id(self):
        """Gets the playlist_item_id of this QueueItem.  # noqa: E501


        :return: The playlist_item_id of this QueueItem.  # noqa: E501
        :rtype: str
        """
        return self._playlist_item_id

    @playlist_item_id.setter
    def playlist_item_id(self, playlist_item_id):
        """Sets the playlist_item_id of this QueueItem.


        :param playlist_item_id: The playlist_item_id of this QueueItem.  # noqa: E501
        :type: str
        """

        self._playlist_item_id = playlist_item_id

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
        if issubclass(QueueItem, dict):
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
        if not isinstance(other, QueueItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
