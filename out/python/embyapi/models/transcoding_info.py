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

class TranscodingInfo(object):
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
        'audio_codec': 'str',
        'video_codec': 'str',
        'sub_protocol': 'str',
        'container': 'str',
        'is_video_direct': 'bool',
        'is_audio_direct': 'bool',
        'bitrate': 'int',
        'audio_bitrate': 'int',
        'video_bitrate': 'int',
        'framerate': 'float',
        'completion_percentage': 'float',
        'transcoding_position_ticks': 'float',
        'transcoding_start_position_ticks': 'float',
        'width': 'int',
        'height': 'int',
        'audio_channels': 'int',
        'transcode_reasons': 'list[str]',
        'current_cpu_usage': 'float',
        'average_cpu_usage': 'float',
        'cpu_history': 'list[TupleDoubleDouble]',
        'current_throttle': 'int',
        'video_decoder': 'str',
        'video_decoder_is_hardware': 'bool',
        'video_decoder_media_type': 'str',
        'video_decoder_hw_accel': 'str',
        'video_encoder': 'str',
        'video_encoder_is_hardware': 'bool',
        'video_encoder_media_type': 'str',
        'video_encoder_hw_accel': 'str',
        'video_pipeline_info': 'list[object]',
        'subtitle_pipeline_infos': 'list[list[object]]'
    }

    attribute_map = {
        'audio_codec': 'AudioCodec',
        'video_codec': 'VideoCodec',
        'sub_protocol': 'SubProtocol',
        'container': 'Container',
        'is_video_direct': 'IsVideoDirect',
        'is_audio_direct': 'IsAudioDirect',
        'bitrate': 'Bitrate',
        'audio_bitrate': 'AudioBitrate',
        'video_bitrate': 'VideoBitrate',
        'framerate': 'Framerate',
        'completion_percentage': 'CompletionPercentage',
        'transcoding_position_ticks': 'TranscodingPositionTicks',
        'transcoding_start_position_ticks': 'TranscodingStartPositionTicks',
        'width': 'Width',
        'height': 'Height',
        'audio_channels': 'AudioChannels',
        'transcode_reasons': 'TranscodeReasons',
        'current_cpu_usage': 'CurrentCpuUsage',
        'average_cpu_usage': 'AverageCpuUsage',
        'cpu_history': 'CpuHistory',
        'current_throttle': 'CurrentThrottle',
        'video_decoder': 'VideoDecoder',
        'video_decoder_is_hardware': 'VideoDecoderIsHardware',
        'video_decoder_media_type': 'VideoDecoderMediaType',
        'video_decoder_hw_accel': 'VideoDecoderHwAccel',
        'video_encoder': 'VideoEncoder',
        'video_encoder_is_hardware': 'VideoEncoderIsHardware',
        'video_encoder_media_type': 'VideoEncoderMediaType',
        'video_encoder_hw_accel': 'VideoEncoderHwAccel',
        'video_pipeline_info': 'VideoPipelineInfo',
        'subtitle_pipeline_infos': 'SubtitlePipelineInfos'
    }

    def __init__(self, audio_codec=None, video_codec=None, sub_protocol=None, container=None, is_video_direct=None, is_audio_direct=None, bitrate=None, audio_bitrate=None, video_bitrate=None, framerate=None, completion_percentage=None, transcoding_position_ticks=None, transcoding_start_position_ticks=None, width=None, height=None, audio_channels=None, transcode_reasons=None, current_cpu_usage=None, average_cpu_usage=None, cpu_history=None, current_throttle=None, video_decoder=None, video_decoder_is_hardware=None, video_decoder_media_type=None, video_decoder_hw_accel=None, video_encoder=None, video_encoder_is_hardware=None, video_encoder_media_type=None, video_encoder_hw_accel=None, video_pipeline_info=None, subtitle_pipeline_infos=None):  # noqa: E501
        """TranscodingInfo - a model defined in Swagger"""  # noqa: E501
        self._audio_codec = None
        self._video_codec = None
        self._sub_protocol = None
        self._container = None
        self._is_video_direct = None
        self._is_audio_direct = None
        self._bitrate = None
        self._audio_bitrate = None
        self._video_bitrate = None
        self._framerate = None
        self._completion_percentage = None
        self._transcoding_position_ticks = None
        self._transcoding_start_position_ticks = None
        self._width = None
        self._height = None
        self._audio_channels = None
        self._transcode_reasons = None
        self._current_cpu_usage = None
        self._average_cpu_usage = None
        self._cpu_history = None
        self._current_throttle = None
        self._video_decoder = None
        self._video_decoder_is_hardware = None
        self._video_decoder_media_type = None
        self._video_decoder_hw_accel = None
        self._video_encoder = None
        self._video_encoder_is_hardware = None
        self._video_encoder_media_type = None
        self._video_encoder_hw_accel = None
        self._video_pipeline_info = None
        self._subtitle_pipeline_infos = None
        self.discriminator = None
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if video_codec is not None:
            self.video_codec = video_codec
        if sub_protocol is not None:
            self.sub_protocol = sub_protocol
        if container is not None:
            self.container = container
        if is_video_direct is not None:
            self.is_video_direct = is_video_direct
        if is_audio_direct is not None:
            self.is_audio_direct = is_audio_direct
        if bitrate is not None:
            self.bitrate = bitrate
        if audio_bitrate is not None:
            self.audio_bitrate = audio_bitrate
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if framerate is not None:
            self.framerate = framerate
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if transcoding_position_ticks is not None:
            self.transcoding_position_ticks = transcoding_position_ticks
        if transcoding_start_position_ticks is not None:
            self.transcoding_start_position_ticks = transcoding_start_position_ticks
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if audio_channels is not None:
            self.audio_channels = audio_channels
        if transcode_reasons is not None:
            self.transcode_reasons = transcode_reasons
        if current_cpu_usage is not None:
            self.current_cpu_usage = current_cpu_usage
        if average_cpu_usage is not None:
            self.average_cpu_usage = average_cpu_usage
        if cpu_history is not None:
            self.cpu_history = cpu_history
        if current_throttle is not None:
            self.current_throttle = current_throttle
        if video_decoder is not None:
            self.video_decoder = video_decoder
        if video_decoder_is_hardware is not None:
            self.video_decoder_is_hardware = video_decoder_is_hardware
        if video_decoder_media_type is not None:
            self.video_decoder_media_type = video_decoder_media_type
        if video_decoder_hw_accel is not None:
            self.video_decoder_hw_accel = video_decoder_hw_accel
        if video_encoder is not None:
            self.video_encoder = video_encoder
        if video_encoder_is_hardware is not None:
            self.video_encoder_is_hardware = video_encoder_is_hardware
        if video_encoder_media_type is not None:
            self.video_encoder_media_type = video_encoder_media_type
        if video_encoder_hw_accel is not None:
            self.video_encoder_hw_accel = video_encoder_hw_accel
        if video_pipeline_info is not None:
            self.video_pipeline_info = video_pipeline_info
        if subtitle_pipeline_infos is not None:
            self.subtitle_pipeline_infos = subtitle_pipeline_infos

    @property
    def audio_codec(self):
        """Gets the audio_codec of this TranscodingInfo.  # noqa: E501


        :return: The audio_codec of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this TranscodingInfo.


        :param audio_codec: The audio_codec of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._audio_codec = audio_codec

    @property
    def video_codec(self):
        """Gets the video_codec of this TranscodingInfo.  # noqa: E501


        :return: The video_codec of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this TranscodingInfo.


        :param video_codec: The video_codec of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_codec = video_codec

    @property
    def sub_protocol(self):
        """Gets the sub_protocol of this TranscodingInfo.  # noqa: E501


        :return: The sub_protocol of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._sub_protocol

    @sub_protocol.setter
    def sub_protocol(self, sub_protocol):
        """Sets the sub_protocol of this TranscodingInfo.


        :param sub_protocol: The sub_protocol of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._sub_protocol = sub_protocol

    @property
    def container(self):
        """Gets the container of this TranscodingInfo.  # noqa: E501


        :return: The container of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this TranscodingInfo.


        :param container: The container of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def is_video_direct(self):
        """Gets the is_video_direct of this TranscodingInfo.  # noqa: E501


        :return: The is_video_direct of this TranscodingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_video_direct

    @is_video_direct.setter
    def is_video_direct(self, is_video_direct):
        """Sets the is_video_direct of this TranscodingInfo.


        :param is_video_direct: The is_video_direct of this TranscodingInfo.  # noqa: E501
        :type: bool
        """

        self._is_video_direct = is_video_direct

    @property
    def is_audio_direct(self):
        """Gets the is_audio_direct of this TranscodingInfo.  # noqa: E501


        :return: The is_audio_direct of this TranscodingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_audio_direct

    @is_audio_direct.setter
    def is_audio_direct(self, is_audio_direct):
        """Sets the is_audio_direct of this TranscodingInfo.


        :param is_audio_direct: The is_audio_direct of this TranscodingInfo.  # noqa: E501
        :type: bool
        """

        self._is_audio_direct = is_audio_direct

    @property
    def bitrate(self):
        """Gets the bitrate of this TranscodingInfo.  # noqa: E501


        :return: The bitrate of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this TranscodingInfo.


        :param bitrate: The bitrate of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._bitrate = bitrate

    @property
    def audio_bitrate(self):
        """Gets the audio_bitrate of this TranscodingInfo.  # noqa: E501


        :return: The audio_bitrate of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._audio_bitrate

    @audio_bitrate.setter
    def audio_bitrate(self, audio_bitrate):
        """Sets the audio_bitrate of this TranscodingInfo.


        :param audio_bitrate: The audio_bitrate of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._audio_bitrate = audio_bitrate

    @property
    def video_bitrate(self):
        """Gets the video_bitrate of this TranscodingInfo.  # noqa: E501


        :return: The video_bitrate of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        """Sets the video_bitrate of this TranscodingInfo.


        :param video_bitrate: The video_bitrate of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._video_bitrate = video_bitrate

    @property
    def framerate(self):
        """Gets the framerate of this TranscodingInfo.  # noqa: E501


        :return: The framerate of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._framerate

    @framerate.setter
    def framerate(self, framerate):
        """Sets the framerate of this TranscodingInfo.


        :param framerate: The framerate of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._framerate = framerate

    @property
    def completion_percentage(self):
        """Gets the completion_percentage of this TranscodingInfo.  # noqa: E501


        :return: The completion_percentage of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._completion_percentage

    @completion_percentage.setter
    def completion_percentage(self, completion_percentage):
        """Sets the completion_percentage of this TranscodingInfo.


        :param completion_percentage: The completion_percentage of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._completion_percentage = completion_percentage

    @property
    def transcoding_position_ticks(self):
        """Gets the transcoding_position_ticks of this TranscodingInfo.  # noqa: E501


        :return: The transcoding_position_ticks of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._transcoding_position_ticks

    @transcoding_position_ticks.setter
    def transcoding_position_ticks(self, transcoding_position_ticks):
        """Sets the transcoding_position_ticks of this TranscodingInfo.


        :param transcoding_position_ticks: The transcoding_position_ticks of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._transcoding_position_ticks = transcoding_position_ticks

    @property
    def transcoding_start_position_ticks(self):
        """Gets the transcoding_start_position_ticks of this TranscodingInfo.  # noqa: E501


        :return: The transcoding_start_position_ticks of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._transcoding_start_position_ticks

    @transcoding_start_position_ticks.setter
    def transcoding_start_position_ticks(self, transcoding_start_position_ticks):
        """Sets the transcoding_start_position_ticks of this TranscodingInfo.


        :param transcoding_start_position_ticks: The transcoding_start_position_ticks of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._transcoding_start_position_ticks = transcoding_start_position_ticks

    @property
    def width(self):
        """Gets the width of this TranscodingInfo.  # noqa: E501


        :return: The width of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TranscodingInfo.


        :param width: The width of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this TranscodingInfo.  # noqa: E501


        :return: The height of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TranscodingInfo.


        :param height: The height of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def audio_channels(self):
        """Gets the audio_channels of this TranscodingInfo.  # noqa: E501


        :return: The audio_channels of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        """Sets the audio_channels of this TranscodingInfo.


        :param audio_channels: The audio_channels of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._audio_channels = audio_channels

    @property
    def transcode_reasons(self):
        """Gets the transcode_reasons of this TranscodingInfo.  # noqa: E501


        :return: The transcode_reasons of this TranscodingInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._transcode_reasons

    @transcode_reasons.setter
    def transcode_reasons(self, transcode_reasons):
        """Sets the transcode_reasons of this TranscodingInfo.


        :param transcode_reasons: The transcode_reasons of this TranscodingInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ContainerNotSupported", "VideoCodecNotSupported", "AudioCodecNotSupported", "ContainerBitrateExceedsLimit", "AudioBitrateNotSupported", "AudioChannelsNotSupported", "VideoResolutionNotSupported", "UnknownVideoStreamInfo", "UnknownAudioStreamInfo", "AudioProfileNotSupported", "AudioSampleRateNotSupported", "AnamorphicVideoNotSupported", "InterlacedVideoNotSupported", "SecondaryAudioNotSupported", "RefFramesNotSupported", "VideoBitDepthNotSupported", "VideoBitrateNotSupported", "VideoFramerateNotSupported", "VideoLevelNotSupported", "VideoProfileNotSupported", "AudioBitDepthNotSupported", "SubtitleCodecNotSupported", "DirectPlayError", "VideoRangeNotSupported"]  # noqa: E501
        if not set(transcode_reasons).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `transcode_reasons` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(transcode_reasons) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._transcode_reasons = transcode_reasons

    @property
    def current_cpu_usage(self):
        """Gets the current_cpu_usage of this TranscodingInfo.  # noqa: E501


        :return: The current_cpu_usage of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._current_cpu_usage

    @current_cpu_usage.setter
    def current_cpu_usage(self, current_cpu_usage):
        """Sets the current_cpu_usage of this TranscodingInfo.


        :param current_cpu_usage: The current_cpu_usage of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._current_cpu_usage = current_cpu_usage

    @property
    def average_cpu_usage(self):
        """Gets the average_cpu_usage of this TranscodingInfo.  # noqa: E501


        :return: The average_cpu_usage of this TranscodingInfo.  # noqa: E501
        :rtype: float
        """
        return self._average_cpu_usage

    @average_cpu_usage.setter
    def average_cpu_usage(self, average_cpu_usage):
        """Sets the average_cpu_usage of this TranscodingInfo.


        :param average_cpu_usage: The average_cpu_usage of this TranscodingInfo.  # noqa: E501
        :type: float
        """

        self._average_cpu_usage = average_cpu_usage

    @property
    def cpu_history(self):
        """Gets the cpu_history of this TranscodingInfo.  # noqa: E501


        :return: The cpu_history of this TranscodingInfo.  # noqa: E501
        :rtype: list[TupleDoubleDouble]
        """
        return self._cpu_history

    @cpu_history.setter
    def cpu_history(self, cpu_history):
        """Sets the cpu_history of this TranscodingInfo.


        :param cpu_history: The cpu_history of this TranscodingInfo.  # noqa: E501
        :type: list[TupleDoubleDouble]
        """

        self._cpu_history = cpu_history

    @property
    def current_throttle(self):
        """Gets the current_throttle of this TranscodingInfo.  # noqa: E501


        :return: The current_throttle of this TranscodingInfo.  # noqa: E501
        :rtype: int
        """
        return self._current_throttle

    @current_throttle.setter
    def current_throttle(self, current_throttle):
        """Sets the current_throttle of this TranscodingInfo.


        :param current_throttle: The current_throttle of this TranscodingInfo.  # noqa: E501
        :type: int
        """

        self._current_throttle = current_throttle

    @property
    def video_decoder(self):
        """Gets the video_decoder of this TranscodingInfo.  # noqa: E501


        :return: The video_decoder of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_decoder

    @video_decoder.setter
    def video_decoder(self, video_decoder):
        """Sets the video_decoder of this TranscodingInfo.


        :param video_decoder: The video_decoder of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_decoder = video_decoder

    @property
    def video_decoder_is_hardware(self):
        """Gets the video_decoder_is_hardware of this TranscodingInfo.  # noqa: E501


        :return: The video_decoder_is_hardware of this TranscodingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._video_decoder_is_hardware

    @video_decoder_is_hardware.setter
    def video_decoder_is_hardware(self, video_decoder_is_hardware):
        """Sets the video_decoder_is_hardware of this TranscodingInfo.


        :param video_decoder_is_hardware: The video_decoder_is_hardware of this TranscodingInfo.  # noqa: E501
        :type: bool
        """

        self._video_decoder_is_hardware = video_decoder_is_hardware

    @property
    def video_decoder_media_type(self):
        """Gets the video_decoder_media_type of this TranscodingInfo.  # noqa: E501


        :return: The video_decoder_media_type of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_decoder_media_type

    @video_decoder_media_type.setter
    def video_decoder_media_type(self, video_decoder_media_type):
        """Sets the video_decoder_media_type of this TranscodingInfo.


        :param video_decoder_media_type: The video_decoder_media_type of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_decoder_media_type = video_decoder_media_type

    @property
    def video_decoder_hw_accel(self):
        """Gets the video_decoder_hw_accel of this TranscodingInfo.  # noqa: E501


        :return: The video_decoder_hw_accel of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_decoder_hw_accel

    @video_decoder_hw_accel.setter
    def video_decoder_hw_accel(self, video_decoder_hw_accel):
        """Sets the video_decoder_hw_accel of this TranscodingInfo.


        :param video_decoder_hw_accel: The video_decoder_hw_accel of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_decoder_hw_accel = video_decoder_hw_accel

    @property
    def video_encoder(self):
        """Gets the video_encoder of this TranscodingInfo.  # noqa: E501


        :return: The video_encoder of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_encoder

    @video_encoder.setter
    def video_encoder(self, video_encoder):
        """Sets the video_encoder of this TranscodingInfo.


        :param video_encoder: The video_encoder of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_encoder = video_encoder

    @property
    def video_encoder_is_hardware(self):
        """Gets the video_encoder_is_hardware of this TranscodingInfo.  # noqa: E501


        :return: The video_encoder_is_hardware of this TranscodingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._video_encoder_is_hardware

    @video_encoder_is_hardware.setter
    def video_encoder_is_hardware(self, video_encoder_is_hardware):
        """Sets the video_encoder_is_hardware of this TranscodingInfo.


        :param video_encoder_is_hardware: The video_encoder_is_hardware of this TranscodingInfo.  # noqa: E501
        :type: bool
        """

        self._video_encoder_is_hardware = video_encoder_is_hardware

    @property
    def video_encoder_media_type(self):
        """Gets the video_encoder_media_type of this TranscodingInfo.  # noqa: E501


        :return: The video_encoder_media_type of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_encoder_media_type

    @video_encoder_media_type.setter
    def video_encoder_media_type(self, video_encoder_media_type):
        """Sets the video_encoder_media_type of this TranscodingInfo.


        :param video_encoder_media_type: The video_encoder_media_type of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_encoder_media_type = video_encoder_media_type

    @property
    def video_encoder_hw_accel(self):
        """Gets the video_encoder_hw_accel of this TranscodingInfo.  # noqa: E501


        :return: The video_encoder_hw_accel of this TranscodingInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_encoder_hw_accel

    @video_encoder_hw_accel.setter
    def video_encoder_hw_accel(self, video_encoder_hw_accel):
        """Sets the video_encoder_hw_accel of this TranscodingInfo.


        :param video_encoder_hw_accel: The video_encoder_hw_accel of this TranscodingInfo.  # noqa: E501
        :type: str
        """

        self._video_encoder_hw_accel = video_encoder_hw_accel

    @property
    def video_pipeline_info(self):
        """Gets the video_pipeline_info of this TranscodingInfo.  # noqa: E501


        :return: The video_pipeline_info of this TranscodingInfo.  # noqa: E501
        :rtype: list[object]
        """
        return self._video_pipeline_info

    @video_pipeline_info.setter
    def video_pipeline_info(self, video_pipeline_info):
        """Sets the video_pipeline_info of this TranscodingInfo.


        :param video_pipeline_info: The video_pipeline_info of this TranscodingInfo.  # noqa: E501
        :type: list[object]
        """

        self._video_pipeline_info = video_pipeline_info

    @property
    def subtitle_pipeline_infos(self):
        """Gets the subtitle_pipeline_infos of this TranscodingInfo.  # noqa: E501


        :return: The subtitle_pipeline_infos of this TranscodingInfo.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._subtitle_pipeline_infos

    @subtitle_pipeline_infos.setter
    def subtitle_pipeline_infos(self, subtitle_pipeline_infos):
        """Sets the subtitle_pipeline_infos of this TranscodingInfo.


        :param subtitle_pipeline_infos: The subtitle_pipeline_infos of this TranscodingInfo.  # noqa: E501
        :type: list[list[object]]
        """

        self._subtitle_pipeline_infos = subtitle_pipeline_infos

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
        if issubclass(TranscodingInfo, dict):
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
        if not isinstance(other, TranscodingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
