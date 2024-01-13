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

class SessionSessionInfo(object):
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
        'play_state': 'PlayerStateInfo',
        'additional_users': 'list[SessionUserInfo]',
        'remote_end_point': 'str',
        'playable_media_types': 'list[str]',
        'playlist_item_id': 'str',
        'playlist_index': 'int',
        'playlist_length': 'int',
        'id': 'str',
        'server_id': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_primary_image_tag': 'str',
        'client': 'str',
        'last_activity_date': 'datetime',
        'device_name': 'str',
        'device_type': 'str',
        'now_playing_item': 'BaseItemDto',
        'device_id': 'str',
        'application_version': 'str',
        'app_icon_url': 'str',
        'supported_commands': 'list[str]',
        'transcoding_info': 'TranscodingInfo',
        'supports_remote_control': 'bool'
    }

    attribute_map = {
        'play_state': 'PlayState',
        'additional_users': 'AdditionalUsers',
        'remote_end_point': 'RemoteEndPoint',
        'playable_media_types': 'PlayableMediaTypes',
        'playlist_item_id': 'PlaylistItemId',
        'playlist_index': 'PlaylistIndex',
        'playlist_length': 'PlaylistLength',
        'id': 'Id',
        'server_id': 'ServerId',
        'user_id': 'UserId',
        'user_name': 'UserName',
        'user_primary_image_tag': 'UserPrimaryImageTag',
        'client': 'Client',
        'last_activity_date': 'LastActivityDate',
        'device_name': 'DeviceName',
        'device_type': 'DeviceType',
        'now_playing_item': 'NowPlayingItem',
        'device_id': 'DeviceId',
        'application_version': 'ApplicationVersion',
        'app_icon_url': 'AppIconUrl',
        'supported_commands': 'SupportedCommands',
        'transcoding_info': 'TranscodingInfo',
        'supports_remote_control': 'SupportsRemoteControl'
    }

    def __init__(self, play_state=None, additional_users=None, remote_end_point=None, playable_media_types=None, playlist_item_id=None, playlist_index=None, playlist_length=None, id=None, server_id=None, user_id=None, user_name=None, user_primary_image_tag=None, client=None, last_activity_date=None, device_name=None, device_type=None, now_playing_item=None, device_id=None, application_version=None, app_icon_url=None, supported_commands=None, transcoding_info=None, supports_remote_control=None):  # noqa: E501
        """SessionSessionInfo - a model defined in Swagger"""  # noqa: E501
        self._play_state = None
        self._additional_users = None
        self._remote_end_point = None
        self._playable_media_types = None
        self._playlist_item_id = None
        self._playlist_index = None
        self._playlist_length = None
        self._id = None
        self._server_id = None
        self._user_id = None
        self._user_name = None
        self._user_primary_image_tag = None
        self._client = None
        self._last_activity_date = None
        self._device_name = None
        self._device_type = None
        self._now_playing_item = None
        self._device_id = None
        self._application_version = None
        self._app_icon_url = None
        self._supported_commands = None
        self._transcoding_info = None
        self._supports_remote_control = None
        self.discriminator = None
        if play_state is not None:
            self.play_state = play_state
        if additional_users is not None:
            self.additional_users = additional_users
        if remote_end_point is not None:
            self.remote_end_point = remote_end_point
        if playable_media_types is not None:
            self.playable_media_types = playable_media_types
        if playlist_item_id is not None:
            self.playlist_item_id = playlist_item_id
        if playlist_index is not None:
            self.playlist_index = playlist_index
        if playlist_length is not None:
            self.playlist_length = playlist_length
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_primary_image_tag is not None:
            self.user_primary_image_tag = user_primary_image_tag
        if client is not None:
            self.client = client
        if last_activity_date is not None:
            self.last_activity_date = last_activity_date
        if device_name is not None:
            self.device_name = device_name
        if device_type is not None:
            self.device_type = device_type
        if now_playing_item is not None:
            self.now_playing_item = now_playing_item
        if device_id is not None:
            self.device_id = device_id
        if application_version is not None:
            self.application_version = application_version
        if app_icon_url is not None:
            self.app_icon_url = app_icon_url
        if supported_commands is not None:
            self.supported_commands = supported_commands
        if transcoding_info is not None:
            self.transcoding_info = transcoding_info
        if supports_remote_control is not None:
            self.supports_remote_control = supports_remote_control

    @property
    def play_state(self):
        """Gets the play_state of this SessionSessionInfo.  # noqa: E501


        :return: The play_state of this SessionSessionInfo.  # noqa: E501
        :rtype: PlayerStateInfo
        """
        return self._play_state

    @play_state.setter
    def play_state(self, play_state):
        """Sets the play_state of this SessionSessionInfo.


        :param play_state: The play_state of this SessionSessionInfo.  # noqa: E501
        :type: PlayerStateInfo
        """

        self._play_state = play_state

    @property
    def additional_users(self):
        """Gets the additional_users of this SessionSessionInfo.  # noqa: E501


        :return: The additional_users of this SessionSessionInfo.  # noqa: E501
        :rtype: list[SessionUserInfo]
        """
        return self._additional_users

    @additional_users.setter
    def additional_users(self, additional_users):
        """Sets the additional_users of this SessionSessionInfo.


        :param additional_users: The additional_users of this SessionSessionInfo.  # noqa: E501
        :type: list[SessionUserInfo]
        """

        self._additional_users = additional_users

    @property
    def remote_end_point(self):
        """Gets the remote_end_point of this SessionSessionInfo.  # noqa: E501


        :return: The remote_end_point of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._remote_end_point

    @remote_end_point.setter
    def remote_end_point(self, remote_end_point):
        """Sets the remote_end_point of this SessionSessionInfo.


        :param remote_end_point: The remote_end_point of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._remote_end_point = remote_end_point

    @property
    def playable_media_types(self):
        """Gets the playable_media_types of this SessionSessionInfo.  # noqa: E501


        :return: The playable_media_types of this SessionSessionInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._playable_media_types

    @playable_media_types.setter
    def playable_media_types(self, playable_media_types):
        """Sets the playable_media_types of this SessionSessionInfo.


        :param playable_media_types: The playable_media_types of this SessionSessionInfo.  # noqa: E501
        :type: list[str]
        """

        self._playable_media_types = playable_media_types

    @property
    def playlist_item_id(self):
        """Gets the playlist_item_id of this SessionSessionInfo.  # noqa: E501


        :return: The playlist_item_id of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._playlist_item_id

    @playlist_item_id.setter
    def playlist_item_id(self, playlist_item_id):
        """Sets the playlist_item_id of this SessionSessionInfo.


        :param playlist_item_id: The playlist_item_id of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._playlist_item_id = playlist_item_id

    @property
    def playlist_index(self):
        """Gets the playlist_index of this SessionSessionInfo.  # noqa: E501


        :return: The playlist_index of this SessionSessionInfo.  # noqa: E501
        :rtype: int
        """
        return self._playlist_index

    @playlist_index.setter
    def playlist_index(self, playlist_index):
        """Sets the playlist_index of this SessionSessionInfo.


        :param playlist_index: The playlist_index of this SessionSessionInfo.  # noqa: E501
        :type: int
        """

        self._playlist_index = playlist_index

    @property
    def playlist_length(self):
        """Gets the playlist_length of this SessionSessionInfo.  # noqa: E501


        :return: The playlist_length of this SessionSessionInfo.  # noqa: E501
        :rtype: int
        """
        return self._playlist_length

    @playlist_length.setter
    def playlist_length(self, playlist_length):
        """Sets the playlist_length of this SessionSessionInfo.


        :param playlist_length: The playlist_length of this SessionSessionInfo.  # noqa: E501
        :type: int
        """

        self._playlist_length = playlist_length

    @property
    def id(self):
        """Gets the id of this SessionSessionInfo.  # noqa: E501


        :return: The id of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionSessionInfo.


        :param id: The id of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this SessionSessionInfo.  # noqa: E501


        :return: The server_id of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this SessionSessionInfo.


        :param server_id: The server_id of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def user_id(self):
        """Gets the user_id of this SessionSessionInfo.  # noqa: E501


        :return: The user_id of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SessionSessionInfo.


        :param user_id: The user_id of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this SessionSessionInfo.  # noqa: E501


        :return: The user_name of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SessionSessionInfo.


        :param user_name: The user_name of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_primary_image_tag(self):
        """Gets the user_primary_image_tag of this SessionSessionInfo.  # noqa: E501


        :return: The user_primary_image_tag of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_primary_image_tag

    @user_primary_image_tag.setter
    def user_primary_image_tag(self, user_primary_image_tag):
        """Sets the user_primary_image_tag of this SessionSessionInfo.


        :param user_primary_image_tag: The user_primary_image_tag of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._user_primary_image_tag = user_primary_image_tag

    @property
    def client(self):
        """Gets the client of this SessionSessionInfo.  # noqa: E501


        :return: The client of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this SessionSessionInfo.


        :param client: The client of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._client = client

    @property
    def last_activity_date(self):
        """Gets the last_activity_date of this SessionSessionInfo.  # noqa: E501


        :return: The last_activity_date of this SessionSessionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity_date

    @last_activity_date.setter
    def last_activity_date(self, last_activity_date):
        """Sets the last_activity_date of this SessionSessionInfo.


        :param last_activity_date: The last_activity_date of this SessionSessionInfo.  # noqa: E501
        :type: datetime
        """

        self._last_activity_date = last_activity_date

    @property
    def device_name(self):
        """Gets the device_name of this SessionSessionInfo.  # noqa: E501


        :return: The device_name of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this SessionSessionInfo.


        :param device_name: The device_name of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def device_type(self):
        """Gets the device_type of this SessionSessionInfo.  # noqa: E501


        :return: The device_type of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this SessionSessionInfo.


        :param device_type: The device_type of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def now_playing_item(self):
        """Gets the now_playing_item of this SessionSessionInfo.  # noqa: E501


        :return: The now_playing_item of this SessionSessionInfo.  # noqa: E501
        :rtype: BaseItemDto
        """
        return self._now_playing_item

    @now_playing_item.setter
    def now_playing_item(self, now_playing_item):
        """Sets the now_playing_item of this SessionSessionInfo.


        :param now_playing_item: The now_playing_item of this SessionSessionInfo.  # noqa: E501
        :type: BaseItemDto
        """

        self._now_playing_item = now_playing_item

    @property
    def device_id(self):
        """Gets the device_id of this SessionSessionInfo.  # noqa: E501


        :return: The device_id of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SessionSessionInfo.


        :param device_id: The device_id of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def application_version(self):
        """Gets the application_version of this SessionSessionInfo.  # noqa: E501


        :return: The application_version of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this SessionSessionInfo.


        :param application_version: The application_version of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._application_version = application_version

    @property
    def app_icon_url(self):
        """Gets the app_icon_url of this SessionSessionInfo.  # noqa: E501


        :return: The app_icon_url of this SessionSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        """Sets the app_icon_url of this SessionSessionInfo.


        :param app_icon_url: The app_icon_url of this SessionSessionInfo.  # noqa: E501
        :type: str
        """

        self._app_icon_url = app_icon_url

    @property
    def supported_commands(self):
        """Gets the supported_commands of this SessionSessionInfo.  # noqa: E501


        :return: The supported_commands of this SessionSessionInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_commands

    @supported_commands.setter
    def supported_commands(self, supported_commands):
        """Sets the supported_commands of this SessionSessionInfo.


        :param supported_commands: The supported_commands of this SessionSessionInfo.  # noqa: E501
        :type: list[str]
        """

        self._supported_commands = supported_commands

    @property
    def transcoding_info(self):
        """Gets the transcoding_info of this SessionSessionInfo.  # noqa: E501


        :return: The transcoding_info of this SessionSessionInfo.  # noqa: E501
        :rtype: TranscodingInfo
        """
        return self._transcoding_info

    @transcoding_info.setter
    def transcoding_info(self, transcoding_info):
        """Sets the transcoding_info of this SessionSessionInfo.


        :param transcoding_info: The transcoding_info of this SessionSessionInfo.  # noqa: E501
        :type: TranscodingInfo
        """

        self._transcoding_info = transcoding_info

    @property
    def supports_remote_control(self):
        """Gets the supports_remote_control of this SessionSessionInfo.  # noqa: E501


        :return: The supports_remote_control of this SessionSessionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._supports_remote_control

    @supports_remote_control.setter
    def supports_remote_control(self, supports_remote_control):
        """Sets the supports_remote_control of this SessionSessionInfo.


        :param supports_remote_control: The supports_remote_control of this SessionSessionInfo.  # noqa: E501
        :type: bool
        """

        self._supports_remote_control = supports_remote_control

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
        if issubclass(SessionSessionInfo, dict):
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
        if not isinstance(other, SessionSessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
