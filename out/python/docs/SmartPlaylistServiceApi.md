# embyapi.SmartPlaylistServiceApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smartplaylist_by_id_by_keep**](SmartPlaylistServiceApi.md#delete_smartplaylist_by_id_by_keep) | **DELETE** /smartplaylist/{Id}/{Keep} | 
[**get_smartplaylist_appdata**](SmartPlaylistServiceApi.md#get_smartplaylist_appdata) | **GET** /smartplaylist/appData | 
[**post_smartplaylist**](SmartPlaylistServiceApi.md#post_smartplaylist) | **POST** /smartplaylist | 
[**post_smartplaylist_sort**](SmartPlaylistServiceApi.md#post_smartplaylist_sort) | **POST** /smartplaylist/sort | 

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
api_instance = embyapi.SmartPlaylistServiceApi()
id = 'id_example' # str | 
keep = true # bool | 

try:
    api_instance.delete_smartplaylist_by_id_by_keep(id, keep)
except ApiException as e:
    print("Exception when calling SmartPlaylistServiceApi->delete_smartplaylist_by_id_by_keep: %s\n" % e)
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
> SmartPlaylistApiAppDataResponse get_smartplaylist_appdata()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistServiceApi()

try:
    api_response = api_instance.get_smartplaylist_appdata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistServiceApi->get_smartplaylist_appdata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmartPlaylistApiAppDataResponse**](SmartPlaylistApiAppDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist**
> SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto post_smartplaylist(body)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistServiceApi()
body = embyapi.SmartPlaylistContractsSmartPlaylistDto() # SmartPlaylistContractsSmartPlaylistDto | SmartPlaylistDto: 

try:
    api_response = api_instance.post_smartplaylist(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistServiceApi->post_smartplaylist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsSmartPlaylistDto.md)| SmartPlaylistDto:  | 

### Return type

[**SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist_sort**
> SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto post_smartplaylist_sort(body)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SmartPlaylistServiceApi()
body = embyapi.SmartPlaylistContractsSmartPlaylistDto() # SmartPlaylistContractsSmartPlaylistDto | SmartPlaylistDto: 

try:
    api_response = api_instance.post_smartplaylist_sort(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartPlaylistServiceApi->post_smartplaylist_sort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsSmartPlaylistDto.md)| SmartPlaylistDto:  | 

### Return type

[**SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto**](SmartPlaylistContractsResponseDtoSmartPlaylistContractsSmartPlaylistDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

