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

class PlaybackProgressInfo(object):
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
        'can_seek': 'bool',
        'item': 'BaseItemDto',
        'now_playing_queue': 'list[QueueItem]',
        'playlist_item_id': 'str',
        'item_id': 'str',
        'session_id': 'str',
        'media_source_id': 'str',
        'audio_stream_index': 'int',
        'subtitle_stream_index': 'int',
        'is_paused': 'bool',
        'playlist_index': 'int',
        'playlist_length': 'int',
        'is_muted': 'bool',
        'position_ticks': 'int',
        'run_time_ticks': 'int',
        'playback_start_time_ticks': 'int',
        'volume_level': 'int',
        'brightness': 'int',
        'aspect_ratio': 'str',
        'event_name': 'str',
        'play_method': 'str',
        'live_stream_id': 'str',
        'play_session_id': 'str',
        'repeat_mode': 'str',
        'subtitle_offset': 'int',
        'playback_rate': 'float',
        'playlist_item_ids': 'list[str]'
    }

    attribute_map = {
        'can_seek': 'CanSeek',
        'item': 'Item',
        'now_playing_queue': 'NowPlayingQueue',
        'playlist_item_id': 'PlaylistItemId',
        'item_id': 'ItemId',
        'session_id': 'SessionId',
        'media_source_id': 'MediaSourceId',
        'audio_stream_index': 'AudioStreamIndex',
        'subtitle_stream_index': 'SubtitleStreamIndex',
        'is_paused': 'IsPaused',
        'playlist_index': 'PlaylistIndex',
        'playlist_length': 'PlaylistLength',
        'is_muted': 'IsMuted',
        'position_ticks': 'PositionTicks',
        'run_time_ticks': 'RunTimeTicks',
        'playback_start_time_ticks': 'PlaybackStartTimeTicks',
        'volume_level': 'VolumeLevel',
        'brightness': 'Brightness',
        'aspect_ratio': 'AspectRatio',
        'event_name': 'EventName',
        'play_method': 'PlayMethod',
        'live_stream_id': 'LiveStreamId',
        'play_session_id': 'PlaySessionId',
        'repeat_mode': 'RepeatMode',
        'subtitle_offset': 'SubtitleOffset',
        'playback_rate': 'PlaybackRate',
        'playlist_item_ids': 'PlaylistItemIds'
    }

    def __init__(self, can_seek=None, item=None, now_playing_queue=None, playlist_item_id=None, item_id=None, session_id=None, media_source_id=None, audio_stream_index=None, subtitle_stream_index=None, is_paused=None, playlist_index=None, playlist_length=None, is_muted=None, position_ticks=None, run_time_ticks=None, playback_start_time_ticks=None, volume_level=None, brightness=None, aspect_ratio=None, event_name=None, play_method=None, live_stream_id=None, play_session_id=None, repeat_mode=None, subtitle_offset=None, playback_rate=None, playlist_item_ids=None):  # noqa: E501
        """PlaybackProgressInfo - a model defined in Swagger"""  # noqa: E501
        self._can_seek = None
        self._item = None
        self._now_playing_queue = None
        self._playlist_item_id = None
        self._item_id = None
        self._session_id = None
        self._media_source_id = None
        self._audio_stream_index = None
        self._subtitle_stream_index = None
        self._is_paused = None
        self._playlist_index = None
        self._playlist_length = None
        self._is_muted = None
        self._position_ticks = None
        self._run_time_ticks = None
        self._playback_start_time_ticks = None
        self._volume_level = None
        self._brightness = None
        self._aspect_ratio = None
        self._event_name = None
        self._play_method = None
        self._live_stream_id = None
        self._play_session_id = None
        self._repeat_mode = None
        self._subtitle_offset = None
        self._playback_rate = None
        self._playlist_item_ids = None
        self.discriminator = None
        if can_seek is not None:
            self.can_seek = can_seek
        if item is not None:
            self.item = item
        if now_playing_queue is not None:
            self.now_playing_queue = now_playing_queue
        if playlist_item_id is not None:
            self.playlist_item_id = playlist_item_id
        if item_id is not None:
            self.item_id = item_id
        if session_id is not None:
            self.session_id = session_id
        if media_source_id is not None:
            self.media_source_id = media_source_id
        if audio_stream_index is not None:
            self.audio_stream_index = audio_stream_index
        if subtitle_stream_index is not None:
            self.subtitle_stream_index = subtitle_stream_index
        if is_paused is not None:
            self.is_paused = is_paused
        if playlist_index is not None:
            self.playlist_index = playlist_index
        if playlist_length is not None:
            self.playlist_length = playlist_length
        if is_muted is not None:
            self.is_muted = is_muted
        if position_ticks is not None:
            self.position_ticks = position_ticks
        if run_time_ticks is not None:
            self.run_time_ticks = run_time_ticks
        if playback_start_time_ticks is not None:
            self.playback_start_time_ticks = playback_start_time_ticks
        if volume_level is not None:
            self.volume_level = volume_level
        if brightness is not None:
            self.brightness = brightness
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if event_name is not None:
            self.event_name = event_name
        if play_method is not None:
            self.play_method = play_method
        if live_stream_id is not None:
            self.live_stream_id = live_stream_id
        if play_session_id is not None:
            self.play_session_id = play_session_id
        if repeat_mode is not None:
            self.repeat_mode = repeat_mode
        if subtitle_offset is not None:
            self.subtitle_offset = subtitle_offset
        if playback_rate is not None:
            self.playback_rate = playback_rate
        if playlist_item_ids is not None:
            self.playlist_item_ids = playlist_item_ids

    @property
    def can_seek(self):
        """Gets the can_seek of this PlaybackProgressInfo.  # noqa: E501


        :return: The can_seek of this PlaybackProgressInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_seek

    @can_seek.setter
    def can_seek(self, can_seek):
        """Sets the can_seek of this PlaybackProgressInfo.


        :param can_seek: The can_seek of this PlaybackProgressInfo.  # noqa: E501
        :type: bool
        """

        self._can_seek = can_seek

    @property
    def item(self):
        """Gets the item of this PlaybackProgressInfo.  # noqa: E501


        :return: The item of this PlaybackProgressInfo.  # noqa: E501
        :rtype: BaseItemDto
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this PlaybackProgressInfo.


        :param item: The item of this PlaybackProgressInfo.  # noqa: E501
        :type: BaseItemDto
        """

        self._item = item

    @property
    def now_playing_queue(self):
        """Gets the now_playing_queue of this PlaybackProgressInfo.  # noqa: E501


        :return: The now_playing_queue of this PlaybackProgressInfo.  # noqa: E501
        :rtype: list[QueueItem]
        """
        return self._now_playing_queue

    @now_playing_queue.setter
    def now_playing_queue(self, now_playing_queue):
        """Sets the now_playing_queue of this PlaybackProgressInfo.


        :param now_playing_queue: The now_playing_queue of this PlaybackProgressInfo.  # noqa: E501
        :type: list[QueueItem]
        """

        self._now_playing_queue = now_playing_queue

    @property
    def playlist_item_id(self):
        """Gets the playlist_item_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The playlist_item_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._playlist_item_id

    @playlist_item_id.setter
    def playlist_item_id(self, playlist_item_id):
        """Sets the playlist_item_id of this PlaybackProgressInfo.


        :param playlist_item_id: The playlist_item_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._playlist_item_id = playlist_item_id

    @property
    def item_id(self):
        """Gets the item_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The item_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this PlaybackProgressInfo.


        :param item_id: The item_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def session_id(self):
        """Gets the session_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The session_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this PlaybackProgressInfo.


        :param session_id: The session_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def media_source_id(self):
        """Gets the media_source_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The media_source_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._media_source_id

    @media_source_id.setter
    def media_source_id(self, media_source_id):
        """Sets the media_source_id of this PlaybackProgressInfo.


        :param media_source_id: The media_source_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._media_source_id = media_source_id

    @property
    def audio_stream_index(self):
        """Gets the audio_stream_index of this PlaybackProgressInfo.  # noqa: E501


        :return: The audio_stream_index of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._audio_stream_index

    @audio_stream_index.setter
    def audio_stream_index(self, audio_stream_index):
        """Sets the audio_stream_index of this PlaybackProgressInfo.


        :param audio_stream_index: The audio_stream_index of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._audio_stream_index = audio_stream_index

    @property
    def subtitle_stream_index(self):
        """Gets the subtitle_stream_index of this PlaybackProgressInfo.  # noqa: E501


        :return: The subtitle_stream_index of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._subtitle_stream_index

    @subtitle_stream_index.setter
    def subtitle_stream_index(self, subtitle_stream_index):
        """Sets the subtitle_stream_index of this PlaybackProgressInfo.


        :param subtitle_stream_index: The subtitle_stream_index of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._subtitle_stream_index = subtitle_stream_index

    @property
    def is_paused(self):
        """Gets the is_paused of this PlaybackProgressInfo.  # noqa: E501


        :return: The is_paused of this PlaybackProgressInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_paused

    @is_paused.setter
    def is_paused(self, is_paused):
        """Sets the is_paused of this PlaybackProgressInfo.


        :param is_paused: The is_paused of this PlaybackProgressInfo.  # noqa: E501
        :type: bool
        """

        self._is_paused = is_paused

    @property
    def playlist_index(self):
        """Gets the playlist_index of this PlaybackProgressInfo.  # noqa: E501


        :return: The playlist_index of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._playlist_index

    @playlist_index.setter
    def playlist_index(self, playlist_index):
        """Sets the playlist_index of this PlaybackProgressInfo.


        :param playlist_index: The playlist_index of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._playlist_index = playlist_index

    @property
    def playlist_length(self):
        """Gets the playlist_length of this PlaybackProgressInfo.  # noqa: E501


        :return: The playlist_length of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._playlist_length

    @playlist_length.setter
    def playlist_length(self, playlist_length):
        """Sets the playlist_length of this PlaybackProgressInfo.


        :param playlist_length: The playlist_length of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._playlist_length = playlist_length

    @property
    def is_muted(self):
        """Gets the is_muted of this PlaybackProgressInfo.  # noqa: E501


        :return: The is_muted of this PlaybackProgressInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_muted

    @is_muted.setter
    def is_muted(self, is_muted):
        """Sets the is_muted of this PlaybackProgressInfo.


        :param is_muted: The is_muted of this PlaybackProgressInfo.  # noqa: E501
        :type: bool
        """

        self._is_muted = is_muted

    @property
    def position_ticks(self):
        """Gets the position_ticks of this PlaybackProgressInfo.  # noqa: E501


        :return: The position_ticks of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._position_ticks

    @position_ticks.setter
    def position_ticks(self, position_ticks):
        """Sets the position_ticks of this PlaybackProgressInfo.


        :param position_ticks: The position_ticks of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._position_ticks = position_ticks

    @property
    def run_time_ticks(self):
        """Gets the run_time_ticks of this PlaybackProgressInfo.  # noqa: E501


        :return: The run_time_ticks of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._run_time_ticks

    @run_time_ticks.setter
    def run_time_ticks(self, run_time_ticks):
        """Sets the run_time_ticks of this PlaybackProgressInfo.


        :param run_time_ticks: The run_time_ticks of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._run_time_ticks = run_time_ticks

    @property
    def playback_start_time_ticks(self):
        """Gets the playback_start_time_ticks of this PlaybackProgressInfo.  # noqa: E501


        :return: The playback_start_time_ticks of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._playback_start_time_ticks

    @playback_start_time_ticks.setter
    def playback_start_time_ticks(self, playback_start_time_ticks):
        """Sets the playback_start_time_ticks of this PlaybackProgressInfo.


        :param playback_start_time_ticks: The playback_start_time_ticks of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._playback_start_time_ticks = playback_start_time_ticks

    @property
    def volume_level(self):
        """Gets the volume_level of this PlaybackProgressInfo.  # noqa: E501


        :return: The volume_level of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._volume_level

    @volume_level.setter
    def volume_level(self, volume_level):
        """Sets the volume_level of this PlaybackProgressInfo.


        :param volume_level: The volume_level of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._volume_level = volume_level

    @property
    def brightness(self):
        """Gets the brightness of this PlaybackProgressInfo.  # noqa: E501


        :return: The brightness of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this PlaybackProgressInfo.


        :param brightness: The brightness of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this PlaybackProgressInfo.  # noqa: E501


        :return: The aspect_ratio of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this PlaybackProgressInfo.


        :param aspect_ratio: The aspect_ratio of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._aspect_ratio = aspect_ratio

    @property
    def event_name(self):
        """Gets the event_name of this PlaybackProgressInfo.  # noqa: E501


        :return: The event_name of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this PlaybackProgressInfo.


        :param event_name: The event_name of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["TimeUpdate", "Pause", "Unpause", "VolumeChange", "RepeatModeChange", "AudioTrackChange", "SubtitleTrackChange", "PlaylistItemMove", "PlaylistItemRemove", "PlaylistItemAdd", "QualityChange", "StateChange", "SubtitleOffsetChange", "PlaybackRateChange"]  # noqa: E501
        if event_name not in allowed_values:
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def play_method(self):
        """Gets the play_method of this PlaybackProgressInfo.  # noqa: E501


        :return: The play_method of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._play_method

    @play_method.setter
    def play_method(self, play_method):
        """Sets the play_method of this PlaybackProgressInfo.


        :param play_method: The play_method of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Transcode", "DirectStream", "DirectPlay"]  # noqa: E501
        if play_method not in allowed_values:
            raise ValueError(
                "Invalid value for `play_method` ({0}), must be one of {1}"  # noqa: E501
                .format(play_method, allowed_values)
            )

        self._play_method = play_method

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The live_stream_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this PlaybackProgressInfo.


        :param live_stream_id: The live_stream_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._live_stream_id = live_stream_id

    @property
    def play_session_id(self):
        """Gets the play_session_id of this PlaybackProgressInfo.  # noqa: E501


        :return: The play_session_id of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._play_session_id

    @play_session_id.setter
    def play_session_id(self, play_session_id):
        """Sets the play_session_id of this PlaybackProgressInfo.


        :param play_session_id: The play_session_id of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """

        self._play_session_id = play_session_id

    @property
    def repeat_mode(self):
        """Gets the repeat_mode of this PlaybackProgressInfo.  # noqa: E501


        :return: The repeat_mode of this PlaybackProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._repeat_mode

    @repeat_mode.setter
    def repeat_mode(self, repeat_mode):
        """Sets the repeat_mode of this PlaybackProgressInfo.


        :param repeat_mode: The repeat_mode of this PlaybackProgressInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["RepeatNone", "RepeatAll", "RepeatOne"]  # noqa: E501
        if repeat_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `repeat_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(repeat_mode, allowed_values)
            )

        self._repeat_mode = repeat_mode

    @property
    def subtitle_offset(self):
        """Gets the subtitle_offset of this PlaybackProgressInfo.  # noqa: E501


        :return: The subtitle_offset of this PlaybackProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._subtitle_offset

    @subtitle_offset.setter
    def subtitle_offset(self, subtitle_offset):
        """Sets the subtitle_offset of this PlaybackProgressInfo.


        :param subtitle_offset: The subtitle_offset of this PlaybackProgressInfo.  # noqa: E501
        :type: int
        """

        self._subtitle_offset = subtitle_offset

    @property
    def playback_rate(self):
        """Gets the playback_rate of this PlaybackProgressInfo.  # noqa: E501


        :return: The playback_rate of this PlaybackProgressInfo.  # noqa: E501
        :rtype: float
        """
        return self._playback_rate

    @playback_rate.setter
    def playback_rate(self, playback_rate):
        """Sets the playback_rate of this PlaybackProgressInfo.


        :param playback_rate: The playback_rate of this PlaybackProgressInfo.  # noqa: E501
        :type: float
        """

        self._playback_rate = playback_rate

    @property
    def playlist_item_ids(self):
        """Gets the playlist_item_ids of this PlaybackProgressInfo.  # noqa: E501


        :return: The playlist_item_ids of this PlaybackProgressInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._playlist_item_ids

    @playlist_item_ids.setter
    def playlist_item_ids(self, playlist_item_ids):
        """Sets the playlist_item_ids of this PlaybackProgressInfo.


        :param playlist_item_ids: The playlist_item_ids of this PlaybackProgressInfo.  # noqa: E501
        :type: list[str]
        """

        self._playlist_item_ids = playlist_item_ids

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
        if issubclass(PlaybackProgressInfo, dict):
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
        if not isinstance(other, PlaybackProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
