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

class SyncModelSyncJobRequest(object):
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
        'target_id': 'str',
        'item_ids': 'list[str]',
        'category': 'str',
        'parent_id': 'str',
        'quality': 'str',
        'profile': 'str',
        'container': 'str',
        'video_codec': 'str',
        'audio_codec': 'str',
        'name': 'str',
        'user_id': 'str',
        'unwatched_only': 'bool',
        'sync_new_content': 'bool',
        'item_limit': 'int',
        'bitrate': 'int',
        'downloaded': 'bool'
    }

    attribute_map = {
        'target_id': 'TargetId',
        'item_ids': 'ItemIds',
        'category': 'Category',
        'parent_id': 'ParentId',
        'quality': 'Quality',
        'profile': 'Profile',
        'container': 'Container',
        'video_codec': 'VideoCodec',
        'audio_codec': 'AudioCodec',
        'name': 'Name',
        'user_id': 'UserId',
        'unwatched_only': 'UnwatchedOnly',
        'sync_new_content': 'SyncNewContent',
        'item_limit': 'ItemLimit',
        'bitrate': 'Bitrate',
        'downloaded': 'Downloaded'
    }

    def __init__(self, target_id=None, item_ids=None, category=None, parent_id=None, quality=None, profile=None, container=None, video_codec=None, audio_codec=None, name=None, user_id=None, unwatched_only=None, sync_new_content=None, item_limit=None, bitrate=None, downloaded=None):  # noqa: E501
        """SyncModelSyncJobRequest - a model defined in Swagger"""  # noqa: E501
        self._target_id = None
        self._item_ids = None
        self._category = None
        self._parent_id = None
        self._quality = None
        self._profile = None
        self._container = None
        self._video_codec = None
        self._audio_codec = None
        self._name = None
        self._user_id = None
        self._unwatched_only = None
        self._sync_new_content = None
        self._item_limit = None
        self._bitrate = None
        self._downloaded = None
        self.discriminator = None
        if target_id is not None:
            self.target_id = target_id
        if item_ids is not None:
            self.item_ids = item_ids
        if category is not None:
            self.category = category
        if parent_id is not None:
            self.parent_id = parent_id
        if quality is not None:
            self.quality = quality
        if profile is not None:
            self.profile = profile
        if container is not None:
            self.container = container
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id
        if unwatched_only is not None:
            self.unwatched_only = unwatched_only
        if sync_new_content is not None:
            self.sync_new_content = sync_new_content
        if item_limit is not None:
            self.item_limit = item_limit
        if bitrate is not None:
            self.bitrate = bitrate
        if downloaded is not None:
            self.downloaded = downloaded

    @property
    def target_id(self):
        """Gets the target_id of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The target_id of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this SyncModelSyncJobRequest.


        :param target_id: The target_id of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def item_ids(self):
        """Gets the item_ids of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The item_ids of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this SyncModelSyncJobRequest.


        :param item_ids: The item_ids of this SyncModelSyncJobRequest.  # noqa: E501
        :type: list[str]
        """

        self._item_ids = item_ids

    @property
    def category(self):
        """Gets the category of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The category of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SyncModelSyncJobRequest.


        :param category: The category of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Latest", "NextUp", "Resume"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def parent_id(self):
        """Gets the parent_id of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The parent_id of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SyncModelSyncJobRequest.


        :param parent_id: The parent_id of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def quality(self):
        """Gets the quality of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The quality of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this SyncModelSyncJobRequest.


        :param quality: The quality of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._quality = quality

    @property
    def profile(self):
        """Gets the profile of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The profile of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SyncModelSyncJobRequest.


        :param profile: The profile of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._profile = profile

    @property
    def container(self):
        """Gets the container of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The container of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this SyncModelSyncJobRequest.


        :param container: The container of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def video_codec(self):
        """Gets the video_codec of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The video_codec of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this SyncModelSyncJobRequest.


        :param video_codec: The video_codec of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The audio_codec of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this SyncModelSyncJobRequest.


        :param audio_codec: The audio_codec of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._audio_codec = audio_codec

    @property
    def name(self):
        """Gets the name of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The name of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SyncModelSyncJobRequest.


        :param name: The name of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The user_id of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SyncModelSyncJobRequest.


        :param user_id: The user_id of this SyncModelSyncJobRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def unwatched_only(self):
        """Gets the unwatched_only of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The unwatched_only of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unwatched_only

    @unwatched_only.setter
    def unwatched_only(self, unwatched_only):
        """Sets the unwatched_only of this SyncModelSyncJobRequest.


        :param unwatched_only: The unwatched_only of this SyncModelSyncJobRequest.  # noqa: E501
        :type: bool
        """

        self._unwatched_only = unwatched_only

    @property
    def sync_new_content(self):
        """Gets the sync_new_content of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The sync_new_content of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sync_new_content

    @sync_new_content.setter
    def sync_new_content(self, sync_new_content):
        """Sets the sync_new_content of this SyncModelSyncJobRequest.


        :param sync_new_content: The sync_new_content of this SyncModelSyncJobRequest.  # noqa: E501
        :type: bool
        """

        self._sync_new_content = sync_new_content

    @property
    def item_limit(self):
        """Gets the item_limit of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The item_limit of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_limit

    @item_limit.setter
    def item_limit(self, item_limit):
        """Sets the item_limit of this SyncModelSyncJobRequest.


        :param item_limit: The item_limit of this SyncModelSyncJobRequest.  # noqa: E501
        :type: int
        """

        self._item_limit = item_limit

    @property
    def bitrate(self):
        """Gets the bitrate of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The bitrate of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this SyncModelSyncJobRequest.


        :param bitrate: The bitrate of this SyncModelSyncJobRequest.  # noqa: E501
        :type: int
        """

        self._bitrate = bitrate

    @property
    def downloaded(self):
        """Gets the downloaded of this SyncModelSyncJobRequest.  # noqa: E501


        :return: The downloaded of this SyncModelSyncJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._downloaded

    @downloaded.setter
    def downloaded(self, downloaded):
        """Sets the downloaded of this SyncModelSyncJobRequest.


        :param downloaded: The downloaded of this SyncModelSyncJobRequest.  # noqa: E501
        :type: bool
        """

        self._downloaded = downloaded

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
        if issubclass(SyncModelSyncJobRequest, dict):
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
        if not isinstance(other, SyncModelSyncJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
