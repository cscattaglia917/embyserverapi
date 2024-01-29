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

class UpdatesPackageInfo(object):
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
        'name': 'str',
        'short_description': 'str',
        'overview': 'str',
        'is_premium': 'bool',
        'adult': 'bool',
        'rich_desc_url': 'str',
        'thumb_image': 'str',
        'preview_image': 'str',
        'type': 'str',
        'target_filename': 'str',
        'owner': 'str',
        'category': 'str',
        'tile_color': 'str',
        'feature_id': 'str',
        'reg_info': 'str',
        'price': 'float',
        'target_system': 'UpdatesPackageTargetSystem',
        'guid': 'str',
        'total_ratings': 'int',
        'avg_rating': 'float',
        'is_registered': 'bool',
        'exp_date': 'datetime',
        'versions': 'list[UpdatesPackageVersionInfo]',
        'enable_in_app_store': 'bool',
        'installs': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'short_description': 'shortDescription',
        'overview': 'overview',
        'is_premium': 'isPremium',
        'adult': 'adult',
        'rich_desc_url': 'richDescUrl',
        'thumb_image': 'thumbImage',
        'preview_image': 'previewImage',
        'type': 'type',
        'target_filename': 'targetFilename',
        'owner': 'owner',
        'category': 'category',
        'tile_color': 'tileColor',
        'feature_id': 'featureId',
        'reg_info': 'regInfo',
        'price': 'price',
        'target_system': 'targetSystem',
        'guid': 'guid',
        'total_ratings': 'totalRatings',
        'avg_rating': 'avgRating',
        'is_registered': 'isRegistered',
        'exp_date': 'expDate',
        'versions': 'versions',
        'enable_in_app_store': 'enableInAppStore',
        'installs': 'installs'
    }

    def __init__(self, id=None, name=None, short_description=None, overview=None, is_premium=None, adult=None, rich_desc_url=None, thumb_image=None, preview_image=None, type=None, target_filename=None, owner=None, category=None, tile_color=None, feature_id=None, reg_info=None, price=None, target_system=None, guid=None, total_ratings=None, avg_rating=None, is_registered=None, exp_date=None, versions=None, enable_in_app_store=None, installs=None):  # noqa: E501
        """UpdatesPackageInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._short_description = None
        self._overview = None
        self._is_premium = None
        self._adult = None
        self._rich_desc_url = None
        self._thumb_image = None
        self._preview_image = None
        self._type = None
        self._target_filename = None
        self._owner = None
        self._category = None
        self._tile_color = None
        self._feature_id = None
        self._reg_info = None
        self._price = None
        self._target_system = None
        self._guid = None
        self._total_ratings = None
        self._avg_rating = None
        self._is_registered = None
        self._exp_date = None
        self._versions = None
        self._enable_in_app_store = None
        self._installs = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if short_description is not None:
            self.short_description = short_description
        if overview is not None:
            self.overview = overview
        if is_premium is not None:
            self.is_premium = is_premium
        if adult is not None:
            self.adult = adult
        if rich_desc_url is not None:
            self.rich_desc_url = rich_desc_url
        if thumb_image is not None:
            self.thumb_image = thumb_image
        if preview_image is not None:
            self.preview_image = preview_image
        if type is not None:
            self.type = type
        if target_filename is not None:
            self.target_filename = target_filename
        if owner is not None:
            self.owner = owner
        if category is not None:
            self.category = category
        if tile_color is not None:
            self.tile_color = tile_color
        if feature_id is not None:
            self.feature_id = feature_id
        if reg_info is not None:
            self.reg_info = reg_info
        if price is not None:
            self.price = price
        if target_system is not None:
            self.target_system = target_system
        if guid is not None:
            self.guid = guid
        if total_ratings is not None:
            self.total_ratings = total_ratings
        if avg_rating is not None:
            self.avg_rating = avg_rating
        if is_registered is not None:
            self.is_registered = is_registered
        if exp_date is not None:
            self.exp_date = exp_date
        if versions is not None:
            self.versions = versions
        if enable_in_app_store is not None:
            self.enable_in_app_store = enable_in_app_store
        if installs is not None:
            self.installs = installs

    @property
    def id(self):
        """Gets the id of this UpdatesPackageInfo.  # noqa: E501


        :return: The id of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatesPackageInfo.


        :param id: The id of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdatesPackageInfo.  # noqa: E501


        :return: The name of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatesPackageInfo.


        :param name: The name of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_description(self):
        """Gets the short_description of this UpdatesPackageInfo.  # noqa: E501


        :return: The short_description of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this UpdatesPackageInfo.


        :param short_description: The short_description of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def overview(self):
        """Gets the overview of this UpdatesPackageInfo.  # noqa: E501


        :return: The overview of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this UpdatesPackageInfo.


        :param overview: The overview of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def is_premium(self):
        """Gets the is_premium of this UpdatesPackageInfo.  # noqa: E501


        :return: The is_premium of this UpdatesPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_premium

    @is_premium.setter
    def is_premium(self, is_premium):
        """Sets the is_premium of this UpdatesPackageInfo.


        :param is_premium: The is_premium of this UpdatesPackageInfo.  # noqa: E501
        :type: bool
        """

        self._is_premium = is_premium

    @property
    def adult(self):
        """Gets the adult of this UpdatesPackageInfo.  # noqa: E501


        :return: The adult of this UpdatesPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._adult

    @adult.setter
    def adult(self, adult):
        """Sets the adult of this UpdatesPackageInfo.


        :param adult: The adult of this UpdatesPackageInfo.  # noqa: E501
        :type: bool
        """

        self._adult = adult

    @property
    def rich_desc_url(self):
        """Gets the rich_desc_url of this UpdatesPackageInfo.  # noqa: E501


        :return: The rich_desc_url of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._rich_desc_url

    @rich_desc_url.setter
    def rich_desc_url(self, rich_desc_url):
        """Sets the rich_desc_url of this UpdatesPackageInfo.


        :param rich_desc_url: The rich_desc_url of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._rich_desc_url = rich_desc_url

    @property
    def thumb_image(self):
        """Gets the thumb_image of this UpdatesPackageInfo.  # noqa: E501


        :return: The thumb_image of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumb_image

    @thumb_image.setter
    def thumb_image(self, thumb_image):
        """Sets the thumb_image of this UpdatesPackageInfo.


        :param thumb_image: The thumb_image of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._thumb_image = thumb_image

    @property
    def preview_image(self):
        """Gets the preview_image of this UpdatesPackageInfo.  # noqa: E501


        :return: The preview_image of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._preview_image

    @preview_image.setter
    def preview_image(self, preview_image):
        """Sets the preview_image of this UpdatesPackageInfo.


        :param preview_image: The preview_image of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._preview_image = preview_image

    @property
    def type(self):
        """Gets the type of this UpdatesPackageInfo.  # noqa: E501


        :return: The type of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatesPackageInfo.


        :param type: The type of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def target_filename(self):
        """Gets the target_filename of this UpdatesPackageInfo.  # noqa: E501


        :return: The target_filename of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_filename

    @target_filename.setter
    def target_filename(self, target_filename):
        """Sets the target_filename of this UpdatesPackageInfo.


        :param target_filename: The target_filename of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._target_filename = target_filename

    @property
    def owner(self):
        """Gets the owner of this UpdatesPackageInfo.  # noqa: E501


        :return: The owner of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdatesPackageInfo.


        :param owner: The owner of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def category(self):
        """Gets the category of this UpdatesPackageInfo.  # noqa: E501


        :return: The category of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdatesPackageInfo.


        :param category: The category of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def tile_color(self):
        """Gets the tile_color of this UpdatesPackageInfo.  # noqa: E501


        :return: The tile_color of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._tile_color

    @tile_color.setter
    def tile_color(self, tile_color):
        """Sets the tile_color of this UpdatesPackageInfo.


        :param tile_color: The tile_color of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._tile_color = tile_color

    @property
    def feature_id(self):
        """Gets the feature_id of this UpdatesPackageInfo.  # noqa: E501


        :return: The feature_id of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this UpdatesPackageInfo.


        :param feature_id: The feature_id of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def reg_info(self):
        """Gets the reg_info of this UpdatesPackageInfo.  # noqa: E501


        :return: The reg_info of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._reg_info

    @reg_info.setter
    def reg_info(self, reg_info):
        """Sets the reg_info of this UpdatesPackageInfo.


        :param reg_info: The reg_info of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._reg_info = reg_info

    @property
    def price(self):
        """Gets the price of this UpdatesPackageInfo.  # noqa: E501


        :return: The price of this UpdatesPackageInfo.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this UpdatesPackageInfo.


        :param price: The price of this UpdatesPackageInfo.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def target_system(self):
        """Gets the target_system of this UpdatesPackageInfo.  # noqa: E501


        :return: The target_system of this UpdatesPackageInfo.  # noqa: E501
        :rtype: UpdatesPackageTargetSystem
        """
        return self._target_system

    @target_system.setter
    def target_system(self, target_system):
        """Sets the target_system of this UpdatesPackageInfo.


        :param target_system: The target_system of this UpdatesPackageInfo.  # noqa: E501
        :type: UpdatesPackageTargetSystem
        """

        self._target_system = target_system

    @property
    def guid(self):
        """Gets the guid of this UpdatesPackageInfo.  # noqa: E501


        :return: The guid of this UpdatesPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this UpdatesPackageInfo.


        :param guid: The guid of this UpdatesPackageInfo.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def total_ratings(self):
        """Gets the total_ratings of this UpdatesPackageInfo.  # noqa: E501


        :return: The total_ratings of this UpdatesPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_ratings

    @total_ratings.setter
    def total_ratings(self, total_ratings):
        """Sets the total_ratings of this UpdatesPackageInfo.


        :param total_ratings: The total_ratings of this UpdatesPackageInfo.  # noqa: E501
        :type: int
        """

        self._total_ratings = total_ratings

    @property
    def avg_rating(self):
        """Gets the avg_rating of this UpdatesPackageInfo.  # noqa: E501


        :return: The avg_rating of this UpdatesPackageInfo.  # noqa: E501
        :rtype: float
        """
        return self._avg_rating

    @avg_rating.setter
    def avg_rating(self, avg_rating):
        """Sets the avg_rating of this UpdatesPackageInfo.


        :param avg_rating: The avg_rating of this UpdatesPackageInfo.  # noqa: E501
        :type: float
        """

        self._avg_rating = avg_rating

    @property
    def is_registered(self):
        """Gets the is_registered of this UpdatesPackageInfo.  # noqa: E501


        :return: The is_registered of this UpdatesPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this UpdatesPackageInfo.


        :param is_registered: The is_registered of this UpdatesPackageInfo.  # noqa: E501
        :type: bool
        """

        self._is_registered = is_registered

    @property
    def exp_date(self):
        """Gets the exp_date of this UpdatesPackageInfo.  # noqa: E501


        :return: The exp_date of this UpdatesPackageInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        """Sets the exp_date of this UpdatesPackageInfo.


        :param exp_date: The exp_date of this UpdatesPackageInfo.  # noqa: E501
        :type: datetime
        """

        self._exp_date = exp_date

    @property
    def versions(self):
        """Gets the versions of this UpdatesPackageInfo.  # noqa: E501


        :return: The versions of this UpdatesPackageInfo.  # noqa: E501
        :rtype: list[UpdatesPackageVersionInfo]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this UpdatesPackageInfo.


        :param versions: The versions of this UpdatesPackageInfo.  # noqa: E501
        :type: list[UpdatesPackageVersionInfo]
        """

        self._versions = versions

    @property
    def enable_in_app_store(self):
        """Gets the enable_in_app_store of this UpdatesPackageInfo.  # noqa: E501


        :return: The enable_in_app_store of this UpdatesPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable_in_app_store

    @enable_in_app_store.setter
    def enable_in_app_store(self, enable_in_app_store):
        """Sets the enable_in_app_store of this UpdatesPackageInfo.


        :param enable_in_app_store: The enable_in_app_store of this UpdatesPackageInfo.  # noqa: E501
        :type: bool
        """

        self._enable_in_app_store = enable_in_app_store

    @property
    def installs(self):
        """Gets the installs of this UpdatesPackageInfo.  # noqa: E501


        :return: The installs of this UpdatesPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._installs

    @installs.setter
    def installs(self, installs):
        """Sets the installs of this UpdatesPackageInfo.


        :param installs: The installs of this UpdatesPackageInfo.  # noqa: E501
        :type: int
        """

        self._installs = installs

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
        if issubclass(UpdatesPackageInfo, dict):
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
        if not isinstance(other, UpdatesPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
