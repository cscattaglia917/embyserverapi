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

class LiveTvSeriesTimerInfo(object):
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
        'channel_id': 'str',
        'channel_ids': 'list[str]',
        'program_id': 'str',
        'name': 'str',
        'service_name': 'str',
        'overview': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'record_any_time': 'bool',
        'record_any_channel': 'bool',
        'keep_up_to': 'int',
        'keep_until': 'str',
        'skip_episodes_in_library': 'bool',
        'record_new_only': 'bool',
        'days': 'list[str]',
        'priority': 'int',
        'pre_padding_seconds': 'int',
        'post_padding_seconds': 'int',
        'is_pre_padding_required': 'bool',
        'is_post_padding_required': 'bool',
        'series_id': 'str',
        'provider_ids': 'list[object]',
        'max_recording_seconds': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'channel_id': 'ChannelId',
        'channel_ids': 'ChannelIds',
        'program_id': 'ProgramId',
        'name': 'Name',
        'service_name': 'ServiceName',
        'overview': 'Overview',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'record_any_time': 'RecordAnyTime',
        'record_any_channel': 'RecordAnyChannel',
        'keep_up_to': 'KeepUpTo',
        'keep_until': 'KeepUntil',
        'skip_episodes_in_library': 'SkipEpisodesInLibrary',
        'record_new_only': 'RecordNewOnly',
        'days': 'Days',
        'priority': 'Priority',
        'pre_padding_seconds': 'PrePaddingSeconds',
        'post_padding_seconds': 'PostPaddingSeconds',
        'is_pre_padding_required': 'IsPrePaddingRequired',
        'is_post_padding_required': 'IsPostPaddingRequired',
        'series_id': 'SeriesId',
        'provider_ids': 'ProviderIds',
        'max_recording_seconds': 'MaxRecordingSeconds'
    }

    def __init__(self, id=None, channel_id=None, channel_ids=None, program_id=None, name=None, service_name=None, overview=None, start_date=None, end_date=None, record_any_time=None, record_any_channel=None, keep_up_to=None, keep_until=None, skip_episodes_in_library=None, record_new_only=None, days=None, priority=None, pre_padding_seconds=None, post_padding_seconds=None, is_pre_padding_required=None, is_post_padding_required=None, series_id=None, provider_ids=None, max_recording_seconds=None):  # noqa: E501
        """LiveTvSeriesTimerInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._channel_id = None
        self._channel_ids = None
        self._program_id = None
        self._name = None
        self._service_name = None
        self._overview = None
        self._start_date = None
        self._end_date = None
        self._record_any_time = None
        self._record_any_channel = None
        self._keep_up_to = None
        self._keep_until = None
        self._skip_episodes_in_library = None
        self._record_new_only = None
        self._days = None
        self._priority = None
        self._pre_padding_seconds = None
        self._post_padding_seconds = None
        self._is_pre_padding_required = None
        self._is_post_padding_required = None
        self._series_id = None
        self._provider_ids = None
        self._max_recording_seconds = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_ids is not None:
            self.channel_ids = channel_ids
        if program_id is not None:
            self.program_id = program_id
        if name is not None:
            self.name = name
        if service_name is not None:
            self.service_name = service_name
        if overview is not None:
            self.overview = overview
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if record_any_time is not None:
            self.record_any_time = record_any_time
        if record_any_channel is not None:
            self.record_any_channel = record_any_channel
        if keep_up_to is not None:
            self.keep_up_to = keep_up_to
        if keep_until is not None:
            self.keep_until = keep_until
        if skip_episodes_in_library is not None:
            self.skip_episodes_in_library = skip_episodes_in_library
        if record_new_only is not None:
            self.record_new_only = record_new_only
        if days is not None:
            self.days = days
        if priority is not None:
            self.priority = priority
        if pre_padding_seconds is not None:
            self.pre_padding_seconds = pre_padding_seconds
        if post_padding_seconds is not None:
            self.post_padding_seconds = post_padding_seconds
        if is_pre_padding_required is not None:
            self.is_pre_padding_required = is_pre_padding_required
        if is_post_padding_required is not None:
            self.is_post_padding_required = is_post_padding_required
        if series_id is not None:
            self.series_id = series_id
        if provider_ids is not None:
            self.provider_ids = provider_ids
        if max_recording_seconds is not None:
            self.max_recording_seconds = max_recording_seconds

    @property
    def id(self):
        """Gets the id of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveTvSeriesTimerInfo.


        :param id: The id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def channel_id(self):
        """Gets the channel_id of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The channel_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this LiveTvSeriesTimerInfo.


        :param channel_id: The channel_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def channel_ids(self):
        """Gets the channel_ids of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The channel_ids of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._channel_ids

    @channel_ids.setter
    def channel_ids(self, channel_ids):
        """Sets the channel_ids of this LiveTvSeriesTimerInfo.


        :param channel_ids: The channel_ids of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: list[str]
        """

        self._channel_ids = channel_ids

    @property
    def program_id(self):
        """Gets the program_id of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The program_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LiveTvSeriesTimerInfo.


        :param program_id: The program_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._program_id = program_id

    @property
    def name(self):
        """Gets the name of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The name of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveTvSeriesTimerInfo.


        :param name: The name of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service_name(self):
        """Gets the service_name of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The service_name of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this LiveTvSeriesTimerInfo.


        :param service_name: The service_name of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def overview(self):
        """Gets the overview of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The overview of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this LiveTvSeriesTimerInfo.


        :param overview: The overview of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def start_date(self):
        """Gets the start_date of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The start_date of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LiveTvSeriesTimerInfo.


        :param start_date: The start_date of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The end_date of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this LiveTvSeriesTimerInfo.


        :param end_date: The end_date of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def record_any_time(self):
        """Gets the record_any_time of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The record_any_time of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._record_any_time

    @record_any_time.setter
    def record_any_time(self, record_any_time):
        """Sets the record_any_time of this LiveTvSeriesTimerInfo.


        :param record_any_time: The record_any_time of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._record_any_time = record_any_time

    @property
    def record_any_channel(self):
        """Gets the record_any_channel of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The record_any_channel of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._record_any_channel

    @record_any_channel.setter
    def record_any_channel(self, record_any_channel):
        """Sets the record_any_channel of this LiveTvSeriesTimerInfo.


        :param record_any_channel: The record_any_channel of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._record_any_channel = record_any_channel

    @property
    def keep_up_to(self):
        """Gets the keep_up_to of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The keep_up_to of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: int
        """
        return self._keep_up_to

    @keep_up_to.setter
    def keep_up_to(self, keep_up_to):
        """Sets the keep_up_to of this LiveTvSeriesTimerInfo.


        :param keep_up_to: The keep_up_to of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: int
        """

        self._keep_up_to = keep_up_to

    @property
    def keep_until(self):
        """Gets the keep_until of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The keep_until of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._keep_until

    @keep_until.setter
    def keep_until(self, keep_until):
        """Sets the keep_until of this LiveTvSeriesTimerInfo.


        :param keep_until: The keep_until of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UntilDeleted", "UntilSpaceNeeded", "UntilWatched", "UntilDate"]  # noqa: E501
        if keep_until not in allowed_values:
            raise ValueError(
                "Invalid value for `keep_until` ({0}), must be one of {1}"  # noqa: E501
                .format(keep_until, allowed_values)
            )

        self._keep_until = keep_until

    @property
    def skip_episodes_in_library(self):
        """Gets the skip_episodes_in_library of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The skip_episodes_in_library of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._skip_episodes_in_library

    @skip_episodes_in_library.setter
    def skip_episodes_in_library(self, skip_episodes_in_library):
        """Sets the skip_episodes_in_library of this LiveTvSeriesTimerInfo.


        :param skip_episodes_in_library: The skip_episodes_in_library of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._skip_episodes_in_library = skip_episodes_in_library

    @property
    def record_new_only(self):
        """Gets the record_new_only of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The record_new_only of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._record_new_only

    @record_new_only.setter
    def record_new_only(self, record_new_only):
        """Sets the record_new_only of this LiveTvSeriesTimerInfo.


        :param record_new_only: The record_new_only of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._record_new_only = record_new_only

    @property
    def days(self):
        """Gets the days of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The days of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this LiveTvSeriesTimerInfo.


        :param days: The days of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]  # noqa: E501
        if not set(days).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `days` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(days) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._days = days

    @property
    def priority(self):
        """Gets the priority of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The priority of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this LiveTvSeriesTimerInfo.


        :param priority: The priority of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def pre_padding_seconds(self):
        """Gets the pre_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The pre_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_padding_seconds

    @pre_padding_seconds.setter
    def pre_padding_seconds(self, pre_padding_seconds):
        """Sets the pre_padding_seconds of this LiveTvSeriesTimerInfo.


        :param pre_padding_seconds: The pre_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: int
        """

        self._pre_padding_seconds = pre_padding_seconds

    @property
    def post_padding_seconds(self):
        """Gets the post_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The post_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: int
        """
        return self._post_padding_seconds

    @post_padding_seconds.setter
    def post_padding_seconds(self, post_padding_seconds):
        """Sets the post_padding_seconds of this LiveTvSeriesTimerInfo.


        :param post_padding_seconds: The post_padding_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: int
        """

        self._post_padding_seconds = post_padding_seconds

    @property
    def is_pre_padding_required(self):
        """Gets the is_pre_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The is_pre_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_pre_padding_required

    @is_pre_padding_required.setter
    def is_pre_padding_required(self, is_pre_padding_required):
        """Sets the is_pre_padding_required of this LiveTvSeriesTimerInfo.


        :param is_pre_padding_required: The is_pre_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._is_pre_padding_required = is_pre_padding_required

    @property
    def is_post_padding_required(self):
        """Gets the is_post_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The is_post_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_post_padding_required

    @is_post_padding_required.setter
    def is_post_padding_required(self, is_post_padding_required):
        """Sets the is_post_padding_required of this LiveTvSeriesTimerInfo.


        :param is_post_padding_required: The is_post_padding_required of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: bool
        """

        self._is_post_padding_required = is_post_padding_required

    @property
    def series_id(self):
        """Gets the series_id of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The series_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: str
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this LiveTvSeriesTimerInfo.


        :param series_id: The series_id of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: str
        """

        self._series_id = series_id

    @property
    def provider_ids(self):
        """Gets the provider_ids of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The provider_ids of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: list[object]
        """
        return self._provider_ids

    @provider_ids.setter
    def provider_ids(self, provider_ids):
        """Sets the provider_ids of this LiveTvSeriesTimerInfo.


        :param provider_ids: The provider_ids of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: list[object]
        """

        self._provider_ids = provider_ids

    @property
    def max_recording_seconds(self):
        """Gets the max_recording_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501


        :return: The max_recording_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_recording_seconds

    @max_recording_seconds.setter
    def max_recording_seconds(self, max_recording_seconds):
        """Sets the max_recording_seconds of this LiveTvSeriesTimerInfo.


        :param max_recording_seconds: The max_recording_seconds of this LiveTvSeriesTimerInfo.  # noqa: E501
        :type: int
        """

        self._max_recording_seconds = max_recording_seconds

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
        if issubclass(LiveTvSeriesTimerInfo, dict):
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
        if not isinstance(other, LiveTvSeriesTimerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
