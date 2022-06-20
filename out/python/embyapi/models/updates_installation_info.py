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

class UpdatesInstallationInfo(object):
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
        'name': 'str',
        'assembly_guid': 'str',
        'version': 'str',
        'update_class': 'str',
        'percent_complete': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'assembly_guid': 'AssemblyGuid',
        'version': 'Version',
        'update_class': 'UpdateClass',
        'percent_complete': 'PercentComplete'
    }

    def __init__(self, id=None, name=None, assembly_guid=None, version=None, update_class=None, percent_complete=None):  # noqa: E501
        """UpdatesInstallationInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._assembly_guid = None
        self._version = None
        self._update_class = None
        self._percent_complete = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if assembly_guid is not None:
            self.assembly_guid = assembly_guid
        if version is not None:
            self.version = version
        if update_class is not None:
            self.update_class = update_class
        if percent_complete is not None:
            self.percent_complete = percent_complete

    @property
    def id(self):
        """Gets the id of this UpdatesInstallationInfo.  # noqa: E501


        :return: The id of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatesInstallationInfo.


        :param id: The id of this UpdatesInstallationInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdatesInstallationInfo.  # noqa: E501


        :return: The name of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatesInstallationInfo.


        :param name: The name of this UpdatesInstallationInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assembly_guid(self):
        """Gets the assembly_guid of this UpdatesInstallationInfo.  # noqa: E501


        :return: The assembly_guid of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: str
        """
        return self._assembly_guid

    @assembly_guid.setter
    def assembly_guid(self, assembly_guid):
        """Sets the assembly_guid of this UpdatesInstallationInfo.


        :param assembly_guid: The assembly_guid of this UpdatesInstallationInfo.  # noqa: E501
        :type: str
        """

        self._assembly_guid = assembly_guid

    @property
    def version(self):
        """Gets the version of this UpdatesInstallationInfo.  # noqa: E501


        :return: The version of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdatesInstallationInfo.


        :param version: The version of this UpdatesInstallationInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def update_class(self):
        """Gets the update_class of this UpdatesInstallationInfo.  # noqa: E501


        :return: The update_class of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: str
        """
        return self._update_class

    @update_class.setter
    def update_class(self, update_class):
        """Sets the update_class of this UpdatesInstallationInfo.


        :param update_class: The update_class of this UpdatesInstallationInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Release", "Beta", "Dev"]  # noqa: E501
        if update_class not in allowed_values:
            raise ValueError(
                "Invalid value for `update_class` ({0}), must be one of {1}"  # noqa: E501
                .format(update_class, allowed_values)
            )

        self._update_class = update_class

    @property
    def percent_complete(self):
        """Gets the percent_complete of this UpdatesInstallationInfo.  # noqa: E501


        :return: The percent_complete of this UpdatesInstallationInfo.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this UpdatesInstallationInfo.


        :param percent_complete: The percent_complete of this UpdatesInstallationInfo.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

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
        if issubclass(UpdatesInstallationInfo, dict):
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
        if not isinstance(other, UpdatesInstallationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
