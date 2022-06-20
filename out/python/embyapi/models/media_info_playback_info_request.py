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

class MediaInfoPlaybackInfoRequest(object):
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
        'user_id': 'str',
        'max_streaming_bitrate': 'int',
        'start_time_ticks': 'int',
        'audio_stream_index': 'int',
        'subtitle_stream_index': 'int',
        'max_audio_channels': 'int',
        'media_source_id': 'str',
        'live_stream_id': 'str',
        'device_profile': 'DlnaDeviceProfile',
        'enable_direct_play': 'bool',
        'enable_direct_stream': 'bool',
        'enable_transcoding': 'bool',
        'allow_interlaced_video_stream_copy': 'bool',
        'allow_video_stream_copy': 'bool',
        'allow_audio_stream_copy': 'bool',
        'is_playback': 'bool',
        'auto_open_live_stream': 'bool',
        'direct_play_protocols': 'list[str]',
        'current_play_session_id': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'user_id': 'UserId',
        'max_streaming_bitrate': 'MaxStreamingBitrate',
        'start_time_ticks': 'StartTimeTicks',
        'audio_stream_index': 'AudioStreamIndex',
        'subtitle_stream_index': 'SubtitleStreamIndex',
        'max_audio_channels': 'MaxAudioChannels',
        'media_source_id': 'MediaSourceId',
        'live_stream_id': 'LiveStreamId',
        'device_profile': 'DeviceProfile',
        'enable_direct_play': 'EnableDirectPlay',
        'enable_direct_stream': 'EnableDirectStream',
        'enable_transcoding': 'EnableTranscoding',
        'allow_interlaced_video_stream_copy': 'AllowInterlacedVideoStreamCopy',
        'allow_video_stream_copy': 'AllowVideoStreamCopy',
        'allow_audio_stream_copy': 'AllowAudioStreamCopy',
        'is_playback': 'IsPlayback',
        'auto_open_live_stream': 'AutoOpenLiveStream',
        'direct_play_protocols': 'DirectPlayProtocols',
        'current_play_session_id': 'CurrentPlaySessionId'
    }

    def __init__(self, id=None, user_id=None, max_streaming_bitrate=None, start_time_ticks=None, audio_stream_index=None, subtitle_stream_index=None, max_audio_channels=None, media_source_id=None, live_stream_id=None, device_profile=None, enable_direct_play=None, enable_direct_stream=None, enable_transcoding=None, allow_interlaced_video_stream_copy=None, allow_video_stream_copy=None, allow_audio_stream_copy=None, is_playback=None, auto_open_live_stream=None, direct_play_protocols=None, current_play_session_id=None):  # noqa: E501
        """MediaInfoPlaybackInfoRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._max_streaming_bitrate = None
        self._start_time_ticks = None
        self._audio_stream_index = None
        self._subtitle_stream_index = None
        self._max_audio_channels = None
        self._media_source_id = None
        self._live_stream_id = None
        self._device_profile = None
        self._enable_direct_play = None
        self._enable_direct_stream = None
        self._enable_transcoding = None
        self._allow_interlaced_video_stream_copy = None
        self._allow_video_stream_copy = None
        self._allow_audio_stream_copy = None
        self._is_playback = None
        self._auto_open_live_stream = None
        self._direct_play_protocols = None
        self._current_play_session_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if max_streaming_bitrate is not None:
            self.max_streaming_bitrate = max_streaming_bitrate
        if start_time_ticks is not None:
            self.start_time_ticks = start_time_ticks
        if audio_stream_index is not None:
            self.audio_stream_index = audio_stream_index
        if subtitle_stream_index is not None:
            self.subtitle_stream_index = subtitle_stream_index
        if max_audio_channels is not None:
            self.max_audio_channels = max_audio_channels
        if media_source_id is not None:
            self.media_source_id = media_source_id
        if live_stream_id is not None:
            self.live_stream_id = live_stream_id
        if device_profile is not None:
            self.device_profile = device_profile
        if enable_direct_play is not None:
            self.enable_direct_play = enable_direct_play
        if enable_direct_stream is not None:
            self.enable_direct_stream = enable_direct_stream
        if enable_transcoding is not None:
            self.enable_transcoding = enable_transcoding
        if allow_interlaced_video_stream_copy is not None:
            self.allow_interlaced_video_stream_copy = allow_interlaced_video_stream_copy
        if allow_video_stream_copy is not None:
            self.allow_video_stream_copy = allow_video_stream_copy
        if allow_audio_stream_copy is not None:
            self.allow_audio_stream_copy = allow_audio_stream_copy
        if is_playback is not None:
            self.is_playback = is_playback
        if auto_open_live_stream is not None:
            self.auto_open_live_stream = auto_open_live_stream
        if direct_play_protocols is not None:
            self.direct_play_protocols = direct_play_protocols
        if current_play_session_id is not None:
            self.current_play_session_id = current_play_session_id

    @property
    def id(self):
        """Gets the id of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaInfoPlaybackInfoRequest.


        :param id: The id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The user_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MediaInfoPlaybackInfoRequest.


        :param user_id: The user_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def max_streaming_bitrate(self):
        """Gets the max_streaming_bitrate of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The max_streaming_bitrate of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_streaming_bitrate

    @max_streaming_bitrate.setter
    def max_streaming_bitrate(self, max_streaming_bitrate):
        """Sets the max_streaming_bitrate of this MediaInfoPlaybackInfoRequest.


        :param max_streaming_bitrate: The max_streaming_bitrate of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: int
        """

        self._max_streaming_bitrate = max_streaming_bitrate

    @property
    def start_time_ticks(self):
        """Gets the start_time_ticks of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The start_time_ticks of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time_ticks

    @start_time_ticks.setter
    def start_time_ticks(self, start_time_ticks):
        """Sets the start_time_ticks of this MediaInfoPlaybackInfoRequest.


        :param start_time_ticks: The start_time_ticks of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: int
        """

        self._start_time_ticks = start_time_ticks

    @property
    def audio_stream_index(self):
        """Gets the audio_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The audio_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._audio_stream_index

    @audio_stream_index.setter
    def audio_stream_index(self, audio_stream_index):
        """Sets the audio_stream_index of this MediaInfoPlaybackInfoRequest.


        :param audio_stream_index: The audio_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: int
        """

        self._audio_stream_index = audio_stream_index

    @property
    def subtitle_stream_index(self):
        """Gets the subtitle_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The subtitle_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._subtitle_stream_index

    @subtitle_stream_index.setter
    def subtitle_stream_index(self, subtitle_stream_index):
        """Sets the subtitle_stream_index of this MediaInfoPlaybackInfoRequest.


        :param subtitle_stream_index: The subtitle_stream_index of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: int
        """

        self._subtitle_stream_index = subtitle_stream_index

    @property
    def max_audio_channels(self):
        """Gets the max_audio_channels of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The max_audio_channels of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_audio_channels

    @max_audio_channels.setter
    def max_audio_channels(self, max_audio_channels):
        """Sets the max_audio_channels of this MediaInfoPlaybackInfoRequest.


        :param max_audio_channels: The max_audio_channels of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: int
        """

        self._max_audio_channels = max_audio_channels

    @property
    def media_source_id(self):
        """Gets the media_source_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The media_source_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._media_source_id

    @media_source_id.setter
    def media_source_id(self, media_source_id):
        """Sets the media_source_id of this MediaInfoPlaybackInfoRequest.


        :param media_source_id: The media_source_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: str
        """

        self._media_source_id = media_source_id

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The live_stream_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this MediaInfoPlaybackInfoRequest.


        :param live_stream_id: The live_stream_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: str
        """

        self._live_stream_id = live_stream_id

    @property
    def device_profile(self):
        """Gets the device_profile of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The device_profile of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: DlnaDeviceProfile
        """
        return self._device_profile

    @device_profile.setter
    def device_profile(self, device_profile):
        """Sets the device_profile of this MediaInfoPlaybackInfoRequest.


        :param device_profile: The device_profile of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: DlnaDeviceProfile
        """

        self._device_profile = device_profile

    @property
    def enable_direct_play(self):
        """Gets the enable_direct_play of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The enable_direct_play of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_direct_play

    @enable_direct_play.setter
    def enable_direct_play(self, enable_direct_play):
        """Sets the enable_direct_play of this MediaInfoPlaybackInfoRequest.


        :param enable_direct_play: The enable_direct_play of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._enable_direct_play = enable_direct_play

    @property
    def enable_direct_stream(self):
        """Gets the enable_direct_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The enable_direct_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_direct_stream

    @enable_direct_stream.setter
    def enable_direct_stream(self, enable_direct_stream):
        """Sets the enable_direct_stream of this MediaInfoPlaybackInfoRequest.


        :param enable_direct_stream: The enable_direct_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._enable_direct_stream = enable_direct_stream

    @property
    def enable_transcoding(self):
        """Gets the enable_transcoding of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The enable_transcoding of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_transcoding

    @enable_transcoding.setter
    def enable_transcoding(self, enable_transcoding):
        """Sets the enable_transcoding of this MediaInfoPlaybackInfoRequest.


        :param enable_transcoding: The enable_transcoding of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._enable_transcoding = enable_transcoding

    @property
    def allow_interlaced_video_stream_copy(self):
        """Gets the allow_interlaced_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The allow_interlaced_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_interlaced_video_stream_copy

    @allow_interlaced_video_stream_copy.setter
    def allow_interlaced_video_stream_copy(self, allow_interlaced_video_stream_copy):
        """Sets the allow_interlaced_video_stream_copy of this MediaInfoPlaybackInfoRequest.


        :param allow_interlaced_video_stream_copy: The allow_interlaced_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._allow_interlaced_video_stream_copy = allow_interlaced_video_stream_copy

    @property
    def allow_video_stream_copy(self):
        """Gets the allow_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The allow_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_video_stream_copy

    @allow_video_stream_copy.setter
    def allow_video_stream_copy(self, allow_video_stream_copy):
        """Sets the allow_video_stream_copy of this MediaInfoPlaybackInfoRequest.


        :param allow_video_stream_copy: The allow_video_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._allow_video_stream_copy = allow_video_stream_copy

    @property
    def allow_audio_stream_copy(self):
        """Gets the allow_audio_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The allow_audio_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_audio_stream_copy

    @allow_audio_stream_copy.setter
    def allow_audio_stream_copy(self, allow_audio_stream_copy):
        """Sets the allow_audio_stream_copy of this MediaInfoPlaybackInfoRequest.


        :param allow_audio_stream_copy: The allow_audio_stream_copy of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._allow_audio_stream_copy = allow_audio_stream_copy

    @property
    def is_playback(self):
        """Gets the is_playback of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The is_playback of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_playback

    @is_playback.setter
    def is_playback(self, is_playback):
        """Sets the is_playback of this MediaInfoPlaybackInfoRequest.


        :param is_playback: The is_playback of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._is_playback = is_playback

    @property
    def auto_open_live_stream(self):
        """Gets the auto_open_live_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The auto_open_live_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_open_live_stream

    @auto_open_live_stream.setter
    def auto_open_live_stream(self, auto_open_live_stream):
        """Sets the auto_open_live_stream of this MediaInfoPlaybackInfoRequest.


        :param auto_open_live_stream: The auto_open_live_stream of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: bool
        """

        self._auto_open_live_stream = auto_open_live_stream

    @property
    def direct_play_protocols(self):
        """Gets the direct_play_protocols of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The direct_play_protocols of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._direct_play_protocols

    @direct_play_protocols.setter
    def direct_play_protocols(self, direct_play_protocols):
        """Sets the direct_play_protocols of this MediaInfoPlaybackInfoRequest.


        :param direct_play_protocols: The direct_play_protocols of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["File", "Http", "Rtmp", "Rtsp", "Udp", "Rtp", "Ftp", "Mms"]  # noqa: E501
        if not set(direct_play_protocols).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `direct_play_protocols` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(direct_play_protocols) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._direct_play_protocols = direct_play_protocols

    @property
    def current_play_session_id(self):
        """Gets the current_play_session_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501


        :return: The current_play_session_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._current_play_session_id

    @current_play_session_id.setter
    def current_play_session_id(self, current_play_session_id):
        """Sets the current_play_session_id of this MediaInfoPlaybackInfoRequest.


        :param current_play_session_id: The current_play_session_id of this MediaInfoPlaybackInfoRequest.  # noqa: E501
        :type: str
        """

        self._current_play_session_id = current_play_session_id

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
        if issubclass(MediaInfoPlaybackInfoRequest, dict):
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
        if not isinstance(other, MediaInfoPlaybackInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
