# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from embyapi.api_client import ApiClient


class TraktUriServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_trakt_users_by_userid_items_by_id_comment(self, user_id, id, comment, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_items_by_id_comment  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_items_by_id_comment(user_id, id, comment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param str id: Item Id (required)
        :param str comment: Text for the comment (required)
        :param bool spoiler: Set to true to indicate the comment contains spoilers. Defaults to false
        :param bool review: Set to true to indicate the comment is a 200+ word review. Defaults to false
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_trakt_users_by_userid_items_by_id_comment_with_http_info(user_id, id, comment, **kwargs)  # noqa: E501
        else:
            (data) = self.post_trakt_users_by_userid_items_by_id_comment_with_http_info(user_id, id, comment, **kwargs)  # noqa: E501
            return data

    def post_trakt_users_by_userid_items_by_id_comment_with_http_info(self, user_id, id, comment, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_items_by_id_comment  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_items_by_id_comment_with_http_info(user_id, id, comment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param str id: Item Id (required)
        :param str comment: Text for the comment (required)
        :param bool spoiler: Set to true to indicate the comment contains spoilers. Defaults to false
        :param bool review: Set to true to indicate the comment is a 200+ word review. Defaults to false
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id', 'comment', 'spoiler', 'review']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_trakt_users_by_userid_items_by_id_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_trakt_users_by_userid_items_by_id_comment`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `post_trakt_users_by_userid_items_by_id_comment`")  # noqa: E501
        # verify the required parameter 'comment' is set
        if ('comment' not in params or
                params['comment'] is None):
            raise ValueError("Missing the required parameter `comment` when calling `post_trakt_users_by_userid_items_by_id_comment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['UserId'] = params['user_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'comment' in params:
            query_params.append(('Comment', params['comment']))  # noqa: E501
        if 'spoiler' in params:
            query_params.append(('Spoiler', params['spoiler']))  # noqa: E501
        if 'review' in params:
            query_params.append(('Review', params['review']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Trakt/Users/{UserId}/Items/{Id}/Comment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_trakt_users_by_userid_items_by_id_rate(self, user_id, id, rating, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_items_by_id_rate  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_items_by_id_rate(user_id, id, rating, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param str id: Item Id (required)
        :param int rating: Rating between 1 - 10 (0 = unrate) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_trakt_users_by_userid_items_by_id_rate_with_http_info(user_id, id, rating, **kwargs)  # noqa: E501
        else:
            (data) = self.post_trakt_users_by_userid_items_by_id_rate_with_http_info(user_id, id, rating, **kwargs)  # noqa: E501
            return data

    def post_trakt_users_by_userid_items_by_id_rate_with_http_info(self, user_id, id, rating, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_items_by_id_rate  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_items_by_id_rate_with_http_info(user_id, id, rating, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param str id: Item Id (required)
        :param int rating: Rating between 1 - 10 (0 = unrate) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id', 'rating']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_trakt_users_by_userid_items_by_id_rate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_trakt_users_by_userid_items_by_id_rate`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `post_trakt_users_by_userid_items_by_id_rate`")  # noqa: E501
        # verify the required parameter 'rating' is set
        if ('rating' not in params or
                params['rating'] is None):
            raise ValueError("Missing the required parameter `rating` when calling `post_trakt_users_by_userid_items_by_id_rate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['UserId'] = params['user_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'rating' in params:
            query_params.append(('Rating', params['rating']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Trakt/Users/{UserId}/Items/{Id}/Rate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_trakt_users_by_userid_recommendedmovies(self, user_id, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_recommendedmovies  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_recommendedmovies(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param int genre: Genre slug to filter by. (See http://trakt.tv/api-docs/genres-movies)
        :param int start_year: 4-digit year to filter movies released this year or later
        :param int end_year: 4-digit year to filter movies released this year or earlier
        :param bool hide_collected: Set true to hide movies in the users collection
        :param bool hide_watchlisted: Set true to hide movies in the users watchlist
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_trakt_users_by_userid_recommendedmovies_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_trakt_users_by_userid_recommendedmovies_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def post_trakt_users_by_userid_recommendedmovies_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_recommendedmovies  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_recommendedmovies_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param int genre: Genre slug to filter by. (See http://trakt.tv/api-docs/genres-movies)
        :param int start_year: 4-digit year to filter movies released this year or later
        :param int end_year: 4-digit year to filter movies released this year or earlier
        :param bool hide_collected: Set true to hide movies in the users collection
        :param bool hide_watchlisted: Set true to hide movies in the users watchlist
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'genre', 'start_year', 'end_year', 'hide_collected', 'hide_watchlisted']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_trakt_users_by_userid_recommendedmovies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_trakt_users_by_userid_recommendedmovies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['UserId'] = params['user_id']  # noqa: E501

        query_params = []
        if 'genre' in params:
            query_params.append(('Genre', params['genre']))  # noqa: E501
        if 'start_year' in params:
            query_params.append(('StartYear', params['start_year']))  # noqa: E501
        if 'end_year' in params:
            query_params.append(('EndYear', params['end_year']))  # noqa: E501
        if 'hide_collected' in params:
            query_params.append(('HideCollected', params['hide_collected']))  # noqa: E501
        if 'hide_watchlisted' in params:
            query_params.append(('HideWatchlisted', params['hide_watchlisted']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Trakt/Users/{UserId}/RecommendedMovies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_trakt_users_by_userid_recommendedshows(self, user_id, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_recommendedshows  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_recommendedshows(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param int genre: Genre slug to filter by. (See http://trakt.tv/api-docs/genres-shows)
        :param int start_year: 4-digit year to filter shows released this year or later
        :param int end_year: 4-digit year to filter shows released this year or earlier
        :param bool hide_collected: Set true to hide shows in the users collection
        :param bool hide_watchlisted: Set true to hide shows in the users watchlist
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_trakt_users_by_userid_recommendedshows_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_trakt_users_by_userid_recommendedshows_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def post_trakt_users_by_userid_recommendedshows_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """post_trakt_users_by_userid_recommendedshows  # noqa: E501

        No authentication required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_trakt_users_by_userid_recommendedshows_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User Id (required)
        :param int genre: Genre slug to filter by. (See http://trakt.tv/api-docs/genres-shows)
        :param int start_year: 4-digit year to filter shows released this year or later
        :param int end_year: 4-digit year to filter shows released this year or earlier
        :param bool hide_collected: Set true to hide shows in the users collection
        :param bool hide_watchlisted: Set true to hide shows in the users watchlist
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'genre', 'start_year', 'end_year', 'hide_collected', 'hide_watchlisted']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_trakt_users_by_userid_recommendedshows" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_trakt_users_by_userid_recommendedshows`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['UserId'] = params['user_id']  # noqa: E501

        query_params = []
        if 'genre' in params:
            query_params.append(('Genre', params['genre']))  # noqa: E501
        if 'start_year' in params:
            query_params.append(('StartYear', params['start_year']))  # noqa: E501
        if 'end_year' in params:
            query_params.append(('EndYear', params['end_year']))  # noqa: E501
        if 'hide_collected' in params:
            query_params.append(('HideCollected', params['hide_collected']))  # noqa: E501
        if 'hide_watchlisted' in params:
            query_params.append(('HideWatchlisted', params['hide_watchlisted']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Trakt/Users/{UserId}/RecommendedShows', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)