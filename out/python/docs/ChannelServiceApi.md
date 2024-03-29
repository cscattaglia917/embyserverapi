# embyapi.ChannelServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channels**](ChannelServiceApi.md#get_channels) | **GET** /Channels | Gets available channels

# **get_channels**
> QueryResultBaseItemDto get_channels(user_id=user_id, start_index=start_index, limit=limit)

Gets available channels

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
api_instance = embyapi.ChannelServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)

try:
    # Gets available channels
    api_response = api_instance.get_channels(user_id=user_id, start_index=start_index, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelServiceApi->get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

