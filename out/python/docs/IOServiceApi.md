# embyapi.IOServiceApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smartplaylist_export_by_payload**](IOServiceApi.md#get_smartplaylist_export_by_payload) | **GET** /smartplaylist/export/{payload} | 
[**post_smartplaylist_import**](IOServiceApi.md#post_smartplaylist_import) | **POST** /smartplaylist/import | 

# **get_smartplaylist_export_by_payload**
> get_smartplaylist_export_by_payload(payload)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.IOServiceApi()
payload = 'payload_example' # str | 

try:
    api_instance.get_smartplaylist_export_by_payload(payload)
except ApiException as e:
    print("Exception when calling IOServiceApi->get_smartplaylist_export_by_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smartplaylist_import**
> SmartPlaylistContractsResponseDtoString post_smartplaylist_import(body)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.IOServiceApi()
body = embyapi.SmartPlaylistApiImport() # SmartPlaylistApiImport | Import

try:
    api_response = api_instance.post_smartplaylist_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IOServiceApi->post_smartplaylist_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmartPlaylistApiImport**](SmartPlaylistApiImport.md)| Import | 

### Return type

[**SmartPlaylistContractsResponseDtoString**](SmartPlaylistContractsResponseDtoString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

