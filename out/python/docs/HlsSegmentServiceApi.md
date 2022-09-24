# embyapi.HlsSegmentServiceApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_videos_activeencodings**](HlsSegmentServiceApi.md#delete_videos_activeencodings) | **DELETE** /Videos/ActiveEncodings | 
[**post_videos_activeencodings_delete**](HlsSegmentServiceApi.md#post_videos_activeencodings_delete) | **POST** /Videos/ActiveEncodings/Delete | 

# **delete_videos_activeencodings**
> delete_videos_activeencodings(device_id, play_session_id)



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
api_instance = embyapi.HlsSegmentServiceApi(embyapi.ApiClient(configuration))
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed.
play_session_id = 'play_session_id_example' # str | The play session id

try:
    api_instance.delete_videos_activeencodings(device_id, play_session_id)
except ApiException as e:
    print("Exception when calling HlsSegmentServiceApi->delete_videos_activeencodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | 
 **play_session_id** | **str**| The play session id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_activeencodings_delete**
> post_videos_activeencodings_delete(device_id, play_session_id)



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
api_instance = embyapi.HlsSegmentServiceApi(embyapi.ApiClient(configuration))
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed.
play_session_id = 'play_session_id_example' # str | The play session id

try:
    api_instance.post_videos_activeencodings_delete(device_id, play_session_id)
except ApiException as e:
    print("Exception when calling HlsSegmentServiceApi->post_videos_activeencodings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | 
 **play_session_id** | **str**| The play session id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

