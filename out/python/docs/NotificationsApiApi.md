# embyapi.NotificationsApiApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications_all**](NotificationsApiApi.md#get_notifications_all) | **GET** /Notifications/All | Gets notification types

# **get_notifications_all**
> list[EmbyNotificationsNotificationCategoryInfo] get_notifications_all()

Gets notification types

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
api_instance = embyapi.NotificationsApiApi(embyapi.ApiClient(configuration))

try:
    # Gets notification types
    api_response = api_instance.get_notifications_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApiApi->get_notifications_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EmbyNotificationsNotificationCategoryInfo]**](EmbyNotificationsNotificationCategoryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

