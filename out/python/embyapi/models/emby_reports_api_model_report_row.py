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

class EmbyReportsApiModelReportRow(object):
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
        'has_image_tags_backdrop': 'bool',
        'has_image_tags_primary': 'bool',
        'has_image_tags_logo': 'bool',
        'has_local_trailer': 'bool',
        'has_lock_data': 'bool',
        'has_embedded_image': 'bool',
        'has_subtitles': 'bool',
        'has_specials': 'bool',
        'columns': 'list[EmbyReportsApiModelReportItem]',
        'row_type': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'has_image_tags_backdrop': 'HasImageTagsBackdrop',
        'has_image_tags_primary': 'HasImageTagsPrimary',
        'has_image_tags_logo': 'HasImageTagsLogo',
        'has_local_trailer': 'HasLocalTrailer',
        'has_lock_data': 'HasLockData',
        'has_embedded_image': 'HasEmbeddedImage',
        'has_subtitles': 'HasSubtitles',
        'has_specials': 'HasSpecials',
        'columns': 'Columns',
        'row_type': 'RowType',
        'user_id': 'UserId'
    }

    def __init__(self, id=None, has_image_tags_backdrop=None, has_image_tags_primary=None, has_image_tags_logo=None, has_local_trailer=None, has_lock_data=None, has_embedded_image=None, has_subtitles=None, has_specials=None, columns=None, row_type=None, user_id=None):  # noqa: E501
        """EmbyReportsApiModelReportRow - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._has_image_tags_backdrop = None
        self._has_image_tags_primary = None
        self._has_image_tags_logo = None
        self._has_local_trailer = None
        self._has_lock_data = None
        self._has_embedded_image = None
        self._has_subtitles = None
        self._has_specials = None
        self._columns = None
        self._row_type = None
        self._user_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if has_image_tags_backdrop is not None:
            self.has_image_tags_backdrop = has_image_tags_backdrop
        if has_image_tags_primary is not None:
            self.has_image_tags_primary = has_image_tags_primary
        if has_image_tags_logo is not None:
            self.has_image_tags_logo = has_image_tags_logo
        if has_local_trailer is not None:
            self.has_local_trailer = has_local_trailer
        if has_lock_data is not None:
            self.has_lock_data = has_lock_data
        if has_embedded_image is not None:
            self.has_embedded_image = has_embedded_image
        if has_subtitles is not None:
            self.has_subtitles = has_subtitles
        if has_specials is not None:
            self.has_specials = has_specials
        if columns is not None:
            self.columns = columns
        if row_type is not None:
            self.row_type = row_type
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The id of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmbyReportsApiModelReportRow.


        :param id: The id of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def has_image_tags_backdrop(self):
        """Gets the has_image_tags_backdrop of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_image_tags_backdrop of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_image_tags_backdrop

    @has_image_tags_backdrop.setter
    def has_image_tags_backdrop(self, has_image_tags_backdrop):
        """Sets the has_image_tags_backdrop of this EmbyReportsApiModelReportRow.


        :param has_image_tags_backdrop: The has_image_tags_backdrop of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_image_tags_backdrop = has_image_tags_backdrop

    @property
    def has_image_tags_primary(self):
        """Gets the has_image_tags_primary of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_image_tags_primary of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_image_tags_primary

    @has_image_tags_primary.setter
    def has_image_tags_primary(self, has_image_tags_primary):
        """Sets the has_image_tags_primary of this EmbyReportsApiModelReportRow.


        :param has_image_tags_primary: The has_image_tags_primary of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_image_tags_primary = has_image_tags_primary

    @property
    def has_image_tags_logo(self):
        """Gets the has_image_tags_logo of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_image_tags_logo of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_image_tags_logo

    @has_image_tags_logo.setter
    def has_image_tags_logo(self, has_image_tags_logo):
        """Sets the has_image_tags_logo of this EmbyReportsApiModelReportRow.


        :param has_image_tags_logo: The has_image_tags_logo of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_image_tags_logo = has_image_tags_logo

    @property
    def has_local_trailer(self):
        """Gets the has_local_trailer of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_local_trailer of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_local_trailer

    @has_local_trailer.setter
    def has_local_trailer(self, has_local_trailer):
        """Sets the has_local_trailer of this EmbyReportsApiModelReportRow.


        :param has_local_trailer: The has_local_trailer of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_local_trailer = has_local_trailer

    @property
    def has_lock_data(self):
        """Gets the has_lock_data of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_lock_data of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_lock_data

    @has_lock_data.setter
    def has_lock_data(self, has_lock_data):
        """Sets the has_lock_data of this EmbyReportsApiModelReportRow.


        :param has_lock_data: The has_lock_data of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_lock_data = has_lock_data

    @property
    def has_embedded_image(self):
        """Gets the has_embedded_image of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_embedded_image of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_embedded_image

    @has_embedded_image.setter
    def has_embedded_image(self, has_embedded_image):
        """Sets the has_embedded_image of this EmbyReportsApiModelReportRow.


        :param has_embedded_image: The has_embedded_image of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_embedded_image = has_embedded_image

    @property
    def has_subtitles(self):
        """Gets the has_subtitles of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_subtitles of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_subtitles

    @has_subtitles.setter
    def has_subtitles(self, has_subtitles):
        """Sets the has_subtitles of this EmbyReportsApiModelReportRow.


        :param has_subtitles: The has_subtitles of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_subtitles = has_subtitles

    @property
    def has_specials(self):
        """Gets the has_specials of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The has_specials of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: bool
        """
        return self._has_specials

    @has_specials.setter
    def has_specials(self, has_specials):
        """Sets the has_specials of this EmbyReportsApiModelReportRow.


        :param has_specials: The has_specials of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: bool
        """

        self._has_specials = has_specials

    @property
    def columns(self):
        """Gets the columns of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The columns of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: list[EmbyReportsApiModelReportItem]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this EmbyReportsApiModelReportRow.


        :param columns: The columns of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: list[EmbyReportsApiModelReportItem]
        """

        self._columns = columns

    @property
    def row_type(self):
        """Gets the row_type of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The row_type of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: str
        """
        return self._row_type

    @row_type.setter
    def row_type(self, row_type):
        """Sets the row_type of this EmbyReportsApiModelReportRow.


        :param row_type: The row_type of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: str
        """
        allowed_values = ["MusicArtist", "MusicAlbum", "Book", "BoxSet", "Episode", "Game", "Video", "Movie", "MusicVideo", "Trailer", "Season", "Series", "Audio", "BaseItem", "Artist"]  # noqa: E501
        if row_type not in allowed_values:
            raise ValueError(
                "Invalid value for `row_type` ({0}), must be one of {1}"  # noqa: E501
                .format(row_type, allowed_values)
            )

        self._row_type = row_type

    @property
    def user_id(self):
        """Gets the user_id of this EmbyReportsApiModelReportRow.  # noqa: E501


        :return: The user_id of this EmbyReportsApiModelReportRow.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EmbyReportsApiModelReportRow.


        :param user_id: The user_id of this EmbyReportsApiModelReportRow.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(EmbyReportsApiModelReportRow, dict):
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
        if not isinstance(other, EmbyReportsApiModelReportRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
