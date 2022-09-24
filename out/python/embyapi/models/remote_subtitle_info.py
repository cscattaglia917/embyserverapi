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

class RemoteSubtitleInfo(object):
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
        'three_letter_iso_language_name': 'str',
        'id': 'str',
        'provider_name': 'str',
        'name': 'str',
        'format': 'str',
        'author': 'str',
        'comment': 'str',
        'date_created': 'datetime',
        'community_rating': 'float',
        'download_count': 'int',
        'is_hash_match': 'bool',
        'is_forced': 'bool',
        'language': 'str'
    }

    attribute_map = {
        'three_letter_iso_language_name': 'ThreeLetterISOLanguageName',
        'id': 'Id',
        'provider_name': 'ProviderName',
        'name': 'Name',
        'format': 'Format',
        'author': 'Author',
        'comment': 'Comment',
        'date_created': 'DateCreated',
        'community_rating': 'CommunityRating',
        'download_count': 'DownloadCount',
        'is_hash_match': 'IsHashMatch',
        'is_forced': 'IsForced',
        'language': 'Language'
    }

    def __init__(self, three_letter_iso_language_name=None, id=None, provider_name=None, name=None, format=None, author=None, comment=None, date_created=None, community_rating=None, download_count=None, is_hash_match=None, is_forced=None, language=None):  # noqa: E501
        """RemoteSubtitleInfo - a model defined in Swagger"""  # noqa: E501
        self._three_letter_iso_language_name = None
        self._id = None
        self._provider_name = None
        self._name = None
        self._format = None
        self._author = None
        self._comment = None
        self._date_created = None
        self._community_rating = None
        self._download_count = None
        self._is_hash_match = None
        self._is_forced = None
        self._language = None
        self.discriminator = None
        if three_letter_iso_language_name is not None:
            self.three_letter_iso_language_name = three_letter_iso_language_name
        if id is not None:
            self.id = id
        if provider_name is not None:
            self.provider_name = provider_name
        if name is not None:
            self.name = name
        if format is not None:
            self.format = format
        if author is not None:
            self.author = author
        if comment is not None:
            self.comment = comment
        if date_created is not None:
            self.date_created = date_created
        if community_rating is not None:
            self.community_rating = community_rating
        if download_count is not None:
            self.download_count = download_count
        if is_hash_match is not None:
            self.is_hash_match = is_hash_match
        if is_forced is not None:
            self.is_forced = is_forced
        if language is not None:
            self.language = language

    @property
    def three_letter_iso_language_name(self):
        """Gets the three_letter_iso_language_name of this RemoteSubtitleInfo.  # noqa: E501


        :return: The three_letter_iso_language_name of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_iso_language_name

    @three_letter_iso_language_name.setter
    def three_letter_iso_language_name(self, three_letter_iso_language_name):
        """Sets the three_letter_iso_language_name of this RemoteSubtitleInfo.


        :param three_letter_iso_language_name: The three_letter_iso_language_name of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._three_letter_iso_language_name = three_letter_iso_language_name

    @property
    def id(self):
        """Gets the id of this RemoteSubtitleInfo.  # noqa: E501


        :return: The id of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteSubtitleInfo.


        :param id: The id of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def provider_name(self):
        """Gets the provider_name of this RemoteSubtitleInfo.  # noqa: E501


        :return: The provider_name of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this RemoteSubtitleInfo.


        :param provider_name: The provider_name of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def name(self):
        """Gets the name of this RemoteSubtitleInfo.  # noqa: E501


        :return: The name of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RemoteSubtitleInfo.


        :param name: The name of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format(self):
        """Gets the format of this RemoteSubtitleInfo.  # noqa: E501


        :return: The format of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RemoteSubtitleInfo.


        :param format: The format of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def author(self):
        """Gets the author of this RemoteSubtitleInfo.  # noqa: E501


        :return: The author of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this RemoteSubtitleInfo.


        :param author: The author of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def comment(self):
        """Gets the comment of this RemoteSubtitleInfo.  # noqa: E501


        :return: The comment of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this RemoteSubtitleInfo.


        :param comment: The comment of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def date_created(self):
        """Gets the date_created of this RemoteSubtitleInfo.  # noqa: E501


        :return: The date_created of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RemoteSubtitleInfo.


        :param date_created: The date_created of this RemoteSubtitleInfo.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def community_rating(self):
        """Gets the community_rating of this RemoteSubtitleInfo.  # noqa: E501


        :return: The community_rating of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: float
        """
        return self._community_rating

    @community_rating.setter
    def community_rating(self, community_rating):
        """Sets the community_rating of this RemoteSubtitleInfo.


        :param community_rating: The community_rating of this RemoteSubtitleInfo.  # noqa: E501
        :type: float
        """

        self._community_rating = community_rating

    @property
    def download_count(self):
        """Gets the download_count of this RemoteSubtitleInfo.  # noqa: E501


        :return: The download_count of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """Sets the download_count of this RemoteSubtitleInfo.


        :param download_count: The download_count of this RemoteSubtitleInfo.  # noqa: E501
        :type: int
        """

        self._download_count = download_count

    @property
    def is_hash_match(self):
        """Gets the is_hash_match of this RemoteSubtitleInfo.  # noqa: E501


        :return: The is_hash_match of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_hash_match

    @is_hash_match.setter
    def is_hash_match(self, is_hash_match):
        """Sets the is_hash_match of this RemoteSubtitleInfo.


        :param is_hash_match: The is_hash_match of this RemoteSubtitleInfo.  # noqa: E501
        :type: bool
        """

        self._is_hash_match = is_hash_match

    @property
    def is_forced(self):
        """Gets the is_forced of this RemoteSubtitleInfo.  # noqa: E501


        :return: The is_forced of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_forced

    @is_forced.setter
    def is_forced(self, is_forced):
        """Sets the is_forced of this RemoteSubtitleInfo.


        :param is_forced: The is_forced of this RemoteSubtitleInfo.  # noqa: E501
        :type: bool
        """

        self._is_forced = is_forced

    @property
    def language(self):
        """Gets the language of this RemoteSubtitleInfo.  # noqa: E501


        :return: The language of this RemoteSubtitleInfo.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RemoteSubtitleInfo.


        :param language: The language of this RemoteSubtitleInfo.  # noqa: E501
        :type: str
        """

        self._language = language

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
        if issubclass(RemoteSubtitleInfo, dict):
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
        if not isinstance(other, RemoteSubtitleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
