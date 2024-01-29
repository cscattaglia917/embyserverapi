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

class PersistenceIntroDebugInfo(object):
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
        'path': 'str',
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'path': 'Path',
        'start': 'Start',
        'end': 'End'
    }

    def __init__(self, id=None, path=None, start=None, end=None):  # noqa: E501
        """PersistenceIntroDebugInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._path = None
        self._start = None
        self._end = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def id(self):
        """Gets the id of this PersistenceIntroDebugInfo.  # noqa: E501


        :return: The id of this PersistenceIntroDebugInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersistenceIntroDebugInfo.


        :param id: The id of this PersistenceIntroDebugInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this PersistenceIntroDebugInfo.  # noqa: E501


        :return: The path of this PersistenceIntroDebugInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PersistenceIntroDebugInfo.


        :param path: The path of this PersistenceIntroDebugInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def start(self):
        """Gets the start of this PersistenceIntroDebugInfo.  # noqa: E501


        :return: The start of this PersistenceIntroDebugInfo.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this PersistenceIntroDebugInfo.


        :param start: The start of this PersistenceIntroDebugInfo.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this PersistenceIntroDebugInfo.  # noqa: E501


        :return: The end of this PersistenceIntroDebugInfo.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this PersistenceIntroDebugInfo.


        :param end: The end of this PersistenceIntroDebugInfo.  # noqa: E501
        :type: int
        """

        self._end = end

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
        if issubclass(PersistenceIntroDebugInfo, dict):
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
        if not isinstance(other, PersistenceIntroDebugInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other