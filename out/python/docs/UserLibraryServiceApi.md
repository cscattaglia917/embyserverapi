# embyapi.UserLibraryServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_userid_favoriteitems_by_id**](UserLibraryServiceApi.md#delete_users_by_userid_favoriteitems_by_id) | **DELETE** /Users/{UserId}/FavoriteItems/{Id} | Unmarks an item as a favorite
[**delete_users_by_userid_items_by_id_rating**](UserLibraryServiceApi.md#delete_users_by_userid_items_by_id_rating) | **DELETE** /Users/{UserId}/Items/{Id}/Rating | Deletes a user&#x27;s saved personal rating for an item
[**get_livetv_programs_by_id**](UserLibraryServiceApi.md#get_livetv_programs_by_id) | **GET** /LiveTv/Programs/{Id} | Gets a live tv program
[**get_users_by_userid_items_by_id**](UserLibraryServiceApi.md#get_users_by_userid_items_by_id) | **GET** /Users/{UserId}/Items/{Id} | Gets an item from a user&#x27;s library
[**get_users_by_userid_items_by_id_intros**](UserLibraryServiceApi.md#get_users_by_userid_items_by_id_intros) | **GET** /Users/{UserId}/Items/{Id}/Intros | Gets intros to play before the main media item plays
[**get_users_by_userid_items_by_id_localtrailers**](UserLibraryServiceApi.md#get_users_by_userid_items_by_id_localtrailers) | **GET** /Users/{UserId}/Items/{Id}/LocalTrailers | Gets local trailers for an item
[**get_users_by_userid_items_by_id_specialfeatures**](UserLibraryServiceApi.md#get_users_by_userid_items_by_id_specialfeatures) | **GET** /Users/{UserId}/Items/{Id}/SpecialFeatures | Gets special features for an item
[**get_users_by_userid_items_latest**](UserLibraryServiceApi.md#get_users_by_userid_items_latest) | **GET** /Users/{UserId}/Items/Latest | Gets latest media
[**get_users_by_userid_items_root**](UserLibraryServiceApi.md#get_users_by_userid_items_root) | **GET** /Users/{UserId}/Items/Root | Gets the root folder from a user&#x27;s library
[**get_videos_by_id_additionalparts**](UserLibraryServiceApi.md#get_videos_by_id_additionalparts) | **GET** /Videos/{Id}/AdditionalParts | Gets additional parts for a video.
[**post_users_by_userid_favoriteitems_by_id**](UserLibraryServiceApi.md#post_users_by_userid_favoriteitems_by_id) | **POST** /Users/{UserId}/FavoriteItems/{Id} | Marks an item as a favorite
[**post_users_by_userid_favoriteitems_by_id_delete**](UserLibraryServiceApi.md#post_users_by_userid_favoriteitems_by_id_delete) | **POST** /Users/{UserId}/FavoriteItems/{Id}/Delete | Unmarks an item as a favorite
[**post_users_by_userid_items_by_id_hidefromresume**](UserLibraryServiceApi.md#post_users_by_userid_items_by_id_hidefromresume) | **POST** /Users/{UserId}/Items/{Id}/HideFromResume | Updates a user&#x27;s hide from resume for an item
[**post_users_by_userid_items_by_id_rating**](UserLibraryServiceApi.md#post_users_by_userid_items_by_id_rating) | **POST** /Users/{UserId}/Items/{Id}/Rating | Updates a user&#x27;s rating for an item
[**post_users_by_userid_items_by_id_rating_delete**](UserLibraryServiceApi.md#post_users_by_userid_items_by_id_rating_delete) | **POST** /Users/{UserId}/Items/{Id}/Rating/Delete | Deletes a user&#x27;s saved personal rating for an item

# **delete_users_by_userid_favoriteitems_by_id**
> UserItemDataDto delete_users_by_userid_favoriteitems_by_id(user_id, id)

Unmarks an item as a favorite

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Unmarks an item as a favorite
    api_response = api_instance.delete_users_by_userid_favoriteitems_by_id(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->delete_users_by_userid_favoriteitems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_by_userid_items_by_id_rating**
> UserItemDataDto delete_users_by_userid_items_by_id_rating(user_id, id)

Deletes a user's saved personal rating for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Deletes a user's saved personal rating for an item
    api_response = api_instance.delete_users_by_userid_items_by_id_rating(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->delete_users_by_userid_items_by_id_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_programs_by_id**
> BaseItemDto get_livetv_programs_by_id(id)

Gets a live tv program

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets a live tv program
    api_response = api_instance.get_livetv_programs_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_livetv_programs_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_by_id**
> BaseItemDto get_users_by_userid_items_by_id(user_id, id)

Gets an item from a user's library

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Gets an item from a user's library
    api_response = api_instance.get_users_by_userid_items_by_id(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_by_id_intros**
> QueryResultBaseItemDto get_users_by_userid_items_by_id_intros(user_id, id)

Gets intros to play before the main media item plays

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Gets intros to play before the main media item plays
    api_response = api_instance.get_users_by_userid_items_by_id_intros(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_by_id_intros: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_by_id_localtrailers**
> list[BaseItemDto] get_users_by_userid_items_by_id_localtrailers(user_id, id)

Gets local trailers for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Gets local trailers for an item
    api_response = api_instance.get_users_by_userid_items_by_id_localtrailers(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_by_id_localtrailers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_by_id_specialfeatures**
> list[BaseItemDto] get_users_by_userid_items_by_id_specialfeatures(user_id, id)

Gets special features for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Movie Id

try:
    # Gets special features for an item
    api_response = api_instance.get_users_by_userid_items_by_id_specialfeatures(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_by_id_specialfeatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Movie Id | 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_latest**
> list[BaseItemDto] get_users_by_userid_items_latest(user_id, limit=limit, parent_id=parent_id, fields=fields, include_item_types=include_item_types, media_types=media_types, is_folder=is_folder, is_played=is_played, group_items=group_items, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets latest media

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
limit = 56 # int | Limit (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, SortName, Studios, Taglines (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
is_folder = true # bool | Filter by items that are folders, or not. (optional)
is_played = true # bool | Filter by items that are played, or not. (optional)
group_items = true # bool | Whether or not to group items into a parent container. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
enable_user_data = true # bool | Optional, include user data (optional)

try:
    # Gets latest media
    api_response = api_instance.get_users_by_userid_items_latest(user_id, limit=limit, parent_id=parent_id, fields=fields, include_item_types=include_item_types, media_types=media_types, is_folder=is_folder, is_played=is_played, group_items=group_items, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **limit** | **int**| Limit | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, SortName, Studios, Taglines | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **is_folder** | **bool**| Filter by items that are folders, or not. | [optional] 
 **is_played** | **bool**| Filter by items that are played, or not. | [optional] 
 **group_items** | **bool**| Whether or not to group items into a parent container. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_items_root**
> BaseItemDto get_users_by_userid_items_root(user_id)

Gets the root folder from a user's library

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id

try:
    # Gets the root folder from a user's library
    api_response = api_instance.get_users_by_userid_items_root(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_users_by_userid_items_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_additionalparts**
> QueryResultBaseItemDto get_videos_by_id_additionalparts(id, user_id=user_id)

Gets additional parts for a video.

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)

try:
    # Gets additional parts for a video.
    api_response = api_instance.get_videos_by_id_additionalparts(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->get_videos_by_id_additionalparts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_favoriteitems_by_id**
> UserItemDataDto post_users_by_userid_favoriteitems_by_id(user_id, id)

Marks an item as a favorite

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Marks an item as a favorite
    api_response = api_instance.post_users_by_userid_favoriteitems_by_id(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->post_users_by_userid_favoriteitems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_favoriteitems_by_id_delete**
> UserItemDataDto post_users_by_userid_favoriteitems_by_id_delete(user_id, id)

Unmarks an item as a favorite

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Unmarks an item as a favorite
    api_response = api_instance.post_users_by_userid_favoriteitems_by_id_delete(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->post_users_by_userid_favoriteitems_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_items_by_id_hidefromresume**
> UserItemDataDto post_users_by_userid_items_by_id_hidefromresume(user_id, id, hide)

Updates a user's hide from resume for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
hide = true # bool | Whether the item should be hidden from reusme or not. true/false

try:
    # Updates a user's hide from resume for an item
    api_response = api_instance.post_users_by_userid_items_by_id_hidefromresume(user_id, id, hide)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->post_users_by_userid_items_by_id_hidefromresume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **hide** | **bool**| Whether the item should be hidden from reusme or not. true/false | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_items_by_id_rating**
> UserItemDataDto post_users_by_userid_items_by_id_rating(user_id, id, likes)

Updates a user's rating for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id
likes = true # bool | Whether the user likes the item or not. true/false

try:
    # Updates a user's rating for an item
    api_response = api_instance.post_users_by_userid_items_by_id_rating(user_id, id, likes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->post_users_by_userid_items_by_id_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **likes** | **bool**| Whether the user likes the item or not. true/false | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_items_by_id_rating_delete**
> UserItemDataDto post_users_by_userid_items_by_id_rating_delete(user_id, id)

Deletes a user's saved personal rating for an item

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
api_instance = embyapi.UserLibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
id = 'id_example' # str | Item Id

try:
    # Deletes a user's saved personal rating for an item
    api_response = api_instance.post_users_by_userid_items_by_id_rating_delete(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLibraryServiceApi->post_users_by_userid_items_by_id_rating_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

