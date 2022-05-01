# embyapi.ScripterXAPIApi

All URIs are relative to *http://192.168.1.6:8096/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#delete_scripterx_packages_by_installationid_by_function) | **DELETE** /ScripterX/Packages/{installationId}/{function} | 
[**get_scripterx_changelog**](ScripterXAPIApi.md#get_scripterx_changelog) | **GET** /ScripterX/ChangeLog | 
[**get_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#get_scripterx_packages_by_installationid_by_function) | **GET** /ScripterX/Packages/{installationId}/{function} | 
[**get_scripterx_packages_getconfiginterface_by_installationid**](ScripterXAPIApi.md#get_scripterx_packages_getconfiginterface_by_installationid) | **GET** /ScripterX/Packages/GetConfigInterface/{installationId} | 
[**get_scripterx_packages_info_by_installationid**](ScripterXAPIApi.md#get_scripterx_packages_info_by_installationid) | **GET** /ScripterX/Packages/Info/{installationId} | Get Installed Package Information
[**get_scripterx_packages_instances_by_packageid**](ScripterXAPIApi.md#get_scripterx_packages_instances_by_packageid) | **GET** /ScripterX/Packages/Instances/{packageId} | Get a list of Installed Packages with PackageId
[**get_scripterx_packages_reload_by_installationid**](ScripterXAPIApi.md#get_scripterx_packages_reload_by_installationid) | **GET** /ScripterX/Packages/Reload/{installationId} | 
[**get_scripterx_packages_remove_by_installationid**](ScripterXAPIApi.md#get_scripterx_packages_remove_by_installationid) | **GET** /ScripterX/Packages/Remove/{installationId} | 
[**head_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#head_scripterx_packages_by_installationid_by_function) | **HEAD** /ScripterX/Packages/{installationId}/{function} | 
[**options_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#options_scripterx_packages_by_installationid_by_function) | **OPTIONS** /ScripterX/Packages/{installationId}/{function} | 
[**patch_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#patch_scripterx_packages_by_installationid_by_function) | **PATCH** /ScripterX/Packages/{installationId}/{function} | 
[**post_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#post_scripterx_packages_by_installationid_by_function) | **POST** /ScripterX/Packages/{installationId}/{function} | 
[**post_scripterx_packages_saveconfig_by_installationid**](ScripterXAPIApi.md#post_scripterx_packages_saveconfig_by_installationid) | **POST** /ScripterX/Packages/SaveConfig/{installationId} | Save Package Configuration
[**post_scripterx_packages_upload**](ScripterXAPIApi.md#post_scripterx_packages_upload) | **POST** /ScripterX/Packages/Upload | Upload ZIP Package to ScripterX
[**put_scripterx_packages_by_installationid_by_function**](ScripterXAPIApi.md#put_scripterx_packages_by_installationid_by_function) | **PUT** /ScripterX/Packages/{installationId}/{function} | 

# **delete_scripterx_packages_by_installationid_by_function**
> object delete_scripterx_packages_by_installationid_by_function(installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.delete_scripterx_packages_by_installationid_by_function(installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->delete_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_changelog**
> str get_scripterx_changelog()



Retrieve ScripterX Change Log --- Requires authentication as user

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_scripterx_changelog()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_changelog: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_by_installationid_by_function**
> object get_scripterx_packages_by_installationid_by_function(installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.get_scripterx_packages_by_installationid_by_function(installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_getconfiginterface_by_installationid**
> str get_scripterx_packages_getconfiginterface_by_installationid(installation_id)



Get ScripterX Package Config Interface --- Requires authentication as user

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
installation_id = 'installation_id_example' # str | 

try:
    api_response = api_instance.get_scripterx_packages_getconfiginterface_by_installationid(installation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_getconfiginterface_by_installationid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 

### Return type

**str**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_info_by_installationid**
> EmbyScripterXPackagesPackageInfo get_scripterx_packages_info_by_installationid(installation_id)

Get Installed Package Information

Get Installed Package Information --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
installation_id = 'installation_id_example' # str | 

try:
    # Get Installed Package Information
    api_response = api_instance.get_scripterx_packages_info_by_installationid(installation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_info_by_installationid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 

### Return type

[**EmbyScripterXPackagesPackageInfo**](EmbyScripterXPackagesPackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_instances_by_packageid**
> list[EmbyScripterXPackagesPackageInfo] get_scripterx_packages_instances_by_packageid(package_id)

Get a list of Installed Packages with PackageId

Get a list of Installed Packages with PackageId --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
package_id = 'package_id_example' # str | 

try:
    # Get a list of Installed Packages with PackageId
    api_response = api_instance.get_scripterx_packages_instances_by_packageid(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_instances_by_packageid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  | 

### Return type

[**list[EmbyScripterXPackagesPackageInfo]**](EmbyScripterXPackagesPackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_reload_by_installationid**
> EmbyScripterXPackagesPackageReloadResult get_scripterx_packages_reload_by_installationid(installation_id)



Reload a ScripterX Package Instance --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
installation_id = 'installation_id_example' # str | 

try:
    api_response = api_instance.get_scripterx_packages_reload_by_installationid(installation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_reload_by_installationid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 

### Return type

[**EmbyScripterXPackagesPackageReloadResult**](EmbyScripterXPackagesPackageReloadResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scripterx_packages_remove_by_installationid**
> EmbyScripterXPackagesPackageUninstallResult get_scripterx_packages_remove_by_installationid(installation_id)



Uninstall a ScripterX Package --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
installation_id = 'installation_id_example' # str | 

try:
    api_response = api_instance.get_scripterx_packages_remove_by_installationid(installation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->get_scripterx_packages_remove_by_installationid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 

### Return type

[**EmbyScripterXPackagesPackageUninstallResult**](EmbyScripterXPackagesPackageUninstallResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_scripterx_packages_by_installationid_by_function**
> object head_scripterx_packages_by_installationid_by_function(installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.head_scripterx_packages_by_installationid_by_function(installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->head_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_scripterx_packages_by_installationid_by_function**
> object options_scripterx_packages_by_installationid_by_function(installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.options_scripterx_packages_by_installationid_by_function(installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->options_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_scripterx_packages_by_installationid_by_function**
> object patch_scripterx_packages_by_installationid_by_function(installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.patch_scripterx_packages_by_installationid_by_function(installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->patch_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scripterx_packages_by_installationid_by_function**
> object post_scripterx_packages_by_installationid_by_function(body, installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
body = embyapi.Object() # Object | Binary stream
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.post_scripterx_packages_by_installationid_by_function(body, installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->post_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scripterx_packages_saveconfig_by_installationid**
> str post_scripterx_packages_saveconfig_by_installationid(body, installation_id)

Save Package Configuration

Save Package Configuration --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
installation_id = 'installation_id_example' # str | 

try:
    # Save Package Configuration
    api_response = api_instance.post_scripterx_packages_saveconfig_by_installationid(body, installation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->post_scripterx_packages_saveconfig_by_installationid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **installation_id** | **str**|  | 

### Return type

**str**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scripterx_packages_upload**
> EmbyScripterXPackagesPackageInstallerResult post_scripterx_packages_upload(body)

Upload ZIP Package to ScripterX

Upload ZIP Package to ScripterX --- Requires authentication as administrator

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
api_instance = embyapi.ScripterXAPIApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream

try:
    # Upload ZIP Package to ScripterX
    api_response = api_instance.post_scripterx_packages_upload(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->post_scripterx_packages_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 

### Return type

[**EmbyScripterXPackagesPackageInstallerResult**](EmbyScripterXPackagesPackageInstallerResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_scripterx_packages_by_installationid_by_function**
> object put_scripterx_packages_by_installationid_by_function(body, installation_id, function)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ScripterXAPIApi()
body = embyapi.Object() # Object | Binary stream
installation_id = 'installation_id_example' # str | 
function = 'function_example' # str | 

try:
    api_response = api_instance.put_scripterx_packages_by_installationid_by_function(body, installation_id, function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScripterXAPIApi->put_scripterx_packages_by_installationid_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **installation_id** | **str**|  | 
 **function** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

