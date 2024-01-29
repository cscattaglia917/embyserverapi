# embyapi.ServerApiEndpointsApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_notification_pushover_test_by_userid**](ServerApiEndpointsApi.md#post_notification_pushover_test_by_userid) | **POST** /Notification/Pushover/Test/{UserID} | Tests Pushover

# **post_notification_pushover_test_by_userid**
> post_notification_pushover_test_by_userid(user_id)

Tests Pushover

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ServerApiEndpointsApi()
user_id = 'user_id_example' # str | User Id

try:
    # Tests Pushover
    api_instance.post_notification_pushover_test_by_userid(user_id)
except ApiException as e:
    print("Exception when calling ServerApiEndpointsApi->post_notification_pushover_test_by_userid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

