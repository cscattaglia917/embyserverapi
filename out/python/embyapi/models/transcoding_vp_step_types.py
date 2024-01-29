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

class TranscodingVpStepTypes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DECODER = "Decoder"
    ENCODER = "Encoder"
    SCALING = "Scaling"
    DEINTERLACE = "Deinterlace"
    SUBTITLEOVERLAY = "SubtitleOverlay"
    TONEMAPPING = "ToneMapping"
    COLORCONVERSION = "ColorConversion"
    SPLITCAPTIONS = "SplitCaptions"
    TEXTSUB2VIDEO = "TextSub2Video"
    GRAPHICSUB2VIDEO = "GraphicSub2Video"
    GRAPHICSUB2TEXT = "GraphicSub2Text"
    BURNINTEXTSUBS = "BurnInTextSubs"
    BURNINGRAPHICSUBS = "BurnInGraphicSubs"
    SCALESUBS = "ScaleSubs"
    TEXTMOD = "TextMod"
    CENSOR = "Censor"
    SHOWSPEAKER = "ShowSpeaker"
    STRIPSTYLES = "StripStyles"
    CONNECTTO = "ConnectTo"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """TranscodingVpStepTypes - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(TranscodingVpStepTypes, dict):
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
        if not isinstance(other, TranscodingVpStepTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
