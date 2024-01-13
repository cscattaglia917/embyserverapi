# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EmbyReportsApiModelReportHeader(object):
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
        'header_field_type': 'str',
        'name': 'str',
        'field_name': 'str',
        'sort_field': 'str',
        'type': 'str',
        'item_view_type': 'str',
        'visible': 'bool',
        'display_type': 'str',
        'show_header_label': 'bool',
        'can_group': 'bool'
    }

    attribute_map = {
        'header_field_type': 'HeaderFieldType',
        'name': 'Name',
        'field_name': 'FieldName',
        'sort_field': 'SortField',
        'type': 'Type',
        'item_view_type': 'ItemViewType',
        'visible': 'Visible',
        'display_type': 'DisplayType',
        'show_header_label': 'ShowHeaderLabel',
        'can_group': 'CanGroup'
    }

    def __init__(self, header_field_type=None, name=None, field_name=None, sort_field=None, type=None, item_view_type=None, visible=None, display_type=None, show_header_label=None, can_group=None):  # noqa: E501
        """EmbyReportsApiModelReportHeader - a model defined in Swagger"""  # noqa: E501
        self._header_field_type = None
        self._name = None
        self._field_name = None
        self._sort_field = None
        self._type = None
        self._item_view_type = None
        self._visible = None
        self._display_type = None
        self._show_header_label = None
        self._can_group = None
        self.discriminator = None
        if header_field_type is not None:
            self.header_field_type = header_field_type
        if name is not None:
            self.name = name
        if field_name is not None:
            self.field_name = field_name
        if sort_field is not None:
            self.sort_field = sort_field
        if type is not None:
            self.type = type
        if item_view_type is not None:
            self.item_view_type = item_view_type
        if visible is not None:
            self.visible = visible
        if display_type is not None:
            self.display_type = display_type
        if show_header_label is not None:
            self.show_header_label = show_header_label
        if can_group is not None:
            self.can_group = can_group

    @property
    def header_field_type(self):
        """Gets the header_field_type of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The header_field_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._header_field_type

    @header_field_type.setter
    def header_field_type(self, header_field_type):
        """Sets the header_field_type of this EmbyReportsApiModelReportHeader.


        :param header_field_type: The header_field_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["String", "Boolean", "Date", "Time", "DateTime", "Int", "Image", "Object", "Minutes"]  # noqa: E501
        if header_field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `header_field_type` ({0}), must be one of {1}"  # noqa: E501
                .format(header_field_type, allowed_values)
            )

        self._header_field_type = header_field_type

    @property
    def name(self):
        """Gets the name of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The name of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmbyReportsApiModelReportHeader.


        :param name: The name of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def field_name(self):
        """Gets the field_name of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The field_name of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this EmbyReportsApiModelReportHeader.


        :param field_name: The field_name of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Path", "Name", "SortName", "PremiereDate", "DateAdded", "ReleaseDate", "Runtime", "PlayCount", "Season", "SeasonNumber", "Series", "Network", "Year", "ParentalRating", "CommunityRating", "Trailers", "Specials", "GameSystem", "AlbumArtist", "Album", "Disc", "Track", "Audio", "EmbeddedImage", "Video", "Width", "Height", "Subtitles", "Genres", "Countries", "Status", "Tracks", "EpisodeSeries", "EpisodeSeason", "EpisodeNumber", "AudioAlbumArtist", "MusicArtist", "AudioAlbum", "Locked", "ImagePrimary", "ImageBackdrop", "ImageLogo", "Actor", "Studios", "Composer", "Director", "GuestStar", "Producer", "Writer", "Artist", "Years", "ParentalRatings", "CommunityRatings", "Overview", "ShortOverview", "Type", "Date", "UserPrimaryImage", "Severity", "Item", "User", "UserId"]  # noqa: E501
        if field_name not in allowed_values:
            raise ValueError(
                "Invalid value for `field_name` ({0}), must be one of {1}"  # noqa: E501
                .format(field_name, allowed_values)
            )

        self._field_name = field_name

    @property
    def sort_field(self):
        """Gets the sort_field of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The sort_field of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this EmbyReportsApiModelReportHeader.


        :param sort_field: The sort_field of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

    @property
    def type(self):
        """Gets the type of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmbyReportsApiModelReportHeader.


        :param type: The type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def item_view_type(self):
        """Gets the item_view_type of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The item_view_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._item_view_type

    @item_view_type.setter
    def item_view_type(self, item_view_type):
        """Sets the item_view_type of this EmbyReportsApiModelReportHeader.


        :param item_view_type: The item_view_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Detail", "Edit", "List", "ItemByNameDetails", "StatusImage", "EmbeddedImage", "SubtitleImage", "TrailersImage", "SpecialsImage", "LockDataImage", "TagsPrimaryImage", "TagsBackdropImage", "TagsLogoImage", "UserPrimaryImage"]  # noqa: E501
        if item_view_type not in allowed_values:
            raise ValueError(
                "Invalid value for `item_view_type` ({0}), must be one of {1}"  # noqa: E501
                .format(item_view_type, allowed_values)
            )

        self._item_view_type = item_view_type

    @property
    def visible(self):
        """Gets the visible of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The visible of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this EmbyReportsApiModelReportHeader.


        :param visible: The visible of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def display_type(self):
        """Gets the display_type of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The display_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this EmbyReportsApiModelReportHeader.


        :param display_type: The display_type of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Screen", "Export", "ScreenExport"]  # noqa: E501
        if display_type not in allowed_values:
            raise ValueError(
                "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                .format(display_type, allowed_values)
            )

        self._display_type = display_type

    @property
    def show_header_label(self):
        """Gets the show_header_label of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The show_header_label of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: bool
        """
        return self._show_header_label

    @show_header_label.setter
    def show_header_label(self, show_header_label):
        """Sets the show_header_label of this EmbyReportsApiModelReportHeader.


        :param show_header_label: The show_header_label of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: bool
        """

        self._show_header_label = show_header_label

    @property
    def can_group(self):
        """Gets the can_group of this EmbyReportsApiModelReportHeader.  # noqa: E501


        :return: The can_group of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :rtype: bool
        """
        return self._can_group

    @can_group.setter
    def can_group(self, can_group):
        """Sets the can_group of this EmbyReportsApiModelReportHeader.


        :param can_group: The can_group of this EmbyReportsApiModelReportHeader.  # noqa: E501
        :type: bool
        """

        self._can_group = can_group

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
        if issubclass(EmbyReportsApiModelReportHeader, dict):
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
        if not isinstance(other, EmbyReportsApiModelReportHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
