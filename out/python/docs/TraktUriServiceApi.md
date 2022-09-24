# embyapi.TraktUriServiceApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_trakt_users_by_userid_items_by_id_comment**](TraktUriServiceApi.md#post_trakt_users_by_userid_items_by_id_comment) | **POST** /Trakt/Users/{UserId}/Items/{Id}/Comment | 
[**post_trakt_users_by_userid_items_by_id_rate**](TraktUriServiceApi.md#post_trakt_users_by_userid_items_by_id_rate) | **POST** /Trakt/Users/{UserId}/Items/{Id}/Rate | 
[**post_trakt_users_by_userid_recommendedmovies**](TraktUriServiceApi.md#post_trakt_users_by_userid_recommendedmovies) | **POST** /Trakt/Users/{UserId}/RecommendedMovies | 
[**post_trakt_users_by_userid_recommendedshows**](TraktUriServiceApi.md#post_trakt_users_by_userid_recommendedshows) | **POST** /Trakt/Users/{UserId}/RecommendedShows | 

# **post_trakt_users_by_userid_items_by_id_comment**
> post_trakt_users_by_userid_items_by_id_comment(user_id, id, comment, spoiler=spoiler, review=review)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.TraktUriServiceApi()
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
comment = 'comment_example' # str | Text for the comment
spoiler = true # bool | Set to true to indicate the comment contains spoilers. Defaults to false (optional)
review = true # bool | Set to true to indicate the comment is a 200+ word review. Defaults to false (optional)

try:
    api_instance.post_trakt_users_by_userid_items_by_id_comment(user_id, id, comment, spoiler=spoiler, review=review)
except ApiException as e:
    print("Exception when calling TraktUriServiceApi->post_trakt_users_by_userid_items_by_id_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **comment** | **str**| Text for the comment | 
 **spoiler** | **bool**| Set to true to indicate the comment contains spoilers. Defaults to false | [optional] 
 **review** | **bool**| Set to true to indicate the comment is a 200+ word review. Defaults to false | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_trakt_users_by_userid_items_by_id_rate**
> post_trakt_users_by_userid_items_by_id_rate(user_id, id, rating)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.TraktUriServiceApi()
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
rating = 56 # int | Rating between 1 - 10 (0 = unrate)

try:
    api_instance.post_trakt_users_by_userid_items_by_id_rate(user_id, id, rating)
except ApiException as e:
    print("Exception when calling TraktUriServiceApi->post_trakt_users_by_userid_items_by_id_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **rating** | **int**| Rating between 1 - 10 (0 &#x3D; unrate) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_trakt_users_by_userid_recommendedmovies**
> post_trakt_users_by_userid_recommendedmovies(user_id, genre=genre, start_year=start_year, end_year=end_year, hide_collected=hide_collected, hide_watchlisted=hide_watchlisted)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.TraktUriServiceApi()
user_id = 'user_id_example' # str | User Id
genre = 56 # int | Genre slug to filter by. (See http://trakt.tv/api-docs/genres-movies) (optional)
start_year = 56 # int | 4-digit year to filter movies released this year or later (optional)
end_year = 56 # int | 4-digit year to filter movies released this year or earlier (optional)
hide_collected = true # bool | Set true to hide movies in the users collection (optional)
hide_watchlisted = true # bool | Set true to hide movies in the users watchlist (optional)

try:
    api_instance.post_trakt_users_by_userid_recommendedmovies(user_id, genre=genre, start_year=start_year, end_year=end_year, hide_collected=hide_collected, hide_watchlisted=hide_watchlisted)
except ApiException as e:
    print("Exception when calling TraktUriServiceApi->post_trakt_users_by_userid_recommendedmovies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **genre** | **int**| Genre slug to filter by. (See http://trakt.tv/api-docs/genres-movies) | [optional] 
 **start_year** | **int**| 4-digit year to filter movies released this year or later | [optional] 
 **end_year** | **int**| 4-digit year to filter movies released this year or earlier | [optional] 
 **hide_collected** | **bool**| Set true to hide movies in the users collection | [optional] 
 **hide_watchlisted** | **bool**| Set true to hide movies in the users watchlist | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_trakt_users_by_userid_recommendedshows**
> post_trakt_users_by_userid_recommendedshows(user_id, genre=genre, start_year=start_year, end_year=end_year, hide_collected=hide_collected, hide_watchlisted=hide_watchlisted)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.TraktUriServiceApi()
user_id = 'user_id_example' # str | User Id
genre = 56 # int | Genre slug to filter by. (See http://trakt.tv/api-docs/genres-shows) (optional)
start_year = 56 # int | 4-digit year to filter shows released this year or later (optional)
end_year = 56 # int | 4-digit year to filter shows released this year or earlier (optional)
hide_collected = true # bool | Set true to hide shows in the users collection (optional)
hide_watchlisted = true # bool | Set true to hide shows in the users watchlist (optional)

try:
    api_instance.post_trakt_users_by_userid_recommendedshows(user_id, genre=genre, start_year=start_year, end_year=end_year, hide_collected=hide_collected, hide_watchlisted=hide_watchlisted)
except ApiException as e:
    print("Exception when calling TraktUriServiceApi->post_trakt_users_by_userid_recommendedshows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **genre** | **int**| Genre slug to filter by. (See http://trakt.tv/api-docs/genres-shows) | [optional] 
 **start_year** | **int**| 4-digit year to filter shows released this year or later | [optional] 
 **end_year** | **int**| 4-digit year to filter shows released this year or earlier | [optional] 
 **hide_collected** | **bool**| Set true to hide shows in the users collection | [optional] 
 **hide_watchlisted** | **bool**| Set true to hide shows in the users watchlist | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

