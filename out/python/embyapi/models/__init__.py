# coding: utf-8

# flake8: noqa
"""
    Emby REST API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.7.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from embyapi.models.activity_log_entry import ActivityLogEntry
from embyapi.models.all_theme_media_result import AllThemeMediaResult
from embyapi.models.attributes_simple_condition import AttributesSimpleCondition
from embyapi.models.attributes_value_condition import AttributesValueCondition
from embyapi.models.authenticate_user import AuthenticateUser
from embyapi.models.authenticate_user_by_name import AuthenticateUserByName
from embyapi.models.authentication_authentication_result import AuthenticationAuthenticationResult
from embyapi.models.base_item_dto import BaseItemDto
from embyapi.models.base_item_person import BaseItemPerson
from embyapi.models.branding_branding_options import BrandingBrandingOptions
from embyapi.models.chapter_info import ChapterInfo
from embyapi.models.client_capabilities import ClientCapabilities
from embyapi.models.collections_collection_creation_result import CollectionsCollectionCreationResult
from embyapi.models.common_plugins_i_plugin import CommonPluginsIPlugin
from embyapi.models.configuration_access_schedule import ConfigurationAccessSchedule
from embyapi.models.configuration_codec_configuration import ConfigurationCodecConfiguration
from embyapi.models.configuration_dynamic_day_of_week import ConfigurationDynamicDayOfWeek
from embyapi.models.configuration_image_option import ConfigurationImageOption
from embyapi.models.configuration_image_saving_convention import ConfigurationImageSavingConvention
from embyapi.models.configuration_library_options import ConfigurationLibraryOptions
from embyapi.models.configuration_media_path_info import ConfigurationMediaPathInfo
from embyapi.models.configuration_metadata_features import ConfigurationMetadataFeatures
from embyapi.models.configuration_path_substitution import ConfigurationPathSubstitution
from embyapi.models.configuration_segment_skip_mode import ConfigurationSegmentSkipMode
from embyapi.models.configuration_server_configuration import ConfigurationServerConfiguration
from embyapi.models.configuration_subtitle_playback_mode import ConfigurationSubtitlePlaybackMode
from embyapi.models.configuration_type_options import ConfigurationTypeOptions
from embyapi.models.configuration_unrated_item import ConfigurationUnratedItem
from embyapi.models.configuration_user_configuration import ConfigurationUserConfiguration
from embyapi.models.connect_connect_authentication_exchange_result import ConnectConnectAuthenticationExchangeResult
from embyapi.models.connect_user_link_result import ConnectUserLinkResult
from embyapi.models.connect_user_link_type import ConnectUserLinkType
from embyapi.models.create_user_by_name import CreateUserByName
from embyapi.models.day_of_week import DayOfWeek
from embyapi.models.default_directory_browser_info import DefaultDirectoryBrowserInfo
from embyapi.models.devices_content_upload_history import DevicesContentUploadHistory
from embyapi.models.devices_device_info import DevicesDeviceInfo
from embyapi.models.devices_device_options import DevicesDeviceOptions
from embyapi.models.devices_local_file_info import DevicesLocalFileInfo
from embyapi.models.display_preferences import DisplayPreferences
from embyapi.models.dlna_codec_profile import DlnaCodecProfile
from embyapi.models.dlna_codec_type import DlnaCodecType
from embyapi.models.dlna_container_profile import DlnaContainerProfile
from embyapi.models.dlna_device_profile import DlnaDeviceProfile
from embyapi.models.dlna_direct_play_profile import DlnaDirectPlayProfile
from embyapi.models.dlna_dlna_profile_type import DlnaDlnaProfileType
from embyapi.models.dlna_encoding_context import DlnaEncodingContext
from embyapi.models.dlna_playback_error_code import DlnaPlaybackErrorCode
from embyapi.models.dlna_profile_condition import DlnaProfileCondition
from embyapi.models.dlna_profile_condition_type import DlnaProfileConditionType
from embyapi.models.dlna_profile_condition_value import DlnaProfileConditionValue
from embyapi.models.dlna_response_profile import DlnaResponseProfile
from embyapi.models.dlna_subtitle_delivery_method import DlnaSubtitleDeliveryMethod
from embyapi.models.dlna_subtitle_profile import DlnaSubtitleProfile
from embyapi.models.dlna_transcode_seek_info import DlnaTranscodeSeekInfo
from embyapi.models.dlna_transcoding_profile import DlnaTranscodingProfile
from embyapi.models.drawing_image_orientation import DrawingImageOrientation
from embyapi.models.emby_dlna_profiles_device_identification import EmbyDlnaProfilesDeviceIdentification
from embyapi.models.emby_dlna_profiles_device_profile_type import EmbyDlnaProfilesDeviceProfileType
from embyapi.models.emby_dlna_profiles_dlna_profile import EmbyDlnaProfilesDlnaProfile
from embyapi.models.emby_dlna_profiles_header_match_type import EmbyDlnaProfilesHeaderMatchType
from embyapi.models.emby_dlna_profiles_http_header_info import EmbyDlnaProfilesHttpHeaderInfo
from embyapi.models.emby_dlna_profiles_protocol_info_detection import EmbyDlnaProfilesProtocolInfoDetection
from embyapi.models.emby_live_tv_channel_management_info import EmbyLiveTVChannelManagementInfo
from embyapi.models.emby_media_model_enums_codec_directions import EmbyMediaModelEnumsCodecDirections
from embyapi.models.emby_media_model_enums_codec_kinds import EmbyMediaModelEnumsCodecKinds
from embyapi.models.emby_media_model_enums_color_formats import EmbyMediaModelEnumsColorFormats
from embyapi.models.emby_media_model_enums_secondary_frameworks import EmbyMediaModelEnumsSecondaryFrameworks
from embyapi.models.emby_media_model_enums_video_media_types import EmbyMediaModelEnumsVideoMediaTypes
from embyapi.models.emby_media_model_types_bit_rate import EmbyMediaModelTypesBitRate
from embyapi.models.emby_media_model_types_level_information import EmbyMediaModelTypesLevelInformation
from embyapi.models.emby_media_model_types_profile_information import EmbyMediaModelTypesProfileInformation
from embyapi.models.emby_media_model_types_profile_level_information import EmbyMediaModelTypesProfileLevelInformation
from embyapi.models.emby_media_model_types_resolution import EmbyMediaModelTypesResolution
from embyapi.models.emby_media_model_types_resolution_with_rate import EmbyMediaModelTypesResolutionWithRate
from embyapi.models.emby_notifications_api_notification import EmbyNotificationsApiNotification
from embyapi.models.emby_notifications_api_notification_result import EmbyNotificationsApiNotificationResult
from embyapi.models.emby_notifications_api_notifications_summary import EmbyNotificationsApiNotificationsSummary
from embyapi.models.emby_web_api_configuration_page_info import EmbyWebApiConfigurationPageInfo
from embyapi.models.emby_web_generic_edit_actions_postback_action import EmbyWebGenericEditActionsPostbackAction
from embyapi.models.emby_web_generic_edit_common_editor_types import EmbyWebGenericEditCommonEditorTypes
from embyapi.models.emby_web_generic_edit_conditions_property_condition import EmbyWebGenericEditConditionsPropertyCondition
from embyapi.models.emby_web_generic_edit_conditions_property_condition_type import EmbyWebGenericEditConditionsPropertyConditionType
from embyapi.models.emby_web_generic_edit_edit_object_container import EmbyWebGenericEditEditObjectContainer
from embyapi.models.emby_web_generic_edit_editors_editor_base import EmbyWebGenericEditEditorsEditorBase
from embyapi.models.emby_web_generic_edit_editors_editor_button_item import EmbyWebGenericEditEditorsEditorButtonItem
from embyapi.models.emby_web_generic_edit_editors_editor_root import EmbyWebGenericEditEditorsEditorRoot
from embyapi.models.external_id_info import ExternalIdInfo
from embyapi.models.external_url import ExternalUrl
from embyapi.models.forgot_password import ForgotPassword
from embyapi.models.forgot_password_pin import ForgotPasswordPin
from embyapi.models.game_system_summary import GameSystemSummary
from embyapi.models.general_command import GeneralCommand
from embyapi.models.globalization_country_info import GlobalizationCountryInfo
from embyapi.models.globalization_culture_dto import GlobalizationCultureDto
from embyapi.models.globalization_localizaton_option import GlobalizationLocalizatonOption
from embyapi.models.io_file_system_entry_info import IOFileSystemEntryInfo
from embyapi.models.io_file_system_entry_type import IOFileSystemEntryType
from embyapi.models.image_by_name_info import ImageByNameInfo
from embyapi.models.image_info import ImageInfo
from embyapi.models.image_provider_info import ImageProviderInfo
from embyapi.models.image_type import ImageType
from embyapi.models.item_counts import ItemCounts
from embyapi.models.library_add_media_path import LibraryAddMediaPath
from embyapi.models.library_add_virtual_folder import LibraryAddVirtualFolder
from embyapi.models.library_delete_info import LibraryDeleteInfo
from embyapi.models.library_library_option_info import LibraryLibraryOptionInfo
from embyapi.models.library_library_options_result import LibraryLibraryOptionsResult
from embyapi.models.library_library_type_options import LibraryLibraryTypeOptions
from embyapi.models.library_media_folder import LibraryMediaFolder
from embyapi.models.library_media_update_info import LibraryMediaUpdateInfo
from embyapi.models.library_play_access import LibraryPlayAccess
from embyapi.models.library_post_updated_media import LibraryPostUpdatedMedia
from embyapi.models.library_remove_media_path import LibraryRemoveMediaPath
from embyapi.models.library_remove_virtual_folder import LibraryRemoveVirtualFolder
from embyapi.models.library_rename_virtual_folder import LibraryRenameVirtualFolder
from embyapi.models.library_sub_folder import LibrarySubFolder
from embyapi.models.library_update_library_options import LibraryUpdateLibraryOptions
from embyapi.models.library_update_media_path import LibraryUpdateMediaPath
from embyapi.models.live_tv_api_epg_row import LiveTVApiEpgRow
from embyapi.models.live_tv_api_get_programs import LiveTVApiGetPrograms
from embyapi.models.live_tv_api_listing_provider_type_info import LiveTVApiListingProviderTypeInfo
from embyapi.models.live_tv_api_set_channel_disabled import LiveTVApiSetChannelDisabled
from embyapi.models.live_tv_api_set_channel_mapping import LiveTVApiSetChannelMapping
from embyapi.models.live_tv_api_set_channel_sort_index import LiveTVApiSetChannelSortIndex
from embyapi.models.live_tv_api_tag_item import LiveTVApiTagItem
from embyapi.models.live_tv_channel_type import LiveTvChannelType
from embyapi.models.live_tv_guide_info import LiveTvGuideInfo
from embyapi.models.live_tv_keep_until import LiveTvKeepUntil
from embyapi.models.live_tv_keyword_info import LiveTvKeywordInfo
from embyapi.models.live_tv_keyword_type import LiveTvKeywordType
from embyapi.models.live_tv_listings_provider_info import LiveTvListingsProviderInfo
from embyapi.models.live_tv_live_tv_info import LiveTvLiveTvInfo
from embyapi.models.live_tv_recording_status import LiveTvRecordingStatus
from embyapi.models.live_tv_series_timer_info import LiveTvSeriesTimerInfo
from embyapi.models.live_tv_series_timer_info_dto import LiveTvSeriesTimerInfoDto
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto
from embyapi.models.live_tv_timer_type import LiveTvTimerType
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo
from embyapi.models.location_type import LocationType
from embyapi.models.log_file import LogFile
from embyapi.models.logging_log_severity import LoggingLogSeverity
from embyapi.models.marker_type import MarkerType
from embyapi.models.media_encoding_api_on_playback_progress import MediaEncodingApiOnPlaybackProgress
from embyapi.models.media_encoding_codecs_common_interfaces_i_codec_device_capabilities import MediaEncodingCodecsCommonInterfacesICodecDeviceCapabilities
from embyapi.models.media_encoding_codecs_common_interfaces_i_codec_device_info import MediaEncodingCodecsCommonInterfacesICodecDeviceInfo
from embyapi.models.media_encoding_codecs_video_codecs_video_codec_base import MediaEncodingCodecsVideoCodecsVideoCodecBase
from embyapi.models.media_encoding_configuration_tone_mapping_tone_map_options_visibility import MediaEncodingConfigurationToneMappingToneMapOptionsVisibility
from embyapi.models.media_info_live_stream_request import MediaInfoLiveStreamRequest
from embyapi.models.media_info_live_stream_response import MediaInfoLiveStreamResponse
from embyapi.models.media_info_media_protocol import MediaInfoMediaProtocol
from embyapi.models.media_info_playback_info_request import MediaInfoPlaybackInfoRequest
from embyapi.models.media_info_playback_info_response import MediaInfoPlaybackInfoResponse
from embyapi.models.media_info_transport_stream_timestamp import MediaInfoTransportStreamTimestamp
from embyapi.models.media_source_info import MediaSourceInfo
from embyapi.models.media_source_type import MediaSourceType
from embyapi.models.media_stream import MediaStream
from embyapi.models.media_stream_type import MediaStreamType
from embyapi.models.media_url import MediaUrl
from embyapi.models.metadata_editor_info import MetadataEditorInfo
from embyapi.models.metadata_fields import MetadataFields
from embyapi.models.name_id_pair import NameIdPair
from embyapi.models.name_long_id_pair import NameLongIdPair
from embyapi.models.name_value_pair import NameValuePair
from embyapi.models.net_end_point_info import NetEndPointInfo
from embyapi.models.notifications_notification_level import NotificationsNotificationLevel
from embyapi.models.notifications_notification_type_info import NotificationsNotificationTypeInfo
from embyapi.models.operating_system import OperatingSystem
from embyapi.models.parental_rating import ParentalRating
from embyapi.models.persistence_intro_debug_info import PersistenceIntroDebugInfo
from embyapi.models.person_type import PersonType
from embyapi.models.play_command import PlayCommand
from embyapi.models.play_method import PlayMethod
from embyapi.models.play_request import PlayRequest
from embyapi.models.playback_progress_info import PlaybackProgressInfo
from embyapi.models.playback_start_info import PlaybackStartInfo
from embyapi.models.playback_stop_info import PlaybackStopInfo
from embyapi.models.player_state_info import PlayerStateInfo
from embyapi.models.playlists_playlist_creation_result import PlaylistsPlaylistCreationResult
from embyapi.models.playstate_command import PlaystateCommand
from embyapi.models.playstate_request import PlaystateRequest
from embyapi.models.plugins_configuration_page_type import PluginsConfigurationPageType
from embyapi.models.plugins_plugin_info import PluginsPluginInfo
from embyapi.models.progress_event import ProgressEvent
from embyapi.models.provider_id_dictionary import ProviderIdDictionary
from embyapi.models.providers_album_info import ProvidersAlbumInfo
from embyapi.models.providers_artist_info import ProvidersArtistInfo
from embyapi.models.providers_book_info import ProvidersBookInfo
from embyapi.models.providers_game_info import ProvidersGameInfo
from embyapi.models.providers_item_lookup_info import ProvidersItemLookupInfo
from embyapi.models.providers_metadata_refresh_mode import ProvidersMetadataRefreshMode
from embyapi.models.providers_movie_info import ProvidersMovieInfo
from embyapi.models.providers_music_video_info import ProvidersMusicVideoInfo
from embyapi.models.providers_person_lookup_info import ProvidersPersonLookupInfo
from embyapi.models.providers_remote_search_query_providers_album_info import ProvidersRemoteSearchQueryProvidersAlbumInfo
from embyapi.models.providers_remote_search_query_providers_artist_info import ProvidersRemoteSearchQueryProvidersArtistInfo
from embyapi.models.providers_remote_search_query_providers_book_info import ProvidersRemoteSearchQueryProvidersBookInfo
from embyapi.models.providers_remote_search_query_providers_game_info import ProvidersRemoteSearchQueryProvidersGameInfo
from embyapi.models.providers_remote_search_query_providers_item_lookup_info import ProvidersRemoteSearchQueryProvidersItemLookupInfo
from embyapi.models.providers_remote_search_query_providers_movie_info import ProvidersRemoteSearchQueryProvidersMovieInfo
from embyapi.models.providers_remote_search_query_providers_music_video_info import ProvidersRemoteSearchQueryProvidersMusicVideoInfo
from embyapi.models.providers_remote_search_query_providers_person_lookup_info import ProvidersRemoteSearchQueryProvidersPersonLookupInfo
from embyapi.models.providers_remote_search_query_providers_series_info import ProvidersRemoteSearchQueryProvidersSeriesInfo
from embyapi.models.providers_remote_search_query_providers_trailer_info import ProvidersRemoteSearchQueryProvidersTrailerInfo
from embyapi.models.providers_series_info import ProvidersSeriesInfo
from embyapi.models.providers_song_info import ProvidersSongInfo
from embyapi.models.providers_trailer_info import ProvidersTrailerInfo
from embyapi.models.public_system_info import PublicSystemInfo
from embyapi.models.query_result_activity_log_entry import QueryResultActivityLogEntry
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
from embyapi.models.query_result_devices_device_info import QueryResultDevicesDeviceInfo
from embyapi.models.query_result_emby_live_tv_channel_management_info import QueryResultEmbyLiveTVChannelManagementInfo
from embyapi.models.query_result_live_tv_api_epg_row import QueryResultLiveTVApiEpgRow
from embyapi.models.query_result_live_tv_series_timer_info_dto import QueryResultLiveTvSeriesTimerInfoDto
from embyapi.models.query_result_live_tv_timer_info_dto import QueryResultLiveTvTimerInfoDto
from embyapi.models.query_result_log_file import QueryResultLogFile
from embyapi.models.query_result_string import QueryResultString
from embyapi.models.query_result_sync_model_sync_job_item import QueryResultSyncModelSyncJobItem
from embyapi.models.query_result_sync_sync_job import QueryResultSyncSyncJob
from embyapi.models.query_result_user_dto import QueryResultUserDto
from embyapi.models.query_result_user_library_official_rating_item import QueryResultUserLibraryOfficialRatingItem
from embyapi.models.query_result_user_library_tag_item import QueryResultUserLibraryTagItem
from embyapi.models.query_result_virtual_folder_info import QueryResultVirtualFolderInfo
from embyapi.models.queue_item import QueueItem
from embyapi.models.rating_type import RatingType
from embyapi.models.recommendation_dto import RecommendationDto
from embyapi.models.recommendation_type import RecommendationType
from embyapi.models.remote_image_info import RemoteImageInfo
from embyapi.models.remote_image_result import RemoteImageResult
from embyapi.models.remote_search_result import RemoteSearchResult
from embyapi.models.remote_subtitle_info import RemoteSubtitleInfo
from embyapi.models.repeat_mode import RepeatMode
from embyapi.models.roku_metadata_api_thumbnail_info import RokuMetadataApiThumbnailInfo
from embyapi.models.roku_metadata_api_thumbnail_set_info import RokuMetadataApiThumbnailSetInfo
from embyapi.models.scroll_direction import ScrollDirection
from embyapi.models.series_display_order import SeriesDisplayOrder
from embyapi.models.session_session_info import SessionSessionInfo
from embyapi.models.session_user_info import SessionUserInfo
from embyapi.models.sort_order import SortOrder
from embyapi.models.subtitle_location_type import SubtitleLocationType
from embyapi.models.subtitles_subtitle_download_result import SubtitlesSubtitleDownloadResult
from embyapi.models.sync_model_item_file_info import SyncModelItemFileInfo
from embyapi.models.sync_model_item_file_type import SyncModelItemFileType
from embyapi.models.sync_model_sync_data_request import SyncModelSyncDataRequest
from embyapi.models.sync_model_sync_data_response import SyncModelSyncDataResponse
from embyapi.models.sync_model_sync_dialog_options import SyncModelSyncDialogOptions
from embyapi.models.sync_model_sync_job_creation_result import SyncModelSyncJobCreationResult
from embyapi.models.sync_model_sync_job_item import SyncModelSyncJobItem
from embyapi.models.sync_model_sync_job_item_status import SyncModelSyncJobItemStatus
from embyapi.models.sync_model_sync_job_option import SyncModelSyncJobOption
from embyapi.models.sync_model_sync_job_request import SyncModelSyncJobRequest
from embyapi.models.sync_model_sync_profile_option import SyncModelSyncProfileOption
from embyapi.models.sync_model_sync_quality_option import SyncModelSyncQualityOption
from embyapi.models.sync_model_synced_item import SyncModelSyncedItem
from embyapi.models.sync_model_synced_item_progress import SyncModelSyncedItemProgress
from embyapi.models.sync_sync_category import SyncSyncCategory
from embyapi.models.sync_sync_job import SyncSyncJob
from embyapi.models.sync_sync_job_status import SyncSyncJobStatus
from embyapi.models.sync_sync_target import SyncSyncTarget
from embyapi.models.system_info import SystemInfo
from embyapi.models.tasks_system_event import TasksSystemEvent
from embyapi.models.tasks_task_completion_status import TasksTaskCompletionStatus
from embyapi.models.tasks_task_info import TasksTaskInfo
from embyapi.models.tasks_task_result import TasksTaskResult
from embyapi.models.tasks_task_state import TasksTaskState
from embyapi.models.tasks_task_trigger_info import TasksTaskTriggerInfo
from embyapi.models.theme_media_result import ThemeMediaResult
from embyapi.models.transcode_reason import TranscodeReason
from embyapi.models.transcoding_info import TranscodingInfo
from embyapi.models.transcoding_vp_step_info import TranscodingVpStepInfo
from embyapi.models.transcoding_vp_step_types import TranscodingVpStepTypes
from embyapi.models.tuple_double_double import TupleDoubleDouble
from embyapi.models.update_user_easy_password import UpdateUserEasyPassword
from embyapi.models.update_user_password import UpdateUserPassword
from embyapi.models.updates_installation_info import UpdatesInstallationInfo
from embyapi.models.updates_package_info import UpdatesPackageInfo
from embyapi.models.updates_package_target_system import UpdatesPackageTargetSystem
from embyapi.models.updates_package_version_class import UpdatesPackageVersionClass
from embyapi.models.updates_package_version_info import UpdatesPackageVersionInfo
from embyapi.models.user_dto import UserDto
from embyapi.models.user_item_data_dto import UserItemDataDto
from embyapi.models.user_library_add_tags import UserLibraryAddTags
from embyapi.models.user_library_official_rating_item import UserLibraryOfficialRatingItem
from embyapi.models.user_library_tag_item import UserLibraryTagItem
from embyapi.models.users_forgot_password_action import UsersForgotPasswordAction
from embyapi.models.users_forgot_password_result import UsersForgotPasswordResult
from embyapi.models.users_pin_redeem_result import UsersPinRedeemResult
from embyapi.models.users_user_action import UsersUserAction
from embyapi.models.users_user_action_type import UsersUserActionType
from embyapi.models.users_user_policy import UsersUserPolicy
from embyapi.models.validate_path import ValidatePath
from embyapi.models.version import Version
from embyapi.models.video3_d_format import Video3DFormat
from embyapi.models.virtual_folder_info import VirtualFolderInfo
from embyapi.models.wake_on_lan_info import WakeOnLanInfo
