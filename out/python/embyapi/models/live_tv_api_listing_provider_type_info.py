# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LiveTVApiListingProviderTypeInfo(object):
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
        'id': 'str',
        'setup_url': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'id': 'Id',
        'setup_url': 'SetupUrl'
    }

    def __init__(self, name=None, id=None, setup_url=None):  # noqa: E501
        """LiveTVApiListingProviderTypeInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._setup_url = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if setup_url is not None:
            self.setup_url = setup_url

    @property
    def name(self):
        """Gets the name of this LiveTVApiListingProviderTypeInfo.  # noqa: E501


        :return: The name of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveTVApiListingProviderTypeInfo.


        :param name: The name of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this LiveTVApiListingProviderTypeInfo.  # noqa: E501


        :return: The id of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveTVApiListingProviderTypeInfo.


        :param id: The id of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def setup_url(self):
        """Gets the setup_url of this LiveTVApiListingProviderTypeInfo.  # noqa: E501


        :return: The setup_url of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :rtype: str
        """
        return self._setup_url

    @setup_url.setter
    def setup_url(self, setup_url):
        """Sets the setup_url of this LiveTVApiListingProviderTypeInfo.


        :param setup_url: The setup_url of this LiveTVApiListingProviderTypeInfo.  # noqa: E501
        :type: str
        """

        self._setup_url = setup_url

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
        if issubclass(LiveTVApiListingProviderTypeInfo, dict):
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
        if not isinstance(other, LiveTVApiListingProviderTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
