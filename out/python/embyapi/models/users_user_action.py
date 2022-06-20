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

class UsersUserAction(object):
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
        'server_id': 'str',
        'user_id': 'str',
        'item_id': 'str',
        'type': 'str',
        '_date': 'datetime',
        'position_ticks': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'server_id': 'ServerId',
        'user_id': 'UserId',
        'item_id': 'ItemId',
        'type': 'Type',
        '_date': 'Date',
        'position_ticks': 'PositionTicks'
    }

    def __init__(self, id=None, server_id=None, user_id=None, item_id=None, type=None, _date=None, position_ticks=None):  # noqa: E501
        """UsersUserAction - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._server_id = None
        self._user_id = None
        self._item_id = None
        self._type = None
        self.__date = None
        self._position_ticks = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if user_id is not None:
            self.user_id = user_id
        if item_id is not None:
            self.item_id = item_id
        if type is not None:
            self.type = type
        if _date is not None:
            self._date = _date
        if position_ticks is not None:
            self.position_ticks = position_ticks

    @property
    def id(self):
        """Gets the id of this UsersUserAction.  # noqa: E501


        :return: The id of this UsersUserAction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UsersUserAction.


        :param id: The id of this UsersUserAction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this UsersUserAction.  # noqa: E501


        :return: The server_id of this UsersUserAction.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this UsersUserAction.


        :param server_id: The server_id of this UsersUserAction.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def user_id(self):
        """Gets the user_id of this UsersUserAction.  # noqa: E501


        :return: The user_id of this UsersUserAction.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UsersUserAction.


        :param user_id: The user_id of this UsersUserAction.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def item_id(self):
        """Gets the item_id of this UsersUserAction.  # noqa: E501


        :return: The item_id of this UsersUserAction.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this UsersUserAction.


        :param item_id: The item_id of this UsersUserAction.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def type(self):
        """Gets the type of this UsersUserAction.  # noqa: E501


        :return: The type of this UsersUserAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UsersUserAction.


        :param type: The type of this UsersUserAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["PlayedItem"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def _date(self):
        """Gets the _date of this UsersUserAction.  # noqa: E501


        :return: The _date of this UsersUserAction.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this UsersUserAction.


        :param _date: The _date of this UsersUserAction.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def position_ticks(self):
        """Gets the position_ticks of this UsersUserAction.  # noqa: E501


        :return: The position_ticks of this UsersUserAction.  # noqa: E501
        :rtype: int
        """
        return self._position_ticks

    @position_ticks.setter
    def position_ticks(self, position_ticks):
        """Sets the position_ticks of this UsersUserAction.


        :param position_ticks: The position_ticks of this UsersUserAction.  # noqa: E501
        :type: int
        """

        self._position_ticks = position_ticks

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
        if issubclass(UsersUserAction, dict):
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
        if not isinstance(other, UsersUserAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
