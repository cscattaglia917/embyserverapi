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

class SyncModelSyncJobCreationResult(object):
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
        'job': 'SyncSyncJob',
        'job_items': 'list[SyncModelSyncJobItem]'
    }

    attribute_map = {
        'job': 'Job',
        'job_items': 'JobItems'
    }

    def __init__(self, job=None, job_items=None):  # noqa: E501
        """SyncModelSyncJobCreationResult - a model defined in Swagger"""  # noqa: E501
        self._job = None
        self._job_items = None
        self.discriminator = None
        if job is not None:
            self.job = job
        if job_items is not None:
            self.job_items = job_items

    @property
    def job(self):
        """Gets the job of this SyncModelSyncJobCreationResult.  # noqa: E501


        :return: The job of this SyncModelSyncJobCreationResult.  # noqa: E501
        :rtype: SyncSyncJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this SyncModelSyncJobCreationResult.


        :param job: The job of this SyncModelSyncJobCreationResult.  # noqa: E501
        :type: SyncSyncJob
        """

        self._job = job

    @property
    def job_items(self):
        """Gets the job_items of this SyncModelSyncJobCreationResult.  # noqa: E501


        :return: The job_items of this SyncModelSyncJobCreationResult.  # noqa: E501
        :rtype: list[SyncModelSyncJobItem]
        """
        return self._job_items

    @job_items.setter
    def job_items(self, job_items):
        """Sets the job_items of this SyncModelSyncJobCreationResult.


        :param job_items: The job_items of this SyncModelSyncJobCreationResult.  # noqa: E501
        :type: list[SyncModelSyncJobItem]
        """

        self._job_items = job_items

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
        if issubclass(SyncModelSyncJobCreationResult, dict):
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
        if not isinstance(other, SyncModelSyncJobCreationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
