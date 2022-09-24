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

class LiveTvTimerInfoDto(object):
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
        'status': 'str',
        'series_timer_id': 'str',
        'run_time_ticks': 'int',
        'program_info': 'BaseItemDto',
        'timer_type': 'str',
        'id': 'str',
        'type': 'str',
        'server_id': 'str',
        'channel_id': 'str',
        'channel_name': 'str',
        'channel_primary_image_tag': 'str',
        'program_id': 'str',
        'name': 'str',
        'overview': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'priority': 'int',
        'pre_padding_seconds': 'int',
        'post_padding_seconds': 'int',
        'is_pre_padding_required': 'bool',
        'parent_backdrop_item_id': 'str',
        'parent_backdrop_image_tags': 'list[str]',
        'is_post_padding_required': 'bool',
        'keep_until': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'series_timer_id': 'SeriesTimerId',
        'run_time_ticks': 'RunTimeTicks',
        'program_info': 'ProgramInfo',
        'timer_type': 'TimerType',
        'id': 'Id',
        'type': 'Type',
        'server_id': 'ServerId',
        'channel_id': 'ChannelId',
        'channel_name': 'ChannelName',
        'channel_primary_image_tag': 'ChannelPrimaryImageTag',
        'program_id': 'ProgramId',
        'name': 'Name',
        'overview': 'Overview',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'priority': 'Priority',
        'pre_padding_seconds': 'PrePaddingSeconds',
        'post_padding_seconds': 'PostPaddingSeconds',
        'is_pre_padding_required': 'IsPrePaddingRequired',
        'parent_backdrop_item_id': 'ParentBackdropItemId',
        'parent_backdrop_image_tags': 'ParentBackdropImageTags',
        'is_post_padding_required': 'IsPostPaddingRequired',
        'keep_until': 'KeepUntil'
    }

    def __init__(self, status=None, series_timer_id=None, run_time_ticks=None, program_info=None, timer_type=None, id=None, type=None, server_id=None, channel_id=None, channel_name=None, channel_primary_image_tag=None, program_id=None, name=None, overview=None, start_date=None, end_date=None, priority=None, pre_padding_seconds=None, post_padding_seconds=None, is_pre_padding_required=None, parent_backdrop_item_id=None, parent_backdrop_image_tags=None, is_post_padding_required=None, keep_until=None):  # noqa: E501
        """LiveTvTimerInfoDto - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._series_timer_id = None
        self._run_time_ticks = None
        self._program_info = None
        self._timer_type = None
        self._id = None
        self._type = None
        self._server_id = None
        self._channel_id = None
        self._channel_name = None
        self._channel_primary_image_tag = None
        self._program_id = None
        self._name = None
        self._overview = None
        self._start_date = None
        self._end_date = None
        self._priority = None
        self._pre_padding_seconds = None
        self._post_padding_seconds = None
        self._is_pre_padding_required = None
        self._parent_backdrop_item_id = None
        self._parent_backdrop_image_tags = None
        self._is_post_padding_required = None
        self._keep_until = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if series_timer_id is not None:
            self.series_timer_id = series_timer_id
        if run_time_ticks is not None:
            self.run_time_ticks = run_time_ticks
        if program_info is not None:
            self.program_info = program_info
        if timer_type is not None:
            self.timer_type = timer_type
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if server_id is not None:
            self.server_id = server_id
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_name is not None:
            self.channel_name = channel_name
        if channel_primary_image_tag is not None:
            self.channel_primary_image_tag = channel_primary_image_tag
        if program_id is not None:
            self.program_id = program_id
        if name is not None:
            self.name = name
        if overview is not None:
            self.overview = overview
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if priority is not None:
            self.priority = priority
        if pre_padding_seconds is not None:
            self.pre_padding_seconds = pre_padding_seconds
        if post_padding_seconds is not None:
            self.post_padding_seconds = post_padding_seconds
        if is_pre_padding_required is not None:
            self.is_pre_padding_required = is_pre_padding_required
        if parent_backdrop_item_id is not None:
            self.parent_backdrop_item_id = parent_backdrop_item_id
        if parent_backdrop_image_tags is not None:
            self.parent_backdrop_image_tags = parent_backdrop_image_tags
        if is_post_padding_required is not None:
            self.is_post_padding_required = is_post_padding_required
        if keep_until is not None:
            self.keep_until = keep_until

    @property
    def status(self):
        """Gets the status of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The status of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveTvTimerInfoDto.


        :param status: The status of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["New", "InProgress", "Completed", "Cancelled", "ConflictedOk", "ConflictedNotOk", "Error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def series_timer_id(self):
        """Gets the series_timer_id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The series_timer_id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._series_timer_id

    @series_timer_id.setter
    def series_timer_id(self, series_timer_id):
        """Sets the series_timer_id of this LiveTvTimerInfoDto.


        :param series_timer_id: The series_timer_id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._series_timer_id = series_timer_id

    @property
    def run_time_ticks(self):
        """Gets the run_time_ticks of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The run_time_ticks of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._run_time_ticks

    @run_time_ticks.setter
    def run_time_ticks(self, run_time_ticks):
        """Sets the run_time_ticks of this LiveTvTimerInfoDto.


        :param run_time_ticks: The run_time_ticks of this LiveTvTimerInfoDto.  # noqa: E501
        :type: int
        """

        self._run_time_ticks = run_time_ticks

    @property
    def program_info(self):
        """Gets the program_info of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The program_info of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: BaseItemDto
        """
        return self._program_info

    @program_info.setter
    def program_info(self, program_info):
        """Sets the program_info of this LiveTvTimerInfoDto.


        :param program_info: The program_info of this LiveTvTimerInfoDto.  # noqa: E501
        :type: BaseItemDto
        """

        self._program_info = program_info

    @property
    def timer_type(self):
        """Gets the timer_type of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The timer_type of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._timer_type

    @timer_type.setter
    def timer_type(self, timer_type):
        """Sets the timer_type of this LiveTvTimerInfoDto.


        :param timer_type: The timer_type of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Program", "DateTime", "Keyword"]  # noqa: E501
        if timer_type not in allowed_values:
            raise ValueError(
                "Invalid value for `timer_type` ({0}), must be one of {1}"  # noqa: E501
                .format(timer_type, allowed_values)
            )

        self._timer_type = timer_type

    @property
    def id(self):
        """Gets the id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveTvTimerInfoDto.


        :param id: The id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The type of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LiveTvTimerInfoDto.


        :param type: The type of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def server_id(self):
        """Gets the server_id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The server_id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this LiveTvTimerInfoDto.


        :param server_id: The server_id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def channel_id(self):
        """Gets the channel_id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The channel_id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this LiveTvTimerInfoDto.


        :param channel_id: The channel_id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def channel_name(self):
        """Gets the channel_name of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The channel_name of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this LiveTvTimerInfoDto.


        :param channel_name: The channel_name of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._channel_name = channel_name

    @property
    def channel_primary_image_tag(self):
        """Gets the channel_primary_image_tag of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The channel_primary_image_tag of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._channel_primary_image_tag

    @channel_primary_image_tag.setter
    def channel_primary_image_tag(self, channel_primary_image_tag):
        """Sets the channel_primary_image_tag of this LiveTvTimerInfoDto.


        :param channel_primary_image_tag: The channel_primary_image_tag of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._channel_primary_image_tag = channel_primary_image_tag

    @property
    def program_id(self):
        """Gets the program_id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The program_id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LiveTvTimerInfoDto.


        :param program_id: The program_id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._program_id = program_id

    @property
    def name(self):
        """Gets the name of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The name of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveTvTimerInfoDto.


        :param name: The name of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def overview(self):
        """Gets the overview of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The overview of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this LiveTvTimerInfoDto.


        :param overview: The overview of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def start_date(self):
        """Gets the start_date of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The start_date of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LiveTvTimerInfoDto.


        :param start_date: The start_date of this LiveTvTimerInfoDto.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The end_date of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this LiveTvTimerInfoDto.


        :param end_date: The end_date of this LiveTvTimerInfoDto.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def priority(self):
        """Gets the priority of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The priority of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this LiveTvTimerInfoDto.


        :param priority: The priority of this LiveTvTimerInfoDto.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def pre_padding_seconds(self):
        """Gets the pre_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The pre_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._pre_padding_seconds

    @pre_padding_seconds.setter
    def pre_padding_seconds(self, pre_padding_seconds):
        """Sets the pre_padding_seconds of this LiveTvTimerInfoDto.


        :param pre_padding_seconds: The pre_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501
        :type: int
        """

        self._pre_padding_seconds = pre_padding_seconds

    @property
    def post_padding_seconds(self):
        """Gets the post_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The post_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._post_padding_seconds

    @post_padding_seconds.setter
    def post_padding_seconds(self, post_padding_seconds):
        """Sets the post_padding_seconds of this LiveTvTimerInfoDto.


        :param post_padding_seconds: The post_padding_seconds of this LiveTvTimerInfoDto.  # noqa: E501
        :type: int
        """

        self._post_padding_seconds = post_padding_seconds

    @property
    def is_pre_padding_required(self):
        """Gets the is_pre_padding_required of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The is_pre_padding_required of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_pre_padding_required

    @is_pre_padding_required.setter
    def is_pre_padding_required(self, is_pre_padding_required):
        """Sets the is_pre_padding_required of this LiveTvTimerInfoDto.


        :param is_pre_padding_required: The is_pre_padding_required of this LiveTvTimerInfoDto.  # noqa: E501
        :type: bool
        """

        self._is_pre_padding_required = is_pre_padding_required

    @property
    def parent_backdrop_item_id(self):
        """Gets the parent_backdrop_item_id of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The parent_backdrop_item_id of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_backdrop_item_id

    @parent_backdrop_item_id.setter
    def parent_backdrop_item_id(self, parent_backdrop_item_id):
        """Sets the parent_backdrop_item_id of this LiveTvTimerInfoDto.


        :param parent_backdrop_item_id: The parent_backdrop_item_id of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """

        self._parent_backdrop_item_id = parent_backdrop_item_id

    @property
    def parent_backdrop_image_tags(self):
        """Gets the parent_backdrop_image_tags of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The parent_backdrop_image_tags of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_backdrop_image_tags

    @parent_backdrop_image_tags.setter
    def parent_backdrop_image_tags(self, parent_backdrop_image_tags):
        """Sets the parent_backdrop_image_tags of this LiveTvTimerInfoDto.


        :param parent_backdrop_image_tags: The parent_backdrop_image_tags of this LiveTvTimerInfoDto.  # noqa: E501
        :type: list[str]
        """

        self._parent_backdrop_image_tags = parent_backdrop_image_tags

    @property
    def is_post_padding_required(self):
        """Gets the is_post_padding_required of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The is_post_padding_required of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_post_padding_required

    @is_post_padding_required.setter
    def is_post_padding_required(self, is_post_padding_required):
        """Sets the is_post_padding_required of this LiveTvTimerInfoDto.


        :param is_post_padding_required: The is_post_padding_required of this LiveTvTimerInfoDto.  # noqa: E501
        :type: bool
        """

        self._is_post_padding_required = is_post_padding_required

    @property
    def keep_until(self):
        """Gets the keep_until of this LiveTvTimerInfoDto.  # noqa: E501


        :return: The keep_until of this LiveTvTimerInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._keep_until

    @keep_until.setter
    def keep_until(self, keep_until):
        """Sets the keep_until of this LiveTvTimerInfoDto.


        :param keep_until: The keep_until of this LiveTvTimerInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["UntilDeleted", "UntilSpaceNeeded", "UntilWatched", "UntilDate"]  # noqa: E501
        if keep_until not in allowed_values:
            raise ValueError(
                "Invalid value for `keep_until` ({0}), must be one of {1}"  # noqa: E501
                .format(keep_until, allowed_values)
            )

        self._keep_until = keep_until

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
        if issubclass(LiveTvTimerInfoDto, dict):
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
        if not isinstance(other, LiveTvTimerInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
