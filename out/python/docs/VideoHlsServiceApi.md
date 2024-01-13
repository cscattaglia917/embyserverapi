# embyapi.VideoHlsServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**](VideoHlsServiceApi.md#get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Videos/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_videos_by_id_live_m3u8**](VideoHlsServiceApi.md#get_videos_by_id_live_m3u8) | **GET** /Videos/{Id}/live.m3u8 | 

# **get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**
> get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.VideoHlsServiceApi()
segment_container = 'segment_container_example' # str | 
segment_id = 'segment_id_example' # str | 
id = 'id_example' # str | 
playlist_id = 'playlist_id_example' # str | 

try:
    api_instance.get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
except ApiException as e:
    print("Exception when calling VideoHlsServiceApi->get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_container** | **str**|  | 
 **segment_id** | **str**|  | 
 **id** | **str**|  | 
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_live_m3u8**
> get_videos_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



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
api_instance = embyapi.VideoHlsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = embyapi.DlnaSubtitleDeliveryMethod() # DlnaSubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    api_instance.get_videos_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling VideoHlsServiceApi->get_videos_by_id_live_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**DlnaSubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

