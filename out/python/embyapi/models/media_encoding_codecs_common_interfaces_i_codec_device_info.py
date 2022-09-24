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

class MediaEncodingCodecsCommonInterfacesICodecDeviceInfo(object):
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
        'capabilities': 'MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities',
        'adapter': 'int',
        'name': 'str',
        'desription': 'str',
        'driver': 'str',
        'driver_version': 'Version',
        'api_version': 'Version',
        'vendor_id': 'int',
        'device_id': 'int',
        'device_identifier': 'str',
        'hardware_context_framework': 'str',
        'dev_path': 'str',
        'drm_node': 'str',
        'vendor_name': 'str',
        'device_name': 'str'
    }

    attribute_map = {
        'capabilities': 'Capabilities',
        'adapter': 'Adapter',
        'name': 'Name',
        'desription': 'Desription',
        'driver': 'Driver',
        'driver_version': 'DriverVersion',
        'api_version': 'ApiVersion',
        'vendor_id': 'VendorId',
        'device_id': 'DeviceId',
        'device_identifier': 'DeviceIdentifier',
        'hardware_context_framework': 'HardwareContextFramework',
        'dev_path': 'DevPath',
        'drm_node': 'DrmNode',
        'vendor_name': 'VendorName',
        'device_name': 'DeviceName'
    }

    def __init__(self, capabilities=None, adapter=None, name=None, desription=None, driver=None, driver_version=None, api_version=None, vendor_id=None, device_id=None, device_identifier=None, hardware_context_framework=None, dev_path=None, drm_node=None, vendor_name=None, device_name=None):  # noqa: E501
        """MediaEncodingCodecsCommonInterfacesICodecDeviceInfo - a model defined in Swagger"""  # noqa: E501
        self._capabilities = None
        self._adapter = None
        self._name = None
        self._desription = None
        self._driver = None
        self._driver_version = None
        self._api_version = None
        self._vendor_id = None
        self._device_id = None
        self._device_identifier = None
        self._hardware_context_framework = None
        self._dev_path = None
        self._drm_node = None
        self._vendor_name = None
        self._device_name = None
        self.discriminator = None
        if capabilities is not None:
            self.capabilities = capabilities
        if adapter is not None:
            self.adapter = adapter
        if name is not None:
            self.name = name
        if desription is not None:
            self.desription = desription
        if driver is not None:
            self.driver = driver
        if driver_version is not None:
            self.driver_version = driver_version
        if api_version is not None:
            self.api_version = api_version
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if device_id is not None:
            self.device_id = device_id
        if device_identifier is not None:
            self.device_identifier = device_identifier
        if hardware_context_framework is not None:
            self.hardware_context_framework = hardware_context_framework
        if dev_path is not None:
            self.dev_path = dev_path
        if drm_node is not None:
            self.drm_node = drm_node
        if vendor_name is not None:
            self.vendor_name = vendor_name
        if device_name is not None:
            self.device_name = device_name

    @property
    def capabilities(self):
        """Gets the capabilities of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The capabilities of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param capabilities: The capabilities of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities
        """

        self._capabilities = capabilities

    @property
    def adapter(self):
        """Gets the adapter of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The adapter of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: int
        """
        return self._adapter

    @adapter.setter
    def adapter(self, adapter):
        """Sets the adapter of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param adapter: The adapter of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: int
        """

        self._adapter = adapter

    @property
    def name(self):
        """Gets the name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param name: The name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desription(self):
        """Gets the desription of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The desription of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._desription

    @desription.setter
    def desription(self, desription):
        """Sets the desription of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param desription: The desription of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._desription = desription

    @property
    def driver(self):
        """Gets the driver of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The driver of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param driver: The driver of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def driver_version(self):
        """Gets the driver_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The driver_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: Version
        """
        return self._driver_version

    @driver_version.setter
    def driver_version(self, driver_version):
        """Sets the driver_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param driver_version: The driver_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: Version
        """

        self._driver_version = driver_version

    @property
    def api_version(self):
        """Gets the api_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The api_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: Version
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param api_version: The api_version of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: Version
        """

        self._api_version = api_version

    @property
    def vendor_id(self):
        """Gets the vendor_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The vendor_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param vendor_id: The vendor_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def device_id(self):
        """Gets the device_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The device_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param device_id: The device_id of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_identifier(self):
        """Gets the device_identifier of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The device_identifier of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_identifier

    @device_identifier.setter
    def device_identifier(self, device_identifier):
        """Sets the device_identifier of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param device_identifier: The device_identifier of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._device_identifier = device_identifier

    @property
    def hardware_context_framework(self):
        """Gets the hardware_context_framework of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The hardware_context_framework of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_context_framework

    @hardware_context_framework.setter
    def hardware_context_framework(self, hardware_context_framework):
        """Sets the hardware_context_framework of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param hardware_context_framework: The hardware_context_framework of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "None", "AmdAmf", "MediaCodec", "NvEncDec", "OpenMax", "QuickSync", "VaApi", "V4L2", "DxVa", "D3d11va", "VideoToolbox", "Mmal"]  # noqa: E501
        if hardware_context_framework not in allowed_values:
            raise ValueError(
                "Invalid value for `hardware_context_framework` ({0}), must be one of {1}"  # noqa: E501
                .format(hardware_context_framework, allowed_values)
            )

        self._hardware_context_framework = hardware_context_framework

    @property
    def dev_path(self):
        """Gets the dev_path of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The dev_path of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._dev_path

    @dev_path.setter
    def dev_path(self, dev_path):
        """Sets the dev_path of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param dev_path: The dev_path of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._dev_path = dev_path

    @property
    def drm_node(self):
        """Gets the drm_node of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The drm_node of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._drm_node

    @drm_node.setter
    def drm_node(self, drm_node):
        """Sets the drm_node of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param drm_node: The drm_node of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._drm_node = drm_node

    @property
    def vendor_name(self):
        """Gets the vendor_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The vendor_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param vendor_name: The vendor_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._vendor_name = vendor_name

    @property
    def device_name(self):
        """Gets the device_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501


        :return: The device_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.


        :param device_name: The device_name of this MediaEncodingCodecsCommonInterfacesICodecDeviceInfo.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

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
        if issubclass(MediaEncodingCodecsCommonInterfacesICodecDeviceInfo, dict):
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
        if not isinstance(other, MediaEncodingCodecsCommonInterfacesICodecDeviceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
