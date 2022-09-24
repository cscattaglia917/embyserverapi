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

class ItemCounts(object):
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
        'movie_count': 'int',
        'series_count': 'int',
        'episode_count': 'int',
        'game_count': 'int',
        'artist_count': 'int',
        'program_count': 'int',
        'game_system_count': 'int',
        'trailer_count': 'int',
        'song_count': 'int',
        'album_count': 'int',
        'music_video_count': 'int',
        'box_set_count': 'int',
        'book_count': 'int',
        'item_count': 'int'
    }

    attribute_map = {
        'movie_count': 'MovieCount',
        'series_count': 'SeriesCount',
        'episode_count': 'EpisodeCount',
        'game_count': 'GameCount',
        'artist_count': 'ArtistCount',
        'program_count': 'ProgramCount',
        'game_system_count': 'GameSystemCount',
        'trailer_count': 'TrailerCount',
        'song_count': 'SongCount',
        'album_count': 'AlbumCount',
        'music_video_count': 'MusicVideoCount',
        'box_set_count': 'BoxSetCount',
        'book_count': 'BookCount',
        'item_count': 'ItemCount'
    }

    def __init__(self, movie_count=None, series_count=None, episode_count=None, game_count=None, artist_count=None, program_count=None, game_system_count=None, trailer_count=None, song_count=None, album_count=None, music_video_count=None, box_set_count=None, book_count=None, item_count=None):  # noqa: E501
        """ItemCounts - a model defined in Swagger"""  # noqa: E501
        self._movie_count = None
        self._series_count = None
        self._episode_count = None
        self._game_count = None
        self._artist_count = None
        self._program_count = None
        self._game_system_count = None
        self._trailer_count = None
        self._song_count = None
        self._album_count = None
        self._music_video_count = None
        self._box_set_count = None
        self._book_count = None
        self._item_count = None
        self.discriminator = None
        if movie_count is not None:
            self.movie_count = movie_count
        if series_count is not None:
            self.series_count = series_count
        if episode_count is not None:
            self.episode_count = episode_count
        if game_count is not None:
            self.game_count = game_count
        if artist_count is not None:
            self.artist_count = artist_count
        if program_count is not None:
            self.program_count = program_count
        if game_system_count is not None:
            self.game_system_count = game_system_count
        if trailer_count is not None:
            self.trailer_count = trailer_count
        if song_count is not None:
            self.song_count = song_count
        if album_count is not None:
            self.album_count = album_count
        if music_video_count is not None:
            self.music_video_count = music_video_count
        if box_set_count is not None:
            self.box_set_count = box_set_count
        if book_count is not None:
            self.book_count = book_count
        if item_count is not None:
            self.item_count = item_count

    @property
    def movie_count(self):
        """Gets the movie_count of this ItemCounts.  # noqa: E501


        :return: The movie_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._movie_count

    @movie_count.setter
    def movie_count(self, movie_count):
        """Sets the movie_count of this ItemCounts.


        :param movie_count: The movie_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._movie_count = movie_count

    @property
    def series_count(self):
        """Gets the series_count of this ItemCounts.  # noqa: E501


        :return: The series_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._series_count

    @series_count.setter
    def series_count(self, series_count):
        """Sets the series_count of this ItemCounts.


        :param series_count: The series_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._series_count = series_count

    @property
    def episode_count(self):
        """Gets the episode_count of this ItemCounts.  # noqa: E501


        :return: The episode_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._episode_count

    @episode_count.setter
    def episode_count(self, episode_count):
        """Sets the episode_count of this ItemCounts.


        :param episode_count: The episode_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._episode_count = episode_count

    @property
    def game_count(self):
        """Gets the game_count of this ItemCounts.  # noqa: E501


        :return: The game_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._game_count

    @game_count.setter
    def game_count(self, game_count):
        """Sets the game_count of this ItemCounts.


        :param game_count: The game_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._game_count = game_count

    @property
    def artist_count(self):
        """Gets the artist_count of this ItemCounts.  # noqa: E501


        :return: The artist_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._artist_count

    @artist_count.setter
    def artist_count(self, artist_count):
        """Sets the artist_count of this ItemCounts.


        :param artist_count: The artist_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._artist_count = artist_count

    @property
    def program_count(self):
        """Gets the program_count of this ItemCounts.  # noqa: E501


        :return: The program_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._program_count

    @program_count.setter
    def program_count(self, program_count):
        """Sets the program_count of this ItemCounts.


        :param program_count: The program_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._program_count = program_count

    @property
    def game_system_count(self):
        """Gets the game_system_count of this ItemCounts.  # noqa: E501


        :return: The game_system_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._game_system_count

    @game_system_count.setter
    def game_system_count(self, game_system_count):
        """Sets the game_system_count of this ItemCounts.


        :param game_system_count: The game_system_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._game_system_count = game_system_count

    @property
    def trailer_count(self):
        """Gets the trailer_count of this ItemCounts.  # noqa: E501


        :return: The trailer_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._trailer_count

    @trailer_count.setter
    def trailer_count(self, trailer_count):
        """Sets the trailer_count of this ItemCounts.


        :param trailer_count: The trailer_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._trailer_count = trailer_count

    @property
    def song_count(self):
        """Gets the song_count of this ItemCounts.  # noqa: E501


        :return: The song_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._song_count

    @song_count.setter
    def song_count(self, song_count):
        """Sets the song_count of this ItemCounts.


        :param song_count: The song_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._song_count = song_count

    @property
    def album_count(self):
        """Gets the album_count of this ItemCounts.  # noqa: E501


        :return: The album_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._album_count

    @album_count.setter
    def album_count(self, album_count):
        """Sets the album_count of this ItemCounts.


        :param album_count: The album_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._album_count = album_count

    @property
    def music_video_count(self):
        """Gets the music_video_count of this ItemCounts.  # noqa: E501


        :return: The music_video_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._music_video_count

    @music_video_count.setter
    def music_video_count(self, music_video_count):
        """Sets the music_video_count of this ItemCounts.


        :param music_video_count: The music_video_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._music_video_count = music_video_count

    @property
    def box_set_count(self):
        """Gets the box_set_count of this ItemCounts.  # noqa: E501


        :return: The box_set_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._box_set_count

    @box_set_count.setter
    def box_set_count(self, box_set_count):
        """Sets the box_set_count of this ItemCounts.


        :param box_set_count: The box_set_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._box_set_count = box_set_count

    @property
    def book_count(self):
        """Gets the book_count of this ItemCounts.  # noqa: E501


        :return: The book_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._book_count

    @book_count.setter
    def book_count(self, book_count):
        """Sets the book_count of this ItemCounts.


        :param book_count: The book_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._book_count = book_count

    @property
    def item_count(self):
        """Gets the item_count of this ItemCounts.  # noqa: E501


        :return: The item_count of this ItemCounts.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this ItemCounts.


        :param item_count: The item_count of this ItemCounts.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

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
        if issubclass(ItemCounts, dict):
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
        if not isinstance(other, ItemCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
