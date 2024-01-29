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

class NotificationsNotificationTypeInfo(object):
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
        'type': 'str',
        'name': 'str',
        'enabled': 'bool',
        'category': 'str',
        'is_based_on_user_event': 'bool'
    }

    attribute_map = {
        'type': 'Type',
        'name': 'Name',
        'enabled': 'Enabled',
        'category': 'Category',
        'is_based_on_user_event': 'IsBasedOnUserEvent'
    }

    def __init__(self, type=None, name=None, enabled=None, category=None, is_based_on_user_event=None):  # noqa: E501
        """NotificationsNotificationTypeInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._enabled = None
        self._category = None
        self._is_based_on_user_event = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if category is not None:
            self.category = category
        if is_based_on_user_event is not None:
            self.is_based_on_user_event = is_based_on_user_event

    @property
    def type(self):
        """Gets the type of this NotificationsNotificationTypeInfo.  # noqa: E501


        :return: The type of this NotificationsNotificationTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationsNotificationTypeInfo.


        :param type: The type of this NotificationsNotificationTypeInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this NotificationsNotificationTypeInfo.  # noqa: E501


        :return: The name of this NotificationsNotificationTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationsNotificationTypeInfo.


        :param name: The name of this NotificationsNotificationTypeInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this NotificationsNotificationTypeInfo.  # noqa: E501


        :return: The enabled of this NotificationsNotificationTypeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NotificationsNotificationTypeInfo.


        :param enabled: The enabled of this NotificationsNotificationTypeInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def category(self):
        """Gets the category of this NotificationsNotificationTypeInfo.  # noqa: E501


        :return: The category of this NotificationsNotificationTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NotificationsNotificationTypeInfo.


        :param category: The category of this NotificationsNotificationTypeInfo.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def is_based_on_user_event(self):
        """Gets the is_based_on_user_event of this NotificationsNotificationTypeInfo.  # noqa: E501


        :return: The is_based_on_user_event of this NotificationsNotificationTypeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_based_on_user_event

    @is_based_on_user_event.setter
    def is_based_on_user_event(self, is_based_on_user_event):
        """Sets the is_based_on_user_event of this NotificationsNotificationTypeInfo.


        :param is_based_on_user_event: The is_based_on_user_event of this NotificationsNotificationTypeInfo.  # noqa: E501
        :type: bool
        """

        self._is_based_on_user_event = is_based_on_user_event

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
        if issubclass(NotificationsNotificationTypeInfo, dict):
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
        if not isinstance(other, NotificationsNotificationTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
