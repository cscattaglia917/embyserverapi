# embyapi.SubtitleOptionsServiceApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_encoding_subtitleoptions**](SubtitleOptionsServiceApi.md#get_encoding_subtitleoptions) | **GET** /Encoding/SubtitleOptions | Gets the subtitle options
[**post_encoding_subtitleoptions**](SubtitleOptionsServiceApi.md#post_encoding_subtitleoptions) | **POST** /Encoding/SubtitleOptions | Updates the subtitle options

# **get_encoding_subtitleoptions**
> EmbyWebGenericEditEditObjectContainer get_encoding_subtitleoptions()

Gets the subtitle options

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
api_instance = embyapi.SubtitleOptionsServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets the subtitle options
    api_response = api_instance.get_encoding_subtitleoptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitleOptionsServiceApi->get_encoding_subtitleoptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmbyWebGenericEditEditObjectContainer**](EmbyWebGenericEditEditObjectContainer.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_encoding_subtitleoptions**
> post_encoding_subtitleoptions(body)

Updates the subtitle options

Requires authentication as administrator

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
api_instance = embyapi.SubtitleOptionsServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream

try:
    # Updates the subtitle options
    api_instance.post_encoding_subtitleoptions(body)
except ApiException as e:
    print("Exception when calling SubtitleOptionsServiceApi->post_encoding_subtitleoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

