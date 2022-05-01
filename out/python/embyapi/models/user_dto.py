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

class UserDto(object):
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
        'server_id': 'str',
        'server_name': 'str',
        'connect_user_name': 'str',
        'connect_link_type': 'str',
        'id': 'str',
        'primary_image_tag': 'str',
        'has_password': 'bool',
        'has_configured_password': 'bool',
        'has_configured_easy_password': 'bool',
        'enable_auto_login': 'bool',
        'last_login_date': 'datetime',
        'last_activity_date': 'datetime',
        'configuration': 'ConfigurationUserConfiguration',
        'policy': 'UsersUserPolicy',
        'primary_image_aspect_ratio': 'float'
    }

    attribute_map = {
        'name': 'Name',
        'server_id': 'ServerId',
        'server_name': 'ServerName',
        'connect_user_name': 'ConnectUserName',
        'connect_link_type': 'ConnectLinkType',
        'id': 'Id',
        'primary_image_tag': 'PrimaryImageTag',
        'has_password': 'HasPassword',
        'has_configured_password': 'HasConfiguredPassword',
        'has_configured_easy_password': 'HasConfiguredEasyPassword',
        'enable_auto_login': 'EnableAutoLogin',
        'last_login_date': 'LastLoginDate',
        'last_activity_date': 'LastActivityDate',
        'configuration': 'Configuration',
        'policy': 'Policy',
        'primary_image_aspect_ratio': 'PrimaryImageAspectRatio'
    }

    def __init__(self, name=None, server_id=None, server_name=None, connect_user_name=None, connect_link_type=None, id=None, primary_image_tag=None, has_password=None, has_configured_password=None, has_configured_easy_password=None, enable_auto_login=None, last_login_date=None, last_activity_date=None, configuration=None, policy=None, primary_image_aspect_ratio=None):  # noqa: E501
        """UserDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._server_id = None
        self._server_name = None
        self._connect_user_name = None
        self._connect_link_type = None
        self._id = None
        self._primary_image_tag = None
        self._has_password = None
        self._has_configured_password = None
        self._has_configured_easy_password = None
        self._enable_auto_login = None
        self._last_login_date = None
        self._last_activity_date = None
        self._configuration = None
        self._policy = None
        self._primary_image_aspect_ratio = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if server_id is not None:
            self.server_id = server_id
        if server_name is not None:
            self.server_name = server_name
        if connect_user_name is not None:
            self.connect_user_name = connect_user_name
        if connect_link_type is not None:
            self.connect_link_type = connect_link_type
        if id is not None:
            self.id = id
        if primary_image_tag is not None:
            self.primary_image_tag = primary_image_tag
        if has_password is not None:
            self.has_password = has_password
        if has_configured_password is not None:
            self.has_configured_password = has_configured_password
        if has_configured_easy_password is not None:
            self.has_configured_easy_password = has_configured_easy_password
        if enable_auto_login is not None:
            self.enable_auto_login = enable_auto_login
        if last_login_date is not None:
            self.last_login_date = last_login_date
        if last_activity_date is not None:
            self.last_activity_date = last_activity_date
        if configuration is not None:
            self.configuration = configuration
        if policy is not None:
            self.policy = policy
        if primary_image_aspect_ratio is not None:
            self.primary_image_aspect_ratio = primary_image_aspect_ratio

    @property
    def name(self):
        """Gets the name of this UserDto.  # noqa: E501


        :return: The name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDto.


        :param name: The name of this UserDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def server_id(self):
        """Gets the server_id of this UserDto.  # noqa: E501


        :return: The server_id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this UserDto.


        :param server_id: The server_id of this UserDto.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def server_name(self):
        """Gets the server_name of this UserDto.  # noqa: E501


        :return: The server_name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this UserDto.


        :param server_name: The server_name of this UserDto.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def connect_user_name(self):
        """Gets the connect_user_name of this UserDto.  # noqa: E501


        :return: The connect_user_name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._connect_user_name

    @connect_user_name.setter
    def connect_user_name(self, connect_user_name):
        """Sets the connect_user_name of this UserDto.


        :param connect_user_name: The connect_user_name of this UserDto.  # noqa: E501
        :type: str
        """

        self._connect_user_name = connect_user_name

    @property
    def connect_link_type(self):
        """Gets the connect_link_type of this UserDto.  # noqa: E501


        :return: The connect_link_type of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._connect_link_type

    @connect_link_type.setter
    def connect_link_type(self, connect_link_type):
        """Sets the connect_link_type of this UserDto.


        :param connect_link_type: The connect_link_type of this UserDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["LinkedUser", "Guest"]  # noqa: E501
        if connect_link_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connect_link_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connect_link_type, allowed_values)
            )

        self._connect_link_type = connect_link_type

    @property
    def id(self):
        """Gets the id of this UserDto.  # noqa: E501


        :return: The id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDto.


        :param id: The id of this UserDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def primary_image_tag(self):
        """Gets the primary_image_tag of this UserDto.  # noqa: E501


        :return: The primary_image_tag of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._primary_image_tag

    @primary_image_tag.setter
    def primary_image_tag(self, primary_image_tag):
        """Sets the primary_image_tag of this UserDto.


        :param primary_image_tag: The primary_image_tag of this UserDto.  # noqa: E501
        :type: str
        """

        self._primary_image_tag = primary_image_tag

    @property
    def has_password(self):
        """Gets the has_password of this UserDto.  # noqa: E501


        :return: The has_password of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this UserDto.


        :param has_password: The has_password of this UserDto.  # noqa: E501
        :type: bool
        """

        self._has_password = has_password

    @property
    def has_configured_password(self):
        """Gets the has_configured_password of this UserDto.  # noqa: E501


        :return: The has_configured_password of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_configured_password

    @has_configured_password.setter
    def has_configured_password(self, has_configured_password):
        """Sets the has_configured_password of this UserDto.


        :param has_configured_password: The has_configured_password of this UserDto.  # noqa: E501
        :type: bool
        """

        self._has_configured_password = has_configured_password

    @property
    def has_configured_easy_password(self):
        """Gets the has_configured_easy_password of this UserDto.  # noqa: E501


        :return: The has_configured_easy_password of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_configured_easy_password

    @has_configured_easy_password.setter
    def has_configured_easy_password(self, has_configured_easy_password):
        """Sets the has_configured_easy_password of this UserDto.


        :param has_configured_easy_password: The has_configured_easy_password of this UserDto.  # noqa: E501
        :type: bool
        """

        self._has_configured_easy_password = has_configured_easy_password

    @property
    def enable_auto_login(self):
        """Gets the enable_auto_login of this UserDto.  # noqa: E501


        :return: The enable_auto_login of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_login

    @enable_auto_login.setter
    def enable_auto_login(self, enable_auto_login):
        """Sets the enable_auto_login of this UserDto.


        :param enable_auto_login: The enable_auto_login of this UserDto.  # noqa: E501
        :type: bool
        """

        self._enable_auto_login = enable_auto_login

    @property
    def last_login_date(self):
        """Gets the last_login_date of this UserDto.  # noqa: E501


        :return: The last_login_date of this UserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date):
        """Sets the last_login_date of this UserDto.


        :param last_login_date: The last_login_date of this UserDto.  # noqa: E501
        :type: datetime
        """

        self._last_login_date = last_login_date

    @property
    def last_activity_date(self):
        """Gets the last_activity_date of this UserDto.  # noqa: E501


        :return: The last_activity_date of this UserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity_date

    @last_activity_date.setter
    def last_activity_date(self, last_activity_date):
        """Sets the last_activity_date of this UserDto.


        :param last_activity_date: The last_activity_date of this UserDto.  # noqa: E501
        :type: datetime
        """

        self._last_activity_date = last_activity_date

    @property
    def configuration(self):
        """Gets the configuration of this UserDto.  # noqa: E501


        :return: The configuration of this UserDto.  # noqa: E501
        :rtype: ConfigurationUserConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this UserDto.


        :param configuration: The configuration of this UserDto.  # noqa: E501
        :type: ConfigurationUserConfiguration
        """

        self._configuration = configuration

    @property
    def policy(self):
        """Gets the policy of this UserDto.  # noqa: E501


        :return: The policy of this UserDto.  # noqa: E501
        :rtype: UsersUserPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this UserDto.


        :param policy: The policy of this UserDto.  # noqa: E501
        :type: UsersUserPolicy
        """

        self._policy = policy

    @property
    def primary_image_aspect_ratio(self):
        """Gets the primary_image_aspect_ratio of this UserDto.  # noqa: E501


        :return: The primary_image_aspect_ratio of this UserDto.  # noqa: E501
        :rtype: float
        """
        return self._primary_image_aspect_ratio

    @primary_image_aspect_ratio.setter
    def primary_image_aspect_ratio(self, primary_image_aspect_ratio):
        """Sets the primary_image_aspect_ratio of this UserDto.


        :param primary_image_aspect_ratio: The primary_image_aspect_ratio of this UserDto.  # noqa: E501
        :type: float
        """

        self._primary_image_aspect_ratio = primary_image_aspect_ratio

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
        if issubclass(UserDto, dict):
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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
