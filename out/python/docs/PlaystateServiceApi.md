# embyapi.PlaystateServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_userid_playeditems_by_id**](PlaystateServiceApi.md#delete_users_by_userid_playeditems_by_id) | **DELETE** /Users/{UserId}/PlayedItems/{Id} | Marks an item as unplayed
[**delete_users_by_userid_playingitems_by_id**](PlaystateServiceApi.md#delete_users_by_userid_playingitems_by_id) | **DELETE** /Users/{UserId}/PlayingItems/{Id} | Reports that a user has stopped playing an item
[**post_sessions_playing**](PlaystateServiceApi.md#post_sessions_playing) | **POST** /Sessions/Playing | Reports playback has started within a session
[**post_sessions_playing_ping**](PlaystateServiceApi.md#post_sessions_playing_ping) | **POST** /Sessions/Playing/Ping | Pings a playback session
[**post_sessions_playing_progress**](PlaystateServiceApi.md#post_sessions_playing_progress) | **POST** /Sessions/Playing/Progress | Reports playback progress within a session
[**post_sessions_playing_stopped**](PlaystateServiceApi.md#post_sessions_playing_stopped) | **POST** /Sessions/Playing/Stopped | Reports playback has stopped within a session
[**post_users_by_userid_items_by_itemid_userdata**](PlaystateServiceApi.md#post_users_by_userid_items_by_itemid_userdata) | **POST** /Users/{UserId}/Items/{ItemId}/UserData | Updates userdata for an item
[**post_users_by_userid_playeditems_by_id**](PlaystateServiceApi.md#post_users_by_userid_playeditems_by_id) | **POST** /Users/{UserId}/PlayedItems/{Id} | Marks an item as played
[**post_users_by_userid_playeditems_by_id_delete**](PlaystateServiceApi.md#post_users_by_userid_playeditems_by_id_delete) | **POST** /Users/{UserId}/PlayedItems/{Id}/Delete | Marks an item as unplayed
[**post_users_by_userid_playingitems_by_id**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id) | **POST** /Users/{UserId}/PlayingItems/{Id} | Reports that a user has begun playing an item
[**post_users_by_userid_playingitems_by_id_delete**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id_delete) | **POST** /Users/{UserId}/PlayingItems/{Id}/Delete | Reports that a user has stopped playing an item
[**post_users_by_userid_playingitems_by_id_progress**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id_progress) | **POST** /Users/{UserId}/PlayingItems/{Id}/Progress | Reports a user&#x27;s playback progress

# **delete_users_by_userid_playeditems_by_id**
> UserItemDataDto delete_users_by_userid_playeditems_by_id(user_id, id)

Marks an item as unplayed

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Marks an item as unplayed
    api_response = api_instance.delete_users_by_userid_playeditems_by_id(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->delete_users_by_userid_playeditems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_by_userid_playingitems_by_id**
> delete_users_by_userid_playingitems_by_id(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has stopped playing an item

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | The id of the MediaSource
next_media_type = 'next_media_type_example' # str | The next media type that will play
position_ticks = 789 # int | Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms (optional)
live_stream_id = 'live_stream_id_example' # str |  (optional)
play_session_id = 'play_session_id_example' # str |  (optional)

try:
    # Reports that a user has stopped playing an item
    api_instance.delete_users_by_userid_playingitems_by_id(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->delete_users_by_userid_playingitems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **next_media_type** | **str**| The next media type that will play | 
 **position_ticks** | **int**| Optional. The position, in ticks, where playback stopped. 1 tick &#x3D; 10000 ms | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_playing**
> post_sessions_playing(body)

Reports playback has started within a session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.PlaybackStartInfo() # PlaybackStartInfo | PlaybackStartInfo: 

try:
    # Reports playback has started within a session
    api_instance.post_sessions_playing(body)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_sessions_playing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaybackStartInfo**](PlaybackStartInfo.md)| PlaybackStartInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_playing_ping**
> post_sessions_playing_ping(play_session_id=play_session_id)

Pings a playback session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
play_session_id = 'play_session_id_example' # str |  (optional)

try:
    # Pings a playback session
    api_instance.post_sessions_playing_ping(play_session_id=play_session_id)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_sessions_playing_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_session_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_playing_progress**
> post_sessions_playing_progress(body)

Reports playback progress within a session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.PlaybackProgressInfo() # PlaybackProgressInfo | PlaybackProgressInfo: 

try:
    # Reports playback progress within a session
    api_instance.post_sessions_playing_progress(body)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_sessions_playing_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaybackProgressInfo**](PlaybackProgressInfo.md)| PlaybackProgressInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_playing_stopped**
> post_sessions_playing_stopped(body)

Reports playback has stopped within a session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.PlaybackStopInfo() # PlaybackStopInfo | PlaybackStopInfo: 

try:
    # Reports playback has stopped within a session
    api_instance.post_sessions_playing_stopped(body)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_sessions_playing_stopped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaybackStopInfo**](PlaybackStopInfo.md)| PlaybackStopInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_items_by_itemid_userdata**
> post_users_by_userid_items_by_itemid_userdata(body, user_id, item_id)

Updates userdata for an item

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.UserItemDataDto() # UserItemDataDto | UserItemDataDto: 
user_id = 'user_id_example' # str | User Id
item_id = 'item_id_example' # str | 

try:
    # Updates userdata for an item
    api_instance.post_users_by_userid_items_by_itemid_userdata(body, user_id, item_id)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_items_by_itemid_userdata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserItemDataDto**](UserItemDataDto.md)| UserItemDataDto:  | 
 **user_id** | **str**| User Id | 
 **item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playeditems_by_id**
> UserItemDataDto post_users_by_userid_playeditems_by_id(user_id, id, date_played=date_played)

Marks an item as played

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
date_played = 'date_played_example' # str | The date the item was played (if any). Format = yyyyMMddHHmmss (optional)

try:
    # Marks an item as played
    api_response = api_instance.post_users_by_userid_playeditems_by_id(user_id, id, date_played=date_played)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_playeditems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **date_played** | **str**| The date the item was played (if any). Format &#x3D; yyyyMMddHHmmss | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playeditems_by_id_delete**
> UserItemDataDto post_users_by_userid_playeditems_by_id_delete(user_id, id)

Marks an item as unplayed

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Marks an item as unplayed
    api_response = api_instance.post_users_by_userid_playeditems_by_id_delete(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_playeditems_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playingitems_by_id**
> post_users_by_userid_playingitems_by_id(user_id, id, media_source_id, can_seek=can_seek, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has begun playing an item

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | The id of the MediaSource
can_seek = true # bool | Indicates if the client can seek (optional)
audio_stream_index = 56 # int |  (optional)
subtitle_stream_index = 56 # int |  (optional)
play_method = embyapi.PlayMethod() # PlayMethod |  (optional)
live_stream_id = 'live_stream_id_example' # str |  (optional)
play_session_id = 'play_session_id_example' # str |  (optional)

try:
    # Reports that a user has begun playing an item
    api_instance.post_users_by_userid_playingitems_by_id(user_id, id, media_source_id, can_seek=can_seek, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **can_seek** | **bool**| Indicates if the client can seek | [optional] 
 **audio_stream_index** | **int**|  | [optional] 
 **subtitle_stream_index** | **int**|  | [optional] 
 **play_method** | [**PlayMethod**](.md)|  | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playingitems_by_id_delete**
> post_users_by_userid_playingitems_by_id_delete(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has stopped playing an item

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | The id of the MediaSource
next_media_type = 'next_media_type_example' # str | The next media type that will play
position_ticks = 789 # int | Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms (optional)
live_stream_id = 'live_stream_id_example' # str |  (optional)
play_session_id = 'play_session_id_example' # str |  (optional)

try:
    # Reports that a user has stopped playing an item
    api_instance.post_users_by_userid_playingitems_by_id_delete(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **next_media_type** | **str**| The next media type that will play | 
 **position_ticks** | **int**| Optional. The position, in ticks, where playback stopped. 1 tick &#x3D; 10000 ms | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playingitems_by_id_progress**
> post_users_by_userid_playingitems_by_id_progress(body, media_source_id, user_id, id, position_ticks=position_ticks, is_paused=is_paused, is_muted=is_muted, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, subtitle_offset=subtitle_offset, playback_rate=playback_rate)

Reports a user's playback progress

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.PlaystateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.MediaEncodingApiOnPlaybackProgress() # MediaEncodingApiOnPlaybackProgress | OnPlaybackProgress
media_source_id = 'media_source_id_example' # str | The id of the MediaSource
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
position_ticks = 789 # int | Optional. The current position, in ticks. 1 tick = 10000 ms (optional)
is_paused = true # bool | Indicates if the player is paused. (optional)
is_muted = true # bool | Indicates if the player is muted. (optional)
audio_stream_index = 56 # int |  (optional)
subtitle_stream_index = 56 # int |  (optional)
volume_level = 56 # int | Scale of 0-100 (optional)
play_method = embyapi.PlayMethod() # PlayMethod |  (optional)
live_stream_id = 'live_stream_id_example' # str |  (optional)
play_session_id = 'play_session_id_example' # str |  (optional)
repeat_mode = embyapi.RepeatMode() # RepeatMode |  (optional)
subtitle_offset = 56 # int |  (optional)
playback_rate = 1.2 # float |  (optional)

try:
    # Reports a user's playback progress
    api_instance.post_users_by_userid_playingitems_by_id_progress(body, media_source_id, user_id, id, position_ticks=position_ticks, is_paused=is_paused, is_muted=is_muted, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, subtitle_offset=subtitle_offset, playback_rate=playback_rate)
except ApiException as e:
    print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaEncodingApiOnPlaybackProgress**](MediaEncodingApiOnPlaybackProgress.md)| OnPlaybackProgress | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **position_ticks** | **int**| Optional. The current position, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **is_paused** | **bool**| Indicates if the player is paused. | [optional] 
 **is_muted** | **bool**| Indicates if the player is muted. | [optional] 
 **audio_stream_index** | **int**|  | [optional] 
 **subtitle_stream_index** | **int**|  | [optional] 
 **volume_level** | **int**| Scale of 0-100 | [optional] 
 **play_method** | [**PlayMethod**](.md)|  | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 
 **repeat_mode** | [**RepeatMode**](.md)|  | [optional] 
 **subtitle_offset** | **int**|  | [optional] 
 **playback_rate** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

