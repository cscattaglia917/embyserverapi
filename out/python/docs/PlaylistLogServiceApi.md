# embyapi.PlaylistLogServiceApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smartplaylist_log_by_id**](PlaylistLogServiceApi.md#get_smartplaylist_log_by_id) | **GET** /smartplaylist/log/{Id} | 

# **get_smartplaylist_log_by_id**
> get_smartplaylist_log_by_id(id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.PlaylistLogServiceApi()
id = 'id_example' # str | 

try:
    api_instance.get_smartplaylist_log_by_id(id)
except ApiException as e:
    print("Exception when calling PlaylistLogServiceApi->get_smartplaylist_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

