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

class TranscodingVpStepInfo(object):
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
        'step_type': 'TranscodingVpStepTypes',
        'step_type_name': 'str',
        'hardware_context_name': 'str',
        'is_hardware_context': 'bool',
        'name': 'str',
        'short': 'str',
        'ffmpeg_name': 'str',
        'ffmpeg_description': 'str',
        'ffmpeg_options': 'str',
        'param': 'str',
        'param_short': 'str'
    }

    attribute_map = {
        'step_type': 'StepType',
        'step_type_name': 'StepTypeName',
        'hardware_context_name': 'HardwareContextName',
        'is_hardware_context': 'IsHardwareContext',
        'name': 'Name',
        'short': 'Short',
        'ffmpeg_name': 'FfmpegName',
        'ffmpeg_description': 'FfmpegDescription',
        'ffmpeg_options': 'FfmpegOptions',
        'param': 'Param',
        'param_short': 'ParamShort'
    }

    def __init__(self, step_type=None, step_type_name=None, hardware_context_name=None, is_hardware_context=None, name=None, short=None, ffmpeg_name=None, ffmpeg_description=None, ffmpeg_options=None, param=None, param_short=None):  # noqa: E501
        """TranscodingVpStepInfo - a model defined in Swagger"""  # noqa: E501
        self._step_type = None
        self._step_type_name = None
        self._hardware_context_name = None
        self._is_hardware_context = None
        self._name = None
        self._short = None
        self._ffmpeg_name = None
        self._ffmpeg_description = None
        self._ffmpeg_options = None
        self._param = None
        self._param_short = None
        self.discriminator = None
        if step_type is not None:
            self.step_type = step_type
        if step_type_name is not None:
            self.step_type_name = step_type_name
        if hardware_context_name is not None:
            self.hardware_context_name = hardware_context_name
        if is_hardware_context is not None:
            self.is_hardware_context = is_hardware_context
        if name is not None:
            self.name = name
        if short is not None:
            self.short = short
        if ffmpeg_name is not None:
            self.ffmpeg_name = ffmpeg_name
        if ffmpeg_description is not None:
            self.ffmpeg_description = ffmpeg_description
        if ffmpeg_options is not None:
            self.ffmpeg_options = ffmpeg_options
        if param is not None:
            self.param = param
        if param_short is not None:
            self.param_short = param_short

    @property
    def step_type(self):
        """Gets the step_type of this TranscodingVpStepInfo.  # noqa: E501


        :return: The step_type of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: TranscodingVpStepTypes
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """Sets the step_type of this TranscodingVpStepInfo.


        :param step_type: The step_type of this TranscodingVpStepInfo.  # noqa: E501
        :type: TranscodingVpStepTypes
        """

        self._step_type = step_type

    @property
    def step_type_name(self):
        """Gets the step_type_name of this TranscodingVpStepInfo.  # noqa: E501


        :return: The step_type_name of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._step_type_name

    @step_type_name.setter
    def step_type_name(self, step_type_name):
        """Sets the step_type_name of this TranscodingVpStepInfo.


        :param step_type_name: The step_type_name of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._step_type_name = step_type_name

    @property
    def hardware_context_name(self):
        """Gets the hardware_context_name of this TranscodingVpStepInfo.  # noqa: E501


        :return: The hardware_context_name of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_context_name

    @hardware_context_name.setter
    def hardware_context_name(self, hardware_context_name):
        """Sets the hardware_context_name of this TranscodingVpStepInfo.


        :param hardware_context_name: The hardware_context_name of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._hardware_context_name = hardware_context_name

    @property
    def is_hardware_context(self):
        """Gets the is_hardware_context of this TranscodingVpStepInfo.  # noqa: E501


        :return: The is_hardware_context of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_hardware_context

    @is_hardware_context.setter
    def is_hardware_context(self, is_hardware_context):
        """Sets the is_hardware_context of this TranscodingVpStepInfo.


        :param is_hardware_context: The is_hardware_context of this TranscodingVpStepInfo.  # noqa: E501
        :type: bool
        """

        self._is_hardware_context = is_hardware_context

    @property
    def name(self):
        """Gets the name of this TranscodingVpStepInfo.  # noqa: E501


        :return: The name of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TranscodingVpStepInfo.


        :param name: The name of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short(self):
        """Gets the short of this TranscodingVpStepInfo.  # noqa: E501


        :return: The short of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this TranscodingVpStepInfo.


        :param short: The short of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._short = short

    @property
    def ffmpeg_name(self):
        """Gets the ffmpeg_name of this TranscodingVpStepInfo.  # noqa: E501


        :return: The ffmpeg_name of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._ffmpeg_name

    @ffmpeg_name.setter
    def ffmpeg_name(self, ffmpeg_name):
        """Sets the ffmpeg_name of this TranscodingVpStepInfo.


        :param ffmpeg_name: The ffmpeg_name of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._ffmpeg_name = ffmpeg_name

    @property
    def ffmpeg_description(self):
        """Gets the ffmpeg_description of this TranscodingVpStepInfo.  # noqa: E501


        :return: The ffmpeg_description of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._ffmpeg_description

    @ffmpeg_description.setter
    def ffmpeg_description(self, ffmpeg_description):
        """Sets the ffmpeg_description of this TranscodingVpStepInfo.


        :param ffmpeg_description: The ffmpeg_description of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._ffmpeg_description = ffmpeg_description

    @property
    def ffmpeg_options(self):
        """Gets the ffmpeg_options of this TranscodingVpStepInfo.  # noqa: E501


        :return: The ffmpeg_options of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._ffmpeg_options

    @ffmpeg_options.setter
    def ffmpeg_options(self, ffmpeg_options):
        """Sets the ffmpeg_options of this TranscodingVpStepInfo.


        :param ffmpeg_options: The ffmpeg_options of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._ffmpeg_options = ffmpeg_options

    @property
    def param(self):
        """Gets the param of this TranscodingVpStepInfo.  # noqa: E501


        :return: The param of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this TranscodingVpStepInfo.


        :param param: The param of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._param = param

    @property
    def param_short(self):
        """Gets the param_short of this TranscodingVpStepInfo.  # noqa: E501


        :return: The param_short of this TranscodingVpStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._param_short

    @param_short.setter
    def param_short(self, param_short):
        """Sets the param_short of this TranscodingVpStepInfo.


        :param param_short: The param_short of this TranscodingVpStepInfo.  # noqa: E501
        :type: str
        """

        self._param_short = param_short

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
        if issubclass(TranscodingVpStepInfo, dict):
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
        if not isinstance(other, TranscodingVpStepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
