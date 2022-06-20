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

class VirtualFolderInfo(object):
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
        'locations': 'list[str]',
        'collection_type': 'str',
        'library_options': 'ConfigurationLibraryOptions',
        'item_id': 'str',
        'primary_image_item_id': 'str',
        'refresh_progress': 'float',
        'refresh_status': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'locations': 'Locations',
        'collection_type': 'CollectionType',
        'library_options': 'LibraryOptions',
        'item_id': 'ItemId',
        'primary_image_item_id': 'PrimaryImageItemId',
        'refresh_progress': 'RefreshProgress',
        'refresh_status': 'RefreshStatus'
    }

    def __init__(self, name=None, locations=None, collection_type=None, library_options=None, item_id=None, primary_image_item_id=None, refresh_progress=None, refresh_status=None):  # noqa: E501
        """VirtualFolderInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._locations = None
        self._collection_type = None
        self._library_options = None
        self._item_id = None
        self._primary_image_item_id = None
        self._refresh_progress = None
        self._refresh_status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if locations is not None:
            self.locations = locations
        if collection_type is not None:
            self.collection_type = collection_type
        if library_options is not None:
            self.library_options = library_options
        if item_id is not None:
            self.item_id = item_id
        if primary_image_item_id is not None:
            self.primary_image_item_id = primary_image_item_id
        if refresh_progress is not None:
            self.refresh_progress = refresh_progress
        if refresh_status is not None:
            self.refresh_status = refresh_status

    @property
    def name(self):
        """Gets the name of this VirtualFolderInfo.  # noqa: E501


        :return: The name of this VirtualFolderInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualFolderInfo.


        :param name: The name of this VirtualFolderInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def locations(self):
        """Gets the locations of this VirtualFolderInfo.  # noqa: E501


        :return: The locations of this VirtualFolderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this VirtualFolderInfo.


        :param locations: The locations of this VirtualFolderInfo.  # noqa: E501
        :type: list[str]
        """

        self._locations = locations

    @property
    def collection_type(self):
        """Gets the collection_type of this VirtualFolderInfo.  # noqa: E501


        :return: The collection_type of this VirtualFolderInfo.  # noqa: E501
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """Sets the collection_type of this VirtualFolderInfo.


        :param collection_type: The collection_type of this VirtualFolderInfo.  # noqa: E501
        :type: str
        """

        self._collection_type = collection_type

    @property
    def library_options(self):
        """Gets the library_options of this VirtualFolderInfo.  # noqa: E501


        :return: The library_options of this VirtualFolderInfo.  # noqa: E501
        :rtype: ConfigurationLibraryOptions
        """
        return self._library_options

    @library_options.setter
    def library_options(self, library_options):
        """Sets the library_options of this VirtualFolderInfo.


        :param library_options: The library_options of this VirtualFolderInfo.  # noqa: E501
        :type: ConfigurationLibraryOptions
        """

        self._library_options = library_options

    @property
    def item_id(self):
        """Gets the item_id of this VirtualFolderInfo.  # noqa: E501


        :return: The item_id of this VirtualFolderInfo.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this VirtualFolderInfo.


        :param item_id: The item_id of this VirtualFolderInfo.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def primary_image_item_id(self):
        """Gets the primary_image_item_id of this VirtualFolderInfo.  # noqa: E501


        :return: The primary_image_item_id of this VirtualFolderInfo.  # noqa: E501
        :rtype: str
        """
        return self._primary_image_item_id

    @primary_image_item_id.setter
    def primary_image_item_id(self, primary_image_item_id):
        """Sets the primary_image_item_id of this VirtualFolderInfo.


        :param primary_image_item_id: The primary_image_item_id of this VirtualFolderInfo.  # noqa: E501
        :type: str
        """

        self._primary_image_item_id = primary_image_item_id

    @property
    def refresh_progress(self):
        """Gets the refresh_progress of this VirtualFolderInfo.  # noqa: E501


        :return: The refresh_progress of this VirtualFolderInfo.  # noqa: E501
        :rtype: float
        """
        return self._refresh_progress

    @refresh_progress.setter
    def refresh_progress(self, refresh_progress):
        """Sets the refresh_progress of this VirtualFolderInfo.


        :param refresh_progress: The refresh_progress of this VirtualFolderInfo.  # noqa: E501
        :type: float
        """

        self._refresh_progress = refresh_progress

    @property
    def refresh_status(self):
        """Gets the refresh_status of this VirtualFolderInfo.  # noqa: E501


        :return: The refresh_status of this VirtualFolderInfo.  # noqa: E501
        :rtype: str
        """
        return self._refresh_status

    @refresh_status.setter
    def refresh_status(self, refresh_status):
        """Sets the refresh_status of this VirtualFolderInfo.


        :param refresh_status: The refresh_status of this VirtualFolderInfo.  # noqa: E501
        :type: str
        """

        self._refresh_status = refresh_status

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
        if issubclass(VirtualFolderInfo, dict):
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
        if not isinstance(other, VirtualFolderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
