# embyapi.LibraryStructureServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_library_virtualfolders**](LibraryStructureServiceApi.md#delete_library_virtualfolders) | **DELETE** /Library/VirtualFolders | 
[**delete_library_virtualfolders_paths**](LibraryStructureServiceApi.md#delete_library_virtualfolders_paths) | **DELETE** /Library/VirtualFolders/Paths | 
[**get_library_virtualfolders_query**](LibraryStructureServiceApi.md#get_library_virtualfolders_query) | **GET** /Library/VirtualFolders/Query | 
[**post_library_virtualfolders**](LibraryStructureServiceApi.md#post_library_virtualfolders) | **POST** /Library/VirtualFolders | 
[**post_library_virtualfolders_delete**](LibraryStructureServiceApi.md#post_library_virtualfolders_delete) | **POST** /Library/VirtualFolders/Delete | 
[**post_library_virtualfolders_libraryoptions**](LibraryStructureServiceApi.md#post_library_virtualfolders_libraryoptions) | **POST** /Library/VirtualFolders/LibraryOptions | 
[**post_library_virtualfolders_name**](LibraryStructureServiceApi.md#post_library_virtualfolders_name) | **POST** /Library/VirtualFolders/Name | 
[**post_library_virtualfolders_paths**](LibraryStructureServiceApi.md#post_library_virtualfolders_paths) | **POST** /Library/VirtualFolders/Paths | 
[**post_library_virtualfolders_paths_delete**](LibraryStructureServiceApi.md#post_library_virtualfolders_paths_delete) | **POST** /Library/VirtualFolders/Paths/Delete | 
[**post_library_virtualfolders_paths_update**](LibraryStructureServiceApi.md#post_library_virtualfolders_paths_update) | **POST** /Library/VirtualFolders/Paths/Update | 

# **delete_library_virtualfolders**
> delete_library_virtualfolders()



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))

try:
    api_instance.delete_library_virtualfolders()
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->delete_library_virtualfolders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_virtualfolders_paths**
> delete_library_virtualfolders_paths()



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))

try:
    api_instance.delete_library_virtualfolders_paths()
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->delete_library_virtualfolders_paths: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_virtualfolders_query**
> QueryResultVirtualFolderInfo get_library_virtualfolders_query(start_index=start_index, limit=limit)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)

try:
    api_response = api_instance.get_library_virtualfolders_query(start_index=start_index, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->get_library_virtualfolders_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**QueryResultVirtualFolderInfo**](QueryResultVirtualFolderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders**
> post_library_virtualfolders(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryAddVirtualFolder() # LibraryAddVirtualFolder | AddVirtualFolder

try:
    api_instance.post_library_virtualfolders(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryAddVirtualFolder**](LibraryAddVirtualFolder.md)| AddVirtualFolder | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_delete**
> post_library_virtualfolders_delete(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryRemoveVirtualFolder() # LibraryRemoveVirtualFolder | RemoveVirtualFolder

try:
    api_instance.post_library_virtualfolders_delete(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryRemoveVirtualFolder**](LibraryRemoveVirtualFolder.md)| RemoveVirtualFolder | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_libraryoptions**
> post_library_virtualfolders_libraryoptions(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryUpdateLibraryOptions() # LibraryUpdateLibraryOptions | UpdateLibraryOptions

try:
    api_instance.post_library_virtualfolders_libraryoptions(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_libraryoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryUpdateLibraryOptions**](LibraryUpdateLibraryOptions.md)| UpdateLibraryOptions | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_name**
> post_library_virtualfolders_name(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryRenameVirtualFolder() # LibraryRenameVirtualFolder | RenameVirtualFolder

try:
    api_instance.post_library_virtualfolders_name(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryRenameVirtualFolder**](LibraryRenameVirtualFolder.md)| RenameVirtualFolder | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_paths**
> post_library_virtualfolders_paths(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryAddMediaPath() # LibraryAddMediaPath | AddMediaPath

try:
    api_instance.post_library_virtualfolders_paths(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryAddMediaPath**](LibraryAddMediaPath.md)| AddMediaPath | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_paths_delete**
> post_library_virtualfolders_paths_delete(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryRemoveMediaPath() # LibraryRemoveMediaPath | RemoveMediaPath

try:
    api_instance.post_library_virtualfolders_paths_delete(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_paths_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryRemoveMediaPath**](LibraryRemoveMediaPath.md)| RemoveMediaPath | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_virtualfolders_paths_update**
> post_library_virtualfolders_paths_update(body)



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
api_instance = embyapi.LibraryStructureServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryUpdateMediaPath() # LibraryUpdateMediaPath | UpdateMediaPath

try:
    api_instance.post_library_virtualfolders_paths_update(body)
except ApiException as e:
    print("Exception when calling LibraryStructureServiceApi->post_library_virtualfolders_paths_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryUpdateMediaPath**](LibraryUpdateMediaPath.md)| UpdateMediaPath | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

