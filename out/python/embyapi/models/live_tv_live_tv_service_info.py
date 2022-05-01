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

class LiveTvLiveTvServiceInfo(object):
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
        'home_page_url': 'str',
        'status': 'str',
        'status_message': 'str',
        'version': 'str',
        'has_update_available': 'bool',
        'is_visible': 'bool',
        'tuners': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'home_page_url': 'HomePageUrl',
        'status': 'Status',
        'status_message': 'StatusMessage',
        'version': 'Version',
        'has_update_available': 'HasUpdateAvailable',
        'is_visible': 'IsVisible',
        'tuners': 'Tuners'
    }

    def __init__(self, name=None, home_page_url=None, status=None, status_message=None, version=None, has_update_available=None, is_visible=None, tuners=None):  # noqa: E501
        """LiveTvLiveTvServiceInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._home_page_url = None
        self._status = None
        self._status_message = None
        self._version = None
        self._has_update_available = None
        self._is_visible = None
        self._tuners = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if home_page_url is not None:
            self.home_page_url = home_page_url
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if version is not None:
            self.version = version
        if has_update_available is not None:
            self.has_update_available = has_update_available
        if is_visible is not None:
            self.is_visible = is_visible
        if tuners is not None:
            self.tuners = tuners

    @property
    def name(self):
        """Gets the name of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The name of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveTvLiveTvServiceInfo.


        :param name: The name of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def home_page_url(self):
        """Gets the home_page_url of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The home_page_url of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._home_page_url

    @home_page_url.setter
    def home_page_url(self, home_page_url):
        """Sets the home_page_url of this LiveTvLiveTvServiceInfo.


        :param home_page_url: The home_page_url of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: str
        """

        self._home_page_url = home_page_url

    @property
    def status(self):
        """Gets the status of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The status of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveTvLiveTvServiceInfo.


        :param status: The status of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ok", "Unavailable"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The status_message of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this LiveTvLiveTvServiceInfo.


        :param status_message: The status_message of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def version(self):
        """Gets the version of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The version of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LiveTvLiveTvServiceInfo.


        :param version: The version of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def has_update_available(self):
        """Gets the has_update_available of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The has_update_available of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_update_available

    @has_update_available.setter
    def has_update_available(self, has_update_available):
        """Sets the has_update_available of this LiveTvLiveTvServiceInfo.


        :param has_update_available: The has_update_available of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: bool
        """

        self._has_update_available = has_update_available

    @property
    def is_visible(self):
        """Gets the is_visible of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The is_visible of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this LiveTvLiveTvServiceInfo.


        :param is_visible: The is_visible of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def tuners(self):
        """Gets the tuners of this LiveTvLiveTvServiceInfo.  # noqa: E501


        :return: The tuners of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tuners

    @tuners.setter
    def tuners(self, tuners):
        """Sets the tuners of this LiveTvLiveTvServiceInfo.


        :param tuners: The tuners of this LiveTvLiveTvServiceInfo.  # noqa: E501
        :type: list[str]
        """

        self._tuners = tuners

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
        if issubclass(LiveTvLiveTvServiceInfo, dict):
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
        if not isinstance(other, LiveTvLiveTvServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
