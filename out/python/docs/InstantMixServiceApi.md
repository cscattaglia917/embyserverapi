# embyapi.InstantMixServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_albums_by_id_instantmix**](InstantMixServiceApi.md#get_albums_by_id_instantmix) | **GET** /Albums/{Id}/InstantMix | Creates an instant playlist based on a given album
[**get_artists_instantmix**](InstantMixServiceApi.md#get_artists_instantmix) | **GET** /Artists/InstantMix | Creates an instant playlist based on a given artist
[**get_audiobooks_nextup**](InstantMixServiceApi.md#get_audiobooks_nextup) | **GET** /AudioBooks/NextUp | Gets a list of next up episodes
[**get_items_by_id_instantmix**](InstantMixServiceApi.md#get_items_by_id_instantmix) | **GET** /Items/{Id}/InstantMix | Creates an instant playlist based on a given item
[**get_musicgenres_by_name_instantmix**](InstantMixServiceApi.md#get_musicgenres_by_name_instantmix) | **GET** /MusicGenres/{Name}/InstantMix | Creates an instant playlist based on a music genre
[**get_musicgenres_instantmix**](InstantMixServiceApi.md#get_musicgenres_instantmix) | **GET** /MusicGenres/InstantMix | Creates an instant playlist based on a music genre
[**get_playlists_by_id_instantmix**](InstantMixServiceApi.md#get_playlists_by_id_instantmix) | **GET** /Playlists/{Id}/InstantMix | Creates an instant playlist based on a given playlist
[**get_songs_by_id_instantmix**](InstantMixServiceApi.md#get_songs_by_id_instantmix) | **GET** /Songs/{Id}/InstantMix | Creates an instant playlist based on a given song

# **get_albums_by_id_instantmix**
> QueryResultBaseItemDto get_albums_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given album

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a given album
    api_response = api_instance.get_albums_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_albums_by_id_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists_instantmix**
> QueryResultBaseItemDto get_artists_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given artist

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a given artist
    api_response = api_instance.get_artists_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_artists_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiobooks_nextup**
> QueryResultBaseItemDto get_audiobooks_nextup(user_id, start_index=start_index, limit=limit, fields=fields, album_id=album_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets a list of next up episodes

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)
album_id = 'album_id_example' # str | Optional. Filter by series id (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
enable_user_data = true # bool | Optional, include user data (optional)

try:
    # Gets a list of next up episodes
    api_response = api_instance.get_audiobooks_nextup(user_id, start_index=start_index, limit=limit, fields=fields, album_id=album_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_audiobooks_nextup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 
 **album_id** | **str**| Optional. Filter by series id | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_instantmix**
> QueryResultBaseItemDto get_items_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given item

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a given item
    api_response = api_instance.get_items_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_items_by_id_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_by_name_instantmix**
> QueryResultBaseItemDto get_musicgenres_by_name_instantmix(name, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a music genre

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | The genre name
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a music genre
    api_response = api_instance.get_musicgenres_by_name_instantmix(name, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_musicgenres_by_name_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The genre name | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_instantmix**
> QueryResultBaseItemDto get_musicgenres_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a music genre

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a music genre
    api_response = api_instance.get_musicgenres_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_musicgenres_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlists_by_id_instantmix**
> QueryResultBaseItemDto get_playlists_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given playlist

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a given playlist
    api_response = api_instance.get_playlists_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_playlists_by_id_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_songs_by_id_instantmix**
> QueryResultBaseItemDto get_songs_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given song

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
api_instance = embyapi.InstantMixServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Creates an instant playlist based on a given song
    api_response = api_instance.get_songs_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMixServiceApi->get_songs_by_id_instantmix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

