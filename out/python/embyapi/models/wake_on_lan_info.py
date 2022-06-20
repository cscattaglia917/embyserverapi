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

class WakeOnLanInfo(object):
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
        'mac_address': 'str',
        'broadcast_address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'mac_address': 'MacAddress',
        'broadcast_address': 'BroadcastAddress',
        'port': 'Port'
    }

    def __init__(self, mac_address=None, broadcast_address=None, port=None):  # noqa: E501
        """WakeOnLanInfo - a model defined in Swagger"""  # noqa: E501
        self._mac_address = None
        self._broadcast_address = None
        self._port = None
        self.discriminator = None
        if mac_address is not None:
            self.mac_address = mac_address
        if broadcast_address is not None:
            self.broadcast_address = broadcast_address
        if port is not None:
            self.port = port

    @property
    def mac_address(self):
        """Gets the mac_address of this WakeOnLanInfo.  # noqa: E501


        :return: The mac_address of this WakeOnLanInfo.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this WakeOnLanInfo.


        :param mac_address: The mac_address of this WakeOnLanInfo.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def broadcast_address(self):
        """Gets the broadcast_address of this WakeOnLanInfo.  # noqa: E501


        :return: The broadcast_address of this WakeOnLanInfo.  # noqa: E501
        :rtype: str
        """
        return self._broadcast_address

    @broadcast_address.setter
    def broadcast_address(self, broadcast_address):
        """Sets the broadcast_address of this WakeOnLanInfo.


        :param broadcast_address: The broadcast_address of this WakeOnLanInfo.  # noqa: E501
        :type: str
        """

        self._broadcast_address = broadcast_address

    @property
    def port(self):
        """Gets the port of this WakeOnLanInfo.  # noqa: E501


        :return: The port of this WakeOnLanInfo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WakeOnLanInfo.


        :param port: The port of this WakeOnLanInfo.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(WakeOnLanInfo, dict):
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
        if not isinstance(other, WakeOnLanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
