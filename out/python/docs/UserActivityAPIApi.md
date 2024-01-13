# embyapi.UserActivityAPIApi

All URIs are relative to *http://emby.scattaglia.com/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_usage_stats_by_breakdowntype_breakdownreport**](UserActivityAPIApi.md#get_user_usage_stats_by_breakdowntype_breakdownreport) | **GET** /user_usage_stats/{BreakdownType}/BreakdownReport | Gets a breakdown of a usage metric
[**get_user_usage_stats_by_userid_by_date_getitems**](UserActivityAPIApi.md#get_user_usage_stats_by_userid_by_date_getitems) | **GET** /user_usage_stats/{UserID}/{Date}/GetItems | Gets activity for {USER} for {Date} formatted as yyyy-MM-dd
[**get_user_usage_stats_get_item_path**](UserActivityAPIApi.md#get_user_usage_stats_get_item_path) | **GET** /user_usage_stats/get_item_path | Get a list of items for type and filtered
[**get_user_usage_stats_get_item_stats**](UserActivityAPIApi.md#get_user_usage_stats_get_item_stats) | **GET** /user_usage_stats/get_item_stats | Get a list of items for type and filtered
[**get_user_usage_stats_get_items**](UserActivityAPIApi.md#get_user_usage_stats_get_items) | **GET** /user_usage_stats/get_items | Get a list of items for type and filtered
[**get_user_usage_stats_hourlyreport**](UserActivityAPIApi.md#get_user_usage_stats_hourlyreport) | **GET** /user_usage_stats/HourlyReport | Gets a report of the available activity per hour
[**get_user_usage_stats_load_backup**](UserActivityAPIApi.md#get_user_usage_stats_load_backup) | **GET** /user_usage_stats/load_backup | Loads a backup from a file
[**get_user_usage_stats_moviesreport**](UserActivityAPIApi.md#get_user_usage_stats_moviesreport) | **GET** /user_usage_stats/MoviesReport | Gets Movies counts
[**get_user_usage_stats_playactivity**](UserActivityAPIApi.md#get_user_usage_stats_playactivity) | **GET** /user_usage_stats/PlayActivity | Gets play activity for number of days
[**get_user_usage_stats_save_backup**](UserActivityAPIApi.md#get_user_usage_stats_save_backup) | **GET** /user_usage_stats/save_backup | Saves a backup of the playback report data to the backup path
[**get_user_usage_stats_session_list**](UserActivityAPIApi.md#get_user_usage_stats_session_list) | **GET** /user_usage_stats/session_list | Gets Session Info
[**get_user_usage_stats_tvshowsreport**](UserActivityAPIApi.md#get_user_usage_stats_tvshowsreport) | **GET** /user_usage_stats/TvShowsReport | Gets TV Shows counts
[**get_user_usage_stats_type_filter_list**](UserActivityAPIApi.md#get_user_usage_stats_type_filter_list) | **GET** /user_usage_stats/type_filter_list | Gets types filter list items
[**get_user_usage_stats_user_activity**](UserActivityAPIApi.md#get_user_usage_stats_user_activity) | **GET** /user_usage_stats/user_activity | Gets a report of the available activity per hour
[**get_user_usage_stats_user_list**](UserActivityAPIApi.md#get_user_usage_stats_user_list) | **GET** /user_usage_stats/user_list | Get users
[**get_user_usage_stats_user_manage_by_action_by_id**](UserActivityAPIApi.md#get_user_usage_stats_user_manage_by_action_by_id) | **GET** /user_usage_stats/user_manage/{Action}/{Id} | Get users
[**get_user_usage_stats_userplaylist**](UserActivityAPIApi.md#get_user_usage_stats_userplaylist) | **GET** /user_usage_stats/UserPlaylist | Gets a report of all played items for a user in a date period
[**post_user_usage_stats_import_backup**](UserActivityAPIApi.md#post_user_usage_stats_import_backup) | **POST** /user_usage_stats/import_backup | Post a backup for importing
[**post_user_usage_stats_submit_custom_query**](UserActivityAPIApi.md#post_user_usage_stats_submit_custom_query) | **POST** /user_usage_stats/submit_custom_query | Submit an SQL query

# **get_user_usage_stats_by_breakdowntype_breakdownreport**
> object get_user_usage_stats_by_breakdowntype_breakdownreport(breakdown_type, user_id=user_id, days=days, end_date=end_date)

Gets a breakdown of a usage metric

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
breakdown_type = 'breakdown_type_example' # str | Breakdown type
user_id = 'user_id_example' # str | User Id (optional)
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets a breakdown of a usage metric
    api_response = api_instance.get_user_usage_stats_by_breakdowntype_breakdownreport(breakdown_type, user_id=user_id, days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_by_breakdowntype_breakdownreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **breakdown_type** | **str**| Breakdown type | 
 **user_id** | **str**| User Id | [optional] 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_by_userid_by_date_getitems**
> object get_user_usage_stats_by_userid_by_date_getitems(user_id, _date, filter=filter)

Gets activity for {USER} for {Date} formatted as yyyy-MM-dd

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
_date = '_date_example' # str | UTC DateTime, Format yyyy-MM-dd
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets activity for {USER} for {Date} formatted as yyyy-MM-dd
    api_response = api_instance.get_user_usage_stats_by_userid_by_date_getitems(user_id, _date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_by_userid_by_date_getitems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **_date** | **str**| UTC DateTime, Format yyyy-MM-dd | 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_get_item_path**
> object get_user_usage_stats_get_item_path(id)

Get a list of items for type and filtered

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
id = 56 # int | item id

try:
    # Get a list of items for type and filtered
    api_response = api_instance.get_user_usage_stats_get_item_path(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_get_item_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| item id | 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_get_item_stats**
> object get_user_usage_stats_get_item_stats(id)

Get a list of items for type and filtered

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
id = 56 # int | item id

try:
    # Get a list of items for type and filtered
    api_response = api_instance.get_user_usage_stats_get_item_stats(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_get_item_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| item id | 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_get_items**
> object get_user_usage_stats_get_items(filter=filter, item_type=item_type, parent=parent)

Get a list of items for type and filtered

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
filter = 'filter_example' # str | filter string (optional)
item_type = 'item_type_example' # str | type of items to return (optional)
parent = 56 # int | parentid (optional)

try:
    # Get a list of items for type and filtered
    api_response = api_instance.get_user_usage_stats_get_items(filter=filter, item_type=item_type, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_get_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| filter string | [optional] 
 **item_type** | **str**| type of items to return | [optional] 
 **parent** | **int**| parentid | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_hourlyreport**
> object get_user_usage_stats_hourlyreport(user_id=user_id, days=days, end_date=end_date, filter=filter)

Gets a report of the available activity per hour

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets a report of the available activity per hour
    api_response = api_instance.get_user_usage_stats_hourlyreport(user_id=user_id, days=days, end_date=end_date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_hourlyreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_load_backup**
> object get_user_usage_stats_load_backup(backupfile)

Loads a backup from a file

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
backupfile = 'backupfile_example' # str | File name of file to load

try:
    # Loads a backup from a file
    api_response = api_instance.get_user_usage_stats_load_backup(backupfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_load_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backupfile** | **str**| File name of file to load | 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_moviesreport**
> object get_user_usage_stats_moviesreport(user_id=user_id, days=days, end_date=end_date)

Gets Movies counts

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets Movies counts
    api_response = api_instance.get_user_usage_stats_moviesreport(user_id=user_id, days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_moviesreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_playactivity**
> object get_user_usage_stats_playactivity(days=days, end_date=end_date, filter=filter, data_type=data_type)

Gets play activity for number of days

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)
data_type = 'data_type_example' # str | Data type to return (count,time) (optional)

try:
    # Gets play activity for number of days
    api_response = api_instance.get_user_usage_stats_playactivity(days=days, end_date=end_date, filter=filter, data_type=data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_playactivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 
 **data_type** | **str**| Data type to return (count,time) | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_save_backup**
> object get_user_usage_stats_save_backup()

Saves a backup of the playback report data to the backup path

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))

try:
    # Saves a backup of the playback report data to the backup path
    api_response = api_instance.get_user_usage_stats_save_backup()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_save_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_session_list**
> object get_user_usage_stats_session_list()

Gets Session Info

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))

try:
    # Gets Session Info
    api_response = api_instance.get_user_usage_stats_session_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_session_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_tvshowsreport**
> object get_user_usage_stats_tvshowsreport(user_id=user_id, days=days, end_date=end_date)

Gets TV Shows counts

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets TV Shows counts
    api_response = api_instance.get_user_usage_stats_tvshowsreport(user_id=user_id, days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_tvshowsreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_type_filter_list**
> object get_user_usage_stats_type_filter_list()

Gets types filter list items

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))

try:
    # Gets types filter list items
    api_response = api_instance.get_user_usage_stats_type_filter_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_type_filter_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_activity**
> object get_user_usage_stats_user_activity(days=days, end_date=end_date)

Gets a report of the available activity per hour

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets a report of the available activity per hour
    api_response = api_instance.get_user_usage_stats_user_activity(days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_list**
> object get_user_usage_stats_user_list()

Get users

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))

try:
    # Get users
    api_response = api_instance.get_user_usage_stats_user_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_manage_by_action_by_id**
> object get_user_usage_stats_user_manage_by_action_by_id(action, id)

Get users

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
action = 'action_example' # str | action to perform
id = 'id_example' # str | user Id to perform the action on

try:
    # Get users
    api_response = api_instance.get_user_usage_stats_user_manage_by_action_by_id(action, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_manage_by_action_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action to perform | 
 **id** | **str**| user Id to perform the action on | 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_userplaylist**
> object get_user_usage_stats_userplaylist(user_id, aggregate_data, filter_name=filter_name, days=days, end_date=end_date, filter=filter)

Gets a report of all played items for a user in a date period

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
aggregate_data = true # bool | Aggregate the data to total duration per user per item
filter_name = 'filter_name_example' # str | Name Filter (optional)
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets a report of all played items for a user in a date period
    api_response = api_instance.get_user_usage_stats_userplaylist(user_id, aggregate_data, filter_name=filter_name, days=days, end_date=end_date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_userplaylist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **aggregate_data** | **bool**| Aggregate the data to total duration per user per item | 
 **filter_name** | **str**| Name Filter | [optional] 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_usage_stats_import_backup**
> post_user_usage_stats_import_backup(body)

Post a backup for importing

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream

try:
    # Post a backup for importing
    api_instance.post_user_usage_stats_import_backup(body)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->post_user_usage_stats_import_backup: %s\n" % e)
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

# **post_user_usage_stats_submit_custom_query**
> object post_user_usage_stats_submit_custom_query(body)

Submit an SQL query

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
api_instance = embyapi.UserActivityAPIApi(embyapi.ApiClient(configuration))
body = embyapi.PlaybackReportingApiCustomQuery() # PlaybackReportingApiCustomQuery | CustomQuery

try:
    # Submit an SQL query
    api_response = api_instance.post_user_usage_stats_submit_custom_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->post_user_usage_stats_submit_custom_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaybackReportingApiCustomQuery**](PlaybackReportingApiCustomQuery.md)| CustomQuery | 

### Return type

**object**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

