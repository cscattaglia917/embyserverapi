# embyapi.SmartPlaylistApiApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smartplaylist_by_id_by_keep**](SmartPlaylistApiApi.md#delete_smartplaylist_by_id_by_keep) | **DELETE** /smartplaylist/{Id}/{Keep} | 
[**get_smartplaylist_appdata**](SmartPlaylistApiApi.md#get_smartplaylist_appdata) | **GET** /smartplaylist/appData | 
[**post_smartplaylist**](SmartPlaylistApiApi.md#post_smartplaylist) | **POST** /smartplaylist | 
[**post_smartplaylist_sort**](SmartPlaylistApiApi.md#post_smartplaylist_sort) | **POST** /smartplaylist/sort | 

# **delete_smartplaylist_by_id_by_keep**
> delete_smartplaylist_by_id_by_keep(id, keep)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistApiApi()
id = 'id_example' # str | 
keep = true # bool | 

try:
    api_instance.delete_smartplaylist_by_id_by_keep(id, keep)
except ApiException as e:
    print("Exception when calling SmartPlaylistApiApi->delete_smartplaylist_by_id_by_keep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **keep** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smartplaylist_appdata**
> SmartPlaylistApiGetAppDataResponse get_smartplaylist_appdata()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistApiApi()

try:
    api_response = api_instance.get_smartplaylist_appdata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistApiApi->get_smartplaylist_appdata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmartPlaylistApiGetAppDataResponse**](SmartPlaylistApiGetAppDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist**
> SmartPlaylistContractsSmartPlaylistResponseDto post_smartplaylist(body)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistApiApi()
body = embyapi.SmartPlaylistContractsSmartPlaylistDto() # SmartPlaylistContractsSmartPlaylistDto | SmartPlaylistDto: 

try:
    api_response = api_instance.post_smartplaylist(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistApiApi->post_smartplaylist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsSmartPlaylistDto.md)| SmartPlaylistDto:  | 

### Return type

[**SmartPlaylistContractsSmartPlaylistResponseDto**](SmartPlaylistContractsSmartPlaylistResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist_sort**
> SmartPlaylistContractsSmartPlaylistResponseDto post_smartplaylist_sort(body)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistApiApi()
body = embyapi.SmartPlaylistContractsSmartPlaylistDto() # SmartPlaylistContractsSmartPlaylistDto | SmartPlaylistDto: 

try:
    api_response = api_instance.post_smartplaylist_sort(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistApiApi->post_smartplaylist_sort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsSmartPlaylistDto.md)| SmartPlaylistDto:  | 

### Return type

[**SmartPlaylistContractsSmartPlaylistResponseDto**](SmartPlaylistContractsSmartPlaylistResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

