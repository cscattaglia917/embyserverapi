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

class MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities(object):
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
        'supports_hw_upload': 'bool',
        'supports_hw_download': 'bool',
        'supports_standalone_device_init': 'bool',
        'supports10_bit_processing': 'bool',
        'supports_native_tone_mapping': 'bool'
    }

    attribute_map = {
        'supports_hw_upload': 'SupportsHwUpload',
        'supports_hw_download': 'SupportsHwDownload',
        'supports_standalone_device_init': 'SupportsStandaloneDeviceInit',
        'supports10_bit_processing': 'Supports10BitProcessing',
        'supports_native_tone_mapping': 'SupportsNativeToneMapping'
    }

    def __init__(self, supports_hw_upload=None, supports_hw_download=None, supports_standalone_device_init=None, supports10_bit_processing=None, supports_native_tone_mapping=None):  # noqa: E501
        """MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities - a model defined in Swagger"""  # noqa: E501
        self._supports_hw_upload = None
        self._supports_hw_download = None
        self._supports_standalone_device_init = None
        self._supports10_bit_processing = None
        self._supports_native_tone_mapping = None
        self.discriminator = None
        if supports_hw_upload is not None:
            self.supports_hw_upload = supports_hw_upload
        if supports_hw_download is not None:
            self.supports_hw_download = supports_hw_download
        if supports_standalone_device_init is not None:
            self.supports_standalone_device_init = supports_standalone_device_init
        if supports10_bit_processing is not None:
            self.supports10_bit_processing = supports10_bit_processing
        if supports_native_tone_mapping is not None:
            self.supports_native_tone_mapping = supports_native_tone_mapping

    @property
    def supports_hw_upload(self):
        """Gets the supports_hw_upload of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501


        :return: The supports_hw_upload of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports_hw_upload

    @supports_hw_upload.setter
    def supports_hw_upload(self, supports_hw_upload):
        """Sets the supports_hw_upload of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.


        :param supports_hw_upload: The supports_hw_upload of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :type: bool
        """

        self._supports_hw_upload = supports_hw_upload

    @property
    def supports_hw_download(self):
        """Gets the supports_hw_download of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501


        :return: The supports_hw_download of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports_hw_download

    @supports_hw_download.setter
    def supports_hw_download(self, supports_hw_download):
        """Sets the supports_hw_download of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.


        :param supports_hw_download: The supports_hw_download of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :type: bool
        """

        self._supports_hw_download = supports_hw_download

    @property
    def supports_standalone_device_init(self):
        """Gets the supports_standalone_device_init of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501


        :return: The supports_standalone_device_init of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports_standalone_device_init

    @supports_standalone_device_init.setter
    def supports_standalone_device_init(self, supports_standalone_device_init):
        """Sets the supports_standalone_device_init of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.


        :param supports_standalone_device_init: The supports_standalone_device_init of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :type: bool
        """

        self._supports_standalone_device_init = supports_standalone_device_init

    @property
    def supports10_bit_processing(self):
        """Gets the supports10_bit_processing of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501


        :return: The supports10_bit_processing of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports10_bit_processing

    @supports10_bit_processing.setter
    def supports10_bit_processing(self, supports10_bit_processing):
        """Sets the supports10_bit_processing of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.


        :param supports10_bit_processing: The supports10_bit_processing of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :type: bool
        """

        self._supports10_bit_processing = supports10_bit_processing

    @property
    def supports_native_tone_mapping(self):
        """Gets the supports_native_tone_mapping of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501


        :return: The supports_native_tone_mapping of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports_native_tone_mapping

    @supports_native_tone_mapping.setter
    def supports_native_tone_mapping(self, supports_native_tone_mapping):
        """Sets the supports_native_tone_mapping of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.


        :param supports_native_tone_mapping: The supports_native_tone_mapping of this MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities.  # noqa: E501
        :type: bool
        """

        self._supports_native_tone_mapping = supports_native_tone_mapping

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
        if issubclass(MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities, dict):
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
        if not isinstance(other, MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
