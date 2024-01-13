# embyapi.SubtitleServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_items_by_id_subtitles_by_index**](SubtitleServiceApi.md#delete_items_by_id_subtitles_by_index) | **DELETE** /Items/{Id}/Subtitles/{Index} | Deletes an external subtitle file
[**delete_videos_by_id_subtitles_by_index**](SubtitleServiceApi.md#delete_videos_by_id_subtitles_by_index) | **DELETE** /Videos/{Id}/Subtitles/{Index} | Deletes an external subtitle file
[**get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**](SubtitleServiceApi.md#get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format) | **GET** /Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format} | Gets subtitles in a specified format.
[**get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**](SubtitleServiceApi.md#get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format) | **GET** /Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format} | Gets subtitles in a specified format.
[**get_items_by_id_remotesearch_subtitles_by_language**](SubtitleServiceApi.md#get_items_by_id_remotesearch_subtitles_by_language) | **GET** /Items/{Id}/RemoteSearch/Subtitles/{Language} | 
[**get_providers_subtitles_subtitles_by_id**](SubtitleServiceApi.md#get_providers_subtitles_subtitles_by_id) | **GET** /Providers/Subtitles/Subtitles/{Id} | 
[**get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**](SubtitleServiceApi.md#get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format) | **GET** /Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format} | Gets subtitles in a specified format.
[**get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**](SubtitleServiceApi.md#get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format) | **GET** /Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format} | Gets subtitles in a specified format.
[**post_items_by_id_remotesearch_subtitles_by_subtitleid**](SubtitleServiceApi.md#post_items_by_id_remotesearch_subtitles_by_subtitleid) | **POST** /Items/{Id}/RemoteSearch/Subtitles/{SubtitleId} | 
[**post_items_by_id_subtitles_by_index_delete**](SubtitleServiceApi.md#post_items_by_id_subtitles_by_index_delete) | **POST** /Items/{Id}/Subtitles/{Index}/Delete | Deletes an external subtitle file
[**post_videos_by_id_subtitles_by_index_delete**](SubtitleServiceApi.md#post_videos_by_id_subtitles_by_index_delete) | **POST** /Videos/{Id}/Subtitles/{Index}/Delete | Deletes an external subtitle file

# **delete_items_by_id_subtitles_by_index**
> delete_items_by_id_subtitles_by_index(id, media_source_id, index)

Deletes an external subtitle file

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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index

try:
    # Deletes an external subtitle file
    api_instance.delete_items_by_id_subtitles_by_index(id, media_source_id, index)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->delete_items_by_id_subtitles_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_by_id_subtitles_by_index**
> delete_videos_by_id_subtitles_by_index(id, media_source_id, index)

Deletes an external subtitle file

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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index

try:
    # Deletes an external subtitle file
    api_instance.delete_videos_by_id_subtitles_by_index(id, media_source_id, index)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->delete_videos_by_id_subtitles_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**
> get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SubtitleServiceApi()
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index
format = 'format_example' # str | Format
start_position_ticks = 789 # int | StartPositionTicks
end_position_ticks = 789 # int | EndPositionTicks (optional)
copy_timestamps = true # bool | CopyTimestamps (optional)

try:
    # Gets subtitles in a specified format.
    api_instance.get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**
> get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SubtitleServiceApi()
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index
format = 'format_example' # str | Format
start_position_ticks = 789 # int | StartPositionTicks (optional)
end_position_ticks = 789 # int | EndPositionTicks (optional)
copy_timestamps = true # bool | CopyTimestamps (optional)

try:
    # Gets subtitles in a specified format.
    api_instance.get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | [optional] 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_remotesearch_subtitles_by_language**
> list[RemoteSubtitleInfo] get_items_by_id_remotesearch_subtitles_by_language(id, media_source_id, language, is_perfect_match=is_perfect_match, is_forced=is_forced)



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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
language = 'language_example' # str | Language
is_perfect_match = true # bool | IsPerfectMatch (optional)
is_forced = true # bool | IsForced (optional)

try:
    api_response = api_instance.get_items_by_id_remotesearch_subtitles_by_language(id, media_source_id, language, is_perfect_match=is_perfect_match, is_forced=is_forced)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_items_by_id_remotesearch_subtitles_by_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **language** | **str**| Language | 
 **is_perfect_match** | **bool**| IsPerfectMatch | [optional] 
 **is_forced** | **bool**| IsForced | [optional] 

### Return type

[**list[RemoteSubtitleInfo]**](RemoteSubtitleInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_subtitles_subtitles_by_id**
> get_providers_subtitles_subtitles_by_id(id)



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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    api_instance.get_providers_subtitles_subtitles_by_id(id)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_providers_subtitles_subtitles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**
> get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SubtitleServiceApi()
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index
format = 'format_example' # str | Format
start_position_ticks = 789 # int | StartPositionTicks
end_position_ticks = 789 # int | EndPositionTicks (optional)
copy_timestamps = true # bool | CopyTimestamps (optional)

try:
    # Gets subtitles in a specified format.
    api_instance.get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**
> get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SubtitleServiceApi()
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index
format = 'format_example' # str | Format
start_position_ticks = 789 # int | StartPositionTicks (optional)
end_position_ticks = 789 # int | EndPositionTicks (optional)
copy_timestamps = true # bool | CopyTimestamps (optional)

try:
    # Gets subtitles in a specified format.
    api_instance.get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | [optional] 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_remotesearch_subtitles_by_subtitleid**
> SubtitlesSubtitleDownloadResult post_items_by_id_remotesearch_subtitles_by_subtitleid(id, media_source_id, subtitle_id)



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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
subtitle_id = 'subtitle_id_example' # str | SubtitleId

try:
    api_response = api_instance.post_items_by_id_remotesearch_subtitles_by_subtitleid(id, media_source_id, subtitle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->post_items_by_id_remotesearch_subtitles_by_subtitleid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **subtitle_id** | **str**| SubtitleId | 

### Return type

[**SubtitlesSubtitleDownloadResult**](SubtitlesSubtitleDownloadResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_subtitles_by_index_delete**
> post_items_by_id_subtitles_by_index_delete(id, media_source_id, index)

Deletes an external subtitle file

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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index

try:
    # Deletes an external subtitle file
    api_instance.post_items_by_id_subtitles_by_index_delete(id, media_source_id, index)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->post_items_by_id_subtitles_by_index_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_by_id_subtitles_by_index_delete**
> post_videos_by_id_subtitles_by_index_delete(id, media_source_id, index)

Deletes an external subtitle file

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
api_instance = embyapi.SubtitleServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
media_source_id = 'media_source_id_example' # str | MediaSourceId
index = 56 # int | The subtitle stream index

try:
    # Deletes an external subtitle file
    api_instance.post_videos_by_id_subtitles_by_index_delete(id, media_source_id, index)
except ApiException as e:
    print("Exception when calling SubtitleServiceApi->post_videos_by_id_subtitles_by_index_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

