# embyapi.PlaylistInfoServiceApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smartplaylist_info_by_id**](PlaylistInfoServiceApi.md#get_smartplaylist_info_by_id) | **GET** /smartplaylist/info/{Id} | 
[**post_smartplaylist_info_by_id**](PlaylistInfoServiceApi.md#post_smartplaylist_info_by_id) | **POST** /smartplaylist/info/{Id} | 

# **get_smartplaylist_info_by_id**
> SmartPlaylistContractsSmartPlaylistInfoDto get_smartplaylist_info_by_id(id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.PlaylistInfoServiceApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_smartplaylist_info_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistInfoServiceApi->get_smartplaylist_info_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SmartPlaylistContractsSmartPlaylistInfoDto**](SmartPlaylistContractsSmartPlaylistInfoDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist_info_by_id**
> SmartPlaylistContractsSmartPlaylistInfoDto post_smartplaylist_info_by_id(body, id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.PlaylistInfoServiceApi()
body = embyapi.SmartPlaylistApiExecutePlaylist() # SmartPlaylistApiExecutePlaylist | ExecutePlaylist
id = 'id_example' # str | 

try:
    api_response = api_instance.post_smartplaylist_info_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistInfoServiceApi->post_smartplaylist_info_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistApiExecutePlaylist**](SmartPlaylistApiExecutePlaylist.md)| ExecutePlaylist | 
 **id** | **str**|  | 

### Return type

[**SmartPlaylistContractsSmartPlaylistInfoDto**](SmartPlaylistContractsSmartPlaylistInfoDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

