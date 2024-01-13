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

class EmbyDlnaProfilesDlnaProfile(object):
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
        'type': 'EmbyDlnaProfilesDeviceProfileType',
        'path': 'str',
        'user_id': 'str',
        'album_art_pn': 'str',
        'max_album_art_width': 'int',
        'max_album_art_height': 'int',
        'max_icon_width': 'int',
        'max_icon_height': 'int',
        'friendly_name': 'str',
        'manufacturer': 'str',
        'manufacturer_url': 'str',
        'model_name': 'str',
        'model_description': 'str',
        'model_number': 'str',
        'model_url': 'str',
        'serial_number': 'str',
        'enable_album_art_in_didl': 'bool',
        'enable_single_album_art_limit': 'bool',
        'enable_single_subtitle_limit': 'bool',
        'protocol_info': 'str',
        'timeline_offset_seconds': 'int',
        'requires_plain_video_items': 'bool',
        'requires_plain_folders': 'bool',
        'ignore_transcode_byte_range_requests': 'bool',
        'supports_samsung_bookmark': 'bool',
        'identification': 'EmbyDlnaProfilesDeviceIdentification',
        'protocol_info_detection': 'EmbyDlnaProfilesProtocolInfoDetection',
        'name': 'str',
        'id': 'str',
        'supported_media_types': 'str',
        'max_streaming_bitrate': 'int',
        'music_streaming_transcoding_bitrate': 'int',
        'max_static_music_bitrate': 'int',
        'direct_play_profiles': 'list[DlnaDirectPlayProfile]',
        'transcoding_profiles': 'list[DlnaTranscodingProfile]',
        'container_profiles': 'list[DlnaContainerProfile]',
        'codec_profiles': 'list[DlnaCodecProfile]',
        'response_profiles': 'list[DlnaResponseProfile]',
        'subtitle_profiles': 'list[DlnaSubtitleProfile]'
    }

    attribute_map = {
        'type': 'Type',
        'path': 'Path',
        'user_id': 'UserId',
        'album_art_pn': 'AlbumArtPn',
        'max_album_art_width': 'MaxAlbumArtWidth',
        'max_album_art_height': 'MaxAlbumArtHeight',
        'max_icon_width': 'MaxIconWidth',
        'max_icon_height': 'MaxIconHeight',
        'friendly_name': 'FriendlyName',
        'manufacturer': 'Manufacturer',
        'manufacturer_url': 'ManufacturerUrl',
        'model_name': 'ModelName',
        'model_description': 'ModelDescription',
        'model_number': 'ModelNumber',
        'model_url': 'ModelUrl',
        'serial_number': 'SerialNumber',
        'enable_album_art_in_didl': 'EnableAlbumArtInDidl',
        'enable_single_album_art_limit': 'EnableSingleAlbumArtLimit',
        'enable_single_subtitle_limit': 'EnableSingleSubtitleLimit',
        'protocol_info': 'ProtocolInfo',
        'timeline_offset_seconds': 'TimelineOffsetSeconds',
        'requires_plain_video_items': 'RequiresPlainVideoItems',
        'requires_plain_folders': 'RequiresPlainFolders',
        'ignore_transcode_byte_range_requests': 'IgnoreTranscodeByteRangeRequests',
        'supports_samsung_bookmark': 'SupportsSamsungBookmark',
        'identification': 'Identification',
        'protocol_info_detection': 'ProtocolInfoDetection',
        'name': 'Name',
        'id': 'Id',
        'supported_media_types': 'SupportedMediaTypes',
        'max_streaming_bitrate': 'MaxStreamingBitrate',
        'music_streaming_transcoding_bitrate': 'MusicStreamingTranscodingBitrate',
        'max_static_music_bitrate': 'MaxStaticMusicBitrate',
        'direct_play_profiles': 'DirectPlayProfiles',
        'transcoding_profiles': 'TranscodingProfiles',
        'container_profiles': 'ContainerProfiles',
        'codec_profiles': 'CodecProfiles',
        'response_profiles': 'ResponseProfiles',
        'subtitle_profiles': 'SubtitleProfiles'
    }

    def __init__(self, type=None, path=None, user_id=None, album_art_pn=None, max_album_art_width=None, max_album_art_height=None, max_icon_width=None, max_icon_height=None, friendly_name=None, manufacturer=None, manufacturer_url=None, model_name=None, model_description=None, model_number=None, model_url=None, serial_number=None, enable_album_art_in_didl=None, enable_single_album_art_limit=None, enable_single_subtitle_limit=None, protocol_info=None, timeline_offset_seconds=None, requires_plain_video_items=None, requires_plain_folders=None, ignore_transcode_byte_range_requests=None, supports_samsung_bookmark=None, identification=None, protocol_info_detection=None, name=None, id=None, supported_media_types=None, max_streaming_bitrate=None, music_streaming_transcoding_bitrate=None, max_static_music_bitrate=None, direct_play_profiles=None, transcoding_profiles=None, container_profiles=None, codec_profiles=None, response_profiles=None, subtitle_profiles=None):  # noqa: E501
        """EmbyDlnaProfilesDlnaProfile - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._path = None
        self._user_id = None
        self._album_art_pn = None
        self._max_album_art_width = None
        self._max_album_art_height = None
        self._max_icon_width = None
        self._max_icon_height = None
        self._friendly_name = None
        self._manufacturer = None
        self._manufacturer_url = None
        self._model_name = None
        self._model_description = None
        self._model_number = None
        self._model_url = None
        self._serial_number = None
        self._enable_album_art_in_didl = None
        self._enable_single_album_art_limit = None
        self._enable_single_subtitle_limit = None
        self._protocol_info = None
        self._timeline_offset_seconds = None
        self._requires_plain_video_items = None
        self._requires_plain_folders = None
        self._ignore_transcode_byte_range_requests = None
        self._supports_samsung_bookmark = None
        self._identification = None
        self._protocol_info_detection = None
        self._name = None
        self._id = None
        self._supported_media_types = None
        self._max_streaming_bitrate = None
        self._music_streaming_transcoding_bitrate = None
        self._max_static_music_bitrate = None
        self._direct_play_profiles = None
        self._transcoding_profiles = None
        self._container_profiles = None
        self._codec_profiles = None
        self._response_profiles = None
        self._subtitle_profiles = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if user_id is not None:
            self.user_id = user_id
        if album_art_pn is not None:
            self.album_art_pn = album_art_pn
        if max_album_art_width is not None:
            self.max_album_art_width = max_album_art_width
        if max_album_art_height is not None:
            self.max_album_art_height = max_album_art_height
        if max_icon_width is not None:
            self.max_icon_width = max_icon_width
        if max_icon_height is not None:
            self.max_icon_height = max_icon_height
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_url is not None:
            self.manufacturer_url = manufacturer_url
        if model_name is not None:
            self.model_name = model_name
        if model_description is not None:
            self.model_description = model_description
        if model_number is not None:
            self.model_number = model_number
        if model_url is not None:
            self.model_url = model_url
        if serial_number is not None:
            self.serial_number = serial_number
        if enable_album_art_in_didl is not None:
            self.enable_album_art_in_didl = enable_album_art_in_didl
        if enable_single_album_art_limit is not None:
            self.enable_single_album_art_limit = enable_single_album_art_limit
        if enable_single_subtitle_limit is not None:
            self.enable_single_subtitle_limit = enable_single_subtitle_limit
        if protocol_info is not None:
            self.protocol_info = protocol_info
        if timeline_offset_seconds is not None:
            self.timeline_offset_seconds = timeline_offset_seconds
        if requires_plain_video_items is not None:
            self.requires_plain_video_items = requires_plain_video_items
        if requires_plain_folders is not None:
            self.requires_plain_folders = requires_plain_folders
        if ignore_transcode_byte_range_requests is not None:
            self.ignore_transcode_byte_range_requests = ignore_transcode_byte_range_requests
        if supports_samsung_bookmark is not None:
            self.supports_samsung_bookmark = supports_samsung_bookmark
        if identification is not None:
            self.identification = identification
        if protocol_info_detection is not None:
            self.protocol_info_detection = protocol_info_detection
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if supported_media_types is not None:
            self.supported_media_types = supported_media_types
        if max_streaming_bitrate is not None:
            self.max_streaming_bitrate = max_streaming_bitrate
        if music_streaming_transcoding_bitrate is not None:
            self.music_streaming_transcoding_bitrate = music_streaming_transcoding_bitrate
        if max_static_music_bitrate is not None:
            self.max_static_music_bitrate = max_static_music_bitrate
        if direct_play_profiles is not None:
            self.direct_play_profiles = direct_play_profiles
        if transcoding_profiles is not None:
            self.transcoding_profiles = transcoding_profiles
        if container_profiles is not None:
            self.container_profiles = container_profiles
        if codec_profiles is not None:
            self.codec_profiles = codec_profiles
        if response_profiles is not None:
            self.response_profiles = response_profiles
        if subtitle_profiles is not None:
            self.subtitle_profiles = subtitle_profiles

    @property
    def type(self):
        """Gets the type of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The type of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: EmbyDlnaProfilesDeviceProfileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmbyDlnaProfilesDlnaProfile.


        :param type: The type of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: EmbyDlnaProfilesDeviceProfileType
        """

        self._type = type

    @property
    def path(self):
        """Gets the path of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The path of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this EmbyDlnaProfilesDlnaProfile.


        :param path: The path of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def user_id(self):
        """Gets the user_id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The user_id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EmbyDlnaProfilesDlnaProfile.


        :param user_id: The user_id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def album_art_pn(self):
        """Gets the album_art_pn of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The album_art_pn of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._album_art_pn

    @album_art_pn.setter
    def album_art_pn(self, album_art_pn):
        """Sets the album_art_pn of this EmbyDlnaProfilesDlnaProfile.


        :param album_art_pn: The album_art_pn of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._album_art_pn = album_art_pn

    @property
    def max_album_art_width(self):
        """Gets the max_album_art_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_album_art_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_album_art_width

    @max_album_art_width.setter
    def max_album_art_width(self, max_album_art_width):
        """Sets the max_album_art_width of this EmbyDlnaProfilesDlnaProfile.


        :param max_album_art_width: The max_album_art_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_album_art_width = max_album_art_width

    @property
    def max_album_art_height(self):
        """Gets the max_album_art_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_album_art_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_album_art_height

    @max_album_art_height.setter
    def max_album_art_height(self, max_album_art_height):
        """Sets the max_album_art_height of this EmbyDlnaProfilesDlnaProfile.


        :param max_album_art_height: The max_album_art_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_album_art_height = max_album_art_height

    @property
    def max_icon_width(self):
        """Gets the max_icon_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_icon_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_icon_width

    @max_icon_width.setter
    def max_icon_width(self, max_icon_width):
        """Sets the max_icon_width of this EmbyDlnaProfilesDlnaProfile.


        :param max_icon_width: The max_icon_width of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_icon_width = max_icon_width

    @property
    def max_icon_height(self):
        """Gets the max_icon_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_icon_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_icon_height

    @max_icon_height.setter
    def max_icon_height(self, max_icon_height):
        """Sets the max_icon_height of this EmbyDlnaProfilesDlnaProfile.


        :param max_icon_height: The max_icon_height of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_icon_height = max_icon_height

    @property
    def friendly_name(self):
        """Gets the friendly_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The friendly_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this EmbyDlnaProfilesDlnaProfile.


        :param friendly_name: The friendly_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The manufacturer of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this EmbyDlnaProfilesDlnaProfile.


        :param manufacturer: The manufacturer of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_url(self):
        """Gets the manufacturer_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The manufacturer_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_url

    @manufacturer_url.setter
    def manufacturer_url(self, manufacturer_url):
        """Sets the manufacturer_url of this EmbyDlnaProfilesDlnaProfile.


        :param manufacturer_url: The manufacturer_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._manufacturer_url = manufacturer_url

    @property
    def model_name(self):
        """Gets the model_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The model_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this EmbyDlnaProfilesDlnaProfile.


        :param model_name: The model_name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def model_description(self):
        """Gets the model_description of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The model_description of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._model_description

    @model_description.setter
    def model_description(self, model_description):
        """Sets the model_description of this EmbyDlnaProfilesDlnaProfile.


        :param model_description: The model_description of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._model_description = model_description

    @property
    def model_number(self):
        """Gets the model_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The model_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this EmbyDlnaProfilesDlnaProfile.


        :param model_number: The model_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._model_number = model_number

    @property
    def model_url(self):
        """Gets the model_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The model_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._model_url

    @model_url.setter
    def model_url(self, model_url):
        """Sets the model_url of this EmbyDlnaProfilesDlnaProfile.


        :param model_url: The model_url of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._model_url = model_url

    @property
    def serial_number(self):
        """Gets the serial_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The serial_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this EmbyDlnaProfilesDlnaProfile.


        :param serial_number: The serial_number of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def enable_album_art_in_didl(self):
        """Gets the enable_album_art_in_didl of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The enable_album_art_in_didl of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_album_art_in_didl

    @enable_album_art_in_didl.setter
    def enable_album_art_in_didl(self, enable_album_art_in_didl):
        """Sets the enable_album_art_in_didl of this EmbyDlnaProfilesDlnaProfile.


        :param enable_album_art_in_didl: The enable_album_art_in_didl of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._enable_album_art_in_didl = enable_album_art_in_didl

    @property
    def enable_single_album_art_limit(self):
        """Gets the enable_single_album_art_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The enable_single_album_art_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_single_album_art_limit

    @enable_single_album_art_limit.setter
    def enable_single_album_art_limit(self, enable_single_album_art_limit):
        """Sets the enable_single_album_art_limit of this EmbyDlnaProfilesDlnaProfile.


        :param enable_single_album_art_limit: The enable_single_album_art_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._enable_single_album_art_limit = enable_single_album_art_limit

    @property
    def enable_single_subtitle_limit(self):
        """Gets the enable_single_subtitle_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The enable_single_subtitle_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_single_subtitle_limit

    @enable_single_subtitle_limit.setter
    def enable_single_subtitle_limit(self, enable_single_subtitle_limit):
        """Sets the enable_single_subtitle_limit of this EmbyDlnaProfilesDlnaProfile.


        :param enable_single_subtitle_limit: The enable_single_subtitle_limit of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._enable_single_subtitle_limit = enable_single_subtitle_limit

    @property
    def protocol_info(self):
        """Gets the protocol_info of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The protocol_info of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._protocol_info

    @protocol_info.setter
    def protocol_info(self, protocol_info):
        """Sets the protocol_info of this EmbyDlnaProfilesDlnaProfile.


        :param protocol_info: The protocol_info of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._protocol_info = protocol_info

    @property
    def timeline_offset_seconds(self):
        """Gets the timeline_offset_seconds of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The timeline_offset_seconds of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._timeline_offset_seconds

    @timeline_offset_seconds.setter
    def timeline_offset_seconds(self, timeline_offset_seconds):
        """Sets the timeline_offset_seconds of this EmbyDlnaProfilesDlnaProfile.


        :param timeline_offset_seconds: The timeline_offset_seconds of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._timeline_offset_seconds = timeline_offset_seconds

    @property
    def requires_plain_video_items(self):
        """Gets the requires_plain_video_items of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The requires_plain_video_items of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._requires_plain_video_items

    @requires_plain_video_items.setter
    def requires_plain_video_items(self, requires_plain_video_items):
        """Sets the requires_plain_video_items of this EmbyDlnaProfilesDlnaProfile.


        :param requires_plain_video_items: The requires_plain_video_items of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._requires_plain_video_items = requires_plain_video_items

    @property
    def requires_plain_folders(self):
        """Gets the requires_plain_folders of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The requires_plain_folders of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._requires_plain_folders

    @requires_plain_folders.setter
    def requires_plain_folders(self, requires_plain_folders):
        """Sets the requires_plain_folders of this EmbyDlnaProfilesDlnaProfile.


        :param requires_plain_folders: The requires_plain_folders of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._requires_plain_folders = requires_plain_folders

    @property
    def ignore_transcode_byte_range_requests(self):
        """Gets the ignore_transcode_byte_range_requests of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The ignore_transcode_byte_range_requests of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_transcode_byte_range_requests

    @ignore_transcode_byte_range_requests.setter
    def ignore_transcode_byte_range_requests(self, ignore_transcode_byte_range_requests):
        """Sets the ignore_transcode_byte_range_requests of this EmbyDlnaProfilesDlnaProfile.


        :param ignore_transcode_byte_range_requests: The ignore_transcode_byte_range_requests of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._ignore_transcode_byte_range_requests = ignore_transcode_byte_range_requests

    @property
    def supports_samsung_bookmark(self):
        """Gets the supports_samsung_bookmark of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The supports_samsung_bookmark of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: bool
        """
        return self._supports_samsung_bookmark

    @supports_samsung_bookmark.setter
    def supports_samsung_bookmark(self, supports_samsung_bookmark):
        """Sets the supports_samsung_bookmark of this EmbyDlnaProfilesDlnaProfile.


        :param supports_samsung_bookmark: The supports_samsung_bookmark of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: bool
        """

        self._supports_samsung_bookmark = supports_samsung_bookmark

    @property
    def identification(self):
        """Gets the identification of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The identification of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: EmbyDlnaProfilesDeviceIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this EmbyDlnaProfilesDlnaProfile.


        :param identification: The identification of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: EmbyDlnaProfilesDeviceIdentification
        """

        self._identification = identification

    @property
    def protocol_info_detection(self):
        """Gets the protocol_info_detection of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The protocol_info_detection of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: EmbyDlnaProfilesProtocolInfoDetection
        """
        return self._protocol_info_detection

    @protocol_info_detection.setter
    def protocol_info_detection(self, protocol_info_detection):
        """Sets the protocol_info_detection of this EmbyDlnaProfilesDlnaProfile.


        :param protocol_info_detection: The protocol_info_detection of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: EmbyDlnaProfilesProtocolInfoDetection
        """

        self._protocol_info_detection = protocol_info_detection

    @property
    def name(self):
        """Gets the name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmbyDlnaProfilesDlnaProfile.


        :param name: The name of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmbyDlnaProfilesDlnaProfile.


        :param id: The id of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def supported_media_types(self):
        """Gets the supported_media_types of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The supported_media_types of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: str
        """
        return self._supported_media_types

    @supported_media_types.setter
    def supported_media_types(self, supported_media_types):
        """Sets the supported_media_types of this EmbyDlnaProfilesDlnaProfile.


        :param supported_media_types: The supported_media_types of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: str
        """

        self._supported_media_types = supported_media_types

    @property
    def max_streaming_bitrate(self):
        """Gets the max_streaming_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_streaming_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_streaming_bitrate

    @max_streaming_bitrate.setter
    def max_streaming_bitrate(self, max_streaming_bitrate):
        """Sets the max_streaming_bitrate of this EmbyDlnaProfilesDlnaProfile.


        :param max_streaming_bitrate: The max_streaming_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_streaming_bitrate = max_streaming_bitrate

    @property
    def music_streaming_transcoding_bitrate(self):
        """Gets the music_streaming_transcoding_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The music_streaming_transcoding_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._music_streaming_transcoding_bitrate

    @music_streaming_transcoding_bitrate.setter
    def music_streaming_transcoding_bitrate(self, music_streaming_transcoding_bitrate):
        """Sets the music_streaming_transcoding_bitrate of this EmbyDlnaProfilesDlnaProfile.


        :param music_streaming_transcoding_bitrate: The music_streaming_transcoding_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._music_streaming_transcoding_bitrate = music_streaming_transcoding_bitrate

    @property
    def max_static_music_bitrate(self):
        """Gets the max_static_music_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The max_static_music_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_static_music_bitrate

    @max_static_music_bitrate.setter
    def max_static_music_bitrate(self, max_static_music_bitrate):
        """Sets the max_static_music_bitrate of this EmbyDlnaProfilesDlnaProfile.


        :param max_static_music_bitrate: The max_static_music_bitrate of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: int
        """

        self._max_static_music_bitrate = max_static_music_bitrate

    @property
    def direct_play_profiles(self):
        """Gets the direct_play_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The direct_play_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaDirectPlayProfile]
        """
        return self._direct_play_profiles

    @direct_play_profiles.setter
    def direct_play_profiles(self, direct_play_profiles):
        """Sets the direct_play_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param direct_play_profiles: The direct_play_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaDirectPlayProfile]
        """

        self._direct_play_profiles = direct_play_profiles

    @property
    def transcoding_profiles(self):
        """Gets the transcoding_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The transcoding_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaTranscodingProfile]
        """
        return self._transcoding_profiles

    @transcoding_profiles.setter
    def transcoding_profiles(self, transcoding_profiles):
        """Sets the transcoding_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param transcoding_profiles: The transcoding_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaTranscodingProfile]
        """

        self._transcoding_profiles = transcoding_profiles

    @property
    def container_profiles(self):
        """Gets the container_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The container_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaContainerProfile]
        """
        return self._container_profiles

    @container_profiles.setter
    def container_profiles(self, container_profiles):
        """Sets the container_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param container_profiles: The container_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaContainerProfile]
        """

        self._container_profiles = container_profiles

    @property
    def codec_profiles(self):
        """Gets the codec_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The codec_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaCodecProfile]
        """
        return self._codec_profiles

    @codec_profiles.setter
    def codec_profiles(self, codec_profiles):
        """Sets the codec_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param codec_profiles: The codec_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaCodecProfile]
        """

        self._codec_profiles = codec_profiles

    @property
    def response_profiles(self):
        """Gets the response_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The response_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaResponseProfile]
        """
        return self._response_profiles

    @response_profiles.setter
    def response_profiles(self, response_profiles):
        """Sets the response_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param response_profiles: The response_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaResponseProfile]
        """

        self._response_profiles = response_profiles

    @property
    def subtitle_profiles(self):
        """Gets the subtitle_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501


        :return: The subtitle_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :rtype: list[DlnaSubtitleProfile]
        """
        return self._subtitle_profiles

    @subtitle_profiles.setter
    def subtitle_profiles(self, subtitle_profiles):
        """Sets the subtitle_profiles of this EmbyDlnaProfilesDlnaProfile.


        :param subtitle_profiles: The subtitle_profiles of this EmbyDlnaProfilesDlnaProfile.  # noqa: E501
        :type: list[DlnaSubtitleProfile]
        """

        self._subtitle_profiles = subtitle_profiles

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
        if issubclass(EmbyDlnaProfilesDlnaProfile, dict):
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
        if not isinstance(other, EmbyDlnaProfilesDlnaProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
