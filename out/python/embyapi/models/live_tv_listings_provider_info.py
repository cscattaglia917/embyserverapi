# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LiveTvListingsProviderInfo(object):
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
        'name': 'str',
        'setup_url': 'str',
        'id': 'str',
        'type': 'str',
        'username': 'str',
        'password': 'str',
        'listings_id': 'str',
        'zip_code': 'str',
        'country': 'str',
        'path': 'str',
        'enabled_tuners': 'list[str]',
        'enable_all_tuners': 'bool',
        'news_categories': 'list[str]',
        'sports_categories': 'list[str]',
        'kids_categories': 'list[str]',
        'movie_categories': 'list[str]',
        'channel_mappings': 'list[NameValuePair]',
        'movie_prefix': 'str',
        'preferred_language': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'setup_url': 'SetupUrl',
        'id': 'Id',
        'type': 'Type',
        'username': 'Username',
        'password': 'Password',
        'listings_id': 'ListingsId',
        'zip_code': 'ZipCode',
        'country': 'Country',
        'path': 'Path',
        'enabled_tuners': 'EnabledTuners',
        'enable_all_tuners': 'EnableAllTuners',
        'news_categories': 'NewsCategories',
        'sports_categories': 'SportsCategories',
        'kids_categories': 'KidsCategories',
        'movie_categories': 'MovieCategories',
        'channel_mappings': 'ChannelMappings',
        'movie_prefix': 'MoviePrefix',
        'preferred_language': 'PreferredLanguage',
        'user_agent': 'UserAgent'
    }

    def __init__(self, name=None, setup_url=None, id=None, type=None, username=None, password=None, listings_id=None, zip_code=None, country=None, path=None, enabled_tuners=None, enable_all_tuners=None, news_categories=None, sports_categories=None, kids_categories=None, movie_categories=None, channel_mappings=None, movie_prefix=None, preferred_language=None, user_agent=None):  # noqa: E501
        """LiveTvListingsProviderInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._setup_url = None
        self._id = None
        self._type = None
        self._username = None
        self._password = None
        self._listings_id = None
        self._zip_code = None
        self._country = None
        self._path = None
        self._enabled_tuners = None
        self._enable_all_tuners = None
        self._news_categories = None
        self._sports_categories = None
        self._kids_categories = None
        self._movie_categories = None
        self._channel_mappings = None
        self._movie_prefix = None
        self._preferred_language = None
        self._user_agent = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if setup_url is not None:
            self.setup_url = setup_url
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if listings_id is not None:
            self.listings_id = listings_id
        if zip_code is not None:
            self.zip_code = zip_code
        if country is not None:
            self.country = country
        if path is not None:
            self.path = path
        if enabled_tuners is not None:
            self.enabled_tuners = enabled_tuners
        if enable_all_tuners is not None:
            self.enable_all_tuners = enable_all_tuners
        if news_categories is not None:
            self.news_categories = news_categories
        if sports_categories is not None:
            self.sports_categories = sports_categories
        if kids_categories is not None:
            self.kids_categories = kids_categories
        if movie_categories is not None:
            self.movie_categories = movie_categories
        if channel_mappings is not None:
            self.channel_mappings = channel_mappings
        if movie_prefix is not None:
            self.movie_prefix = movie_prefix
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def name(self):
        """Gets the name of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The name of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveTvListingsProviderInfo.


        :param name: The name of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def setup_url(self):
        """Gets the setup_url of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The setup_url of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._setup_url

    @setup_url.setter
    def setup_url(self, setup_url):
        """Sets the setup_url of this LiveTvListingsProviderInfo.


        :param setup_url: The setup_url of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._setup_url = setup_url

    @property
    def id(self):
        """Gets the id of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The id of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveTvListingsProviderInfo.


        :param id: The id of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The type of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LiveTvListingsProviderInfo.


        :param type: The type of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def username(self):
        """Gets the username of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The username of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LiveTvListingsProviderInfo.


        :param username: The username of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The password of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LiveTvListingsProviderInfo.


        :param password: The password of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def listings_id(self):
        """Gets the listings_id of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The listings_id of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._listings_id

    @listings_id.setter
    def listings_id(self, listings_id):
        """Sets the listings_id of this LiveTvListingsProviderInfo.


        :param listings_id: The listings_id of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._listings_id = listings_id

    @property
    def zip_code(self):
        """Gets the zip_code of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The zip_code of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this LiveTvListingsProviderInfo.


        :param zip_code: The zip_code of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The country of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this LiveTvListingsProviderInfo.


        :param country: The country of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def path(self):
        """Gets the path of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The path of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LiveTvListingsProviderInfo.


        :param path: The path of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def enabled_tuners(self):
        """Gets the enabled_tuners of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The enabled_tuners of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_tuners

    @enabled_tuners.setter
    def enabled_tuners(self, enabled_tuners):
        """Sets the enabled_tuners of this LiveTvListingsProviderInfo.


        :param enabled_tuners: The enabled_tuners of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[str]
        """

        self._enabled_tuners = enabled_tuners

    @property
    def enable_all_tuners(self):
        """Gets the enable_all_tuners of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The enable_all_tuners of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable_all_tuners

    @enable_all_tuners.setter
    def enable_all_tuners(self, enable_all_tuners):
        """Sets the enable_all_tuners of this LiveTvListingsProviderInfo.


        :param enable_all_tuners: The enable_all_tuners of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: bool
        """

        self._enable_all_tuners = enable_all_tuners

    @property
    def news_categories(self):
        """Gets the news_categories of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The news_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._news_categories

    @news_categories.setter
    def news_categories(self, news_categories):
        """Sets the news_categories of this LiveTvListingsProviderInfo.


        :param news_categories: The news_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[str]
        """

        self._news_categories = news_categories

    @property
    def sports_categories(self):
        """Gets the sports_categories of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The sports_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._sports_categories

    @sports_categories.setter
    def sports_categories(self, sports_categories):
        """Sets the sports_categories of this LiveTvListingsProviderInfo.


        :param sports_categories: The sports_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[str]
        """

        self._sports_categories = sports_categories

    @property
    def kids_categories(self):
        """Gets the kids_categories of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The kids_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._kids_categories

    @kids_categories.setter
    def kids_categories(self, kids_categories):
        """Sets the kids_categories of this LiveTvListingsProviderInfo.


        :param kids_categories: The kids_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[str]
        """

        self._kids_categories = kids_categories

    @property
    def movie_categories(self):
        """Gets the movie_categories of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The movie_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._movie_categories

    @movie_categories.setter
    def movie_categories(self, movie_categories):
        """Sets the movie_categories of this LiveTvListingsProviderInfo.


        :param movie_categories: The movie_categories of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[str]
        """

        self._movie_categories = movie_categories

    @property
    def channel_mappings(self):
        """Gets the channel_mappings of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The channel_mappings of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: list[NameValuePair]
        """
        return self._channel_mappings

    @channel_mappings.setter
    def channel_mappings(self, channel_mappings):
        """Sets the channel_mappings of this LiveTvListingsProviderInfo.


        :param channel_mappings: The channel_mappings of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: list[NameValuePair]
        """

        self._channel_mappings = channel_mappings

    @property
    def movie_prefix(self):
        """Gets the movie_prefix of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The movie_prefix of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._movie_prefix

    @movie_prefix.setter
    def movie_prefix(self, movie_prefix):
        """Sets the movie_prefix of this LiveTvListingsProviderInfo.


        :param movie_prefix: The movie_prefix of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._movie_prefix = movie_prefix

    @property
    def preferred_language(self):
        """Gets the preferred_language of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The preferred_language of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """Sets the preferred_language of this LiveTvListingsProviderInfo.


        :param preferred_language: The preferred_language of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._preferred_language = preferred_language

    @property
    def user_agent(self):
        """Gets the user_agent of this LiveTvListingsProviderInfo.  # noqa: E501


        :return: The user_agent of this LiveTvListingsProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this LiveTvListingsProviderInfo.


        :param user_agent: The user_agent of this LiveTvListingsProviderInfo.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if issubclass(LiveTvListingsProviderInfo, dict):
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
        if not isinstance(other, LiveTvListingsProviderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
