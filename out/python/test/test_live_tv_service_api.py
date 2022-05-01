# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import embyapi
from embyapi.api.live_tv_service_api import LiveTvServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestLiveTvServiceApi(unittest.TestCase):
    """LiveTvServiceApi unit test stubs"""

    def setUp(self):
        self.api = LiveTvServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_livetv_channelmappingoptions(self):
        """Test case for delete_livetv_channelmappingoptions

        """
        pass

    def test_delete_livetv_channelmappings(self):
        """Test case for delete_livetv_channelmappings

        """
        pass

    def test_delete_livetv_listingproviders(self):
        """Test case for delete_livetv_listingproviders

        Deletes a listing provider  # noqa: E501
        """
        pass

    def test_delete_livetv_recordings_by_id(self):
        """Test case for delete_livetv_recordings_by_id

        Deletes a live tv recording  # noqa: E501
        """
        pass

    def test_delete_livetv_seriestimers_by_id(self):
        """Test case for delete_livetv_seriestimers_by_id

        Cancels a live tv series timer  # noqa: E501
        """
        pass

    def test_delete_livetv_timers_by_id(self):
        """Test case for delete_livetv_timers_by_id

        Cancels a live tv timer  # noqa: E501
        """
        pass

    def test_delete_livetv_tunerhosts(self):
        """Test case for delete_livetv_tunerhosts

        Deletes a tuner host  # noqa: E501
        """
        pass

    def test_get_livetv_channelmappingoptions(self):
        """Test case for get_livetv_channelmappingoptions

        """
        pass

    def test_get_livetv_channelmappings(self):
        """Test case for get_livetv_channelmappings

        """
        pass

    def test_get_livetv_channels(self):
        """Test case for get_livetv_channels

        Gets available live tv channels.  # noqa: E501
        """
        pass

    def test_get_livetv_channels_by_id(self):
        """Test case for get_livetv_channels_by_id

        Gets a live tv channel  # noqa: E501
        """
        pass

    def test_get_livetv_guideinfo(self):
        """Test case for get_livetv_guideinfo

        Gets guide info  # noqa: E501
        """
        pass

    def test_get_livetv_info(self):
        """Test case for get_livetv_info

        Gets available live tv services.  # noqa: E501
        """
        pass

    def test_get_livetv_listingproviders(self):
        """Test case for get_livetv_listingproviders

        Gets current listing providers  # noqa: E501
        """
        pass

    def test_get_livetv_listingproviders_available(self):
        """Test case for get_livetv_listingproviders_available

        Gets listing provider  # noqa: E501
        """
        pass

    def test_get_livetv_listingproviders_default(self):
        """Test case for get_livetv_listingproviders_default

        """
        pass

    def test_get_livetv_listingproviders_lineups(self):
        """Test case for get_livetv_listingproviders_lineups

        Gets available lineups  # noqa: E501
        """
        pass

    def test_get_livetv_listingproviders_schedulesdirect_countries(self):
        """Test case for get_livetv_listingproviders_schedulesdirect_countries

        Gets available lineups  # noqa: E501
        """
        pass

    def test_get_livetv_liverecordings_by_id_stream(self):
        """Test case for get_livetv_liverecordings_by_id_stream

        Gets a live tv channel  # noqa: E501
        """
        pass

    def test_get_livetv_livestreamfiles_by_id_by_container(self):
        """Test case for get_livetv_livestreamfiles_by_id_by_container

        Gets a live tv channel  # noqa: E501
        """
        pass

    def test_get_livetv_programs(self):
        """Test case for get_livetv_programs

        Gets available live tv epgs..  # noqa: E501
        """
        pass

    def test_get_livetv_programs_recommended(self):
        """Test case for get_livetv_programs_recommended

        Gets available live tv epgs..  # noqa: E501
        """
        pass

    def test_get_livetv_recordings(self):
        """Test case for get_livetv_recordings

        Gets live tv recordings  # noqa: E501
        """
        pass

    def test_get_livetv_recordings_by_id(self):
        """Test case for get_livetv_recordings_by_id

        Gets a live tv recording  # noqa: E501
        """
        pass

    def test_get_livetv_recordings_folders(self):
        """Test case for get_livetv_recordings_folders

        Gets recording folders  # noqa: E501
        """
        pass

    def test_get_livetv_recordings_groups(self):
        """Test case for get_livetv_recordings_groups

        Gets live tv recording groups  # noqa: E501
        """
        pass

    def test_get_livetv_recordings_groups_by_id(self):
        """Test case for get_livetv_recordings_groups_by_id

        Gets a recording group  # noqa: E501
        """
        pass

    def test_get_livetv_recordings_series(self):
        """Test case for get_livetv_recordings_series

        Gets live tv recordings  # noqa: E501
        """
        pass

    def test_get_livetv_seriestimers(self):
        """Test case for get_livetv_seriestimers

        Gets live tv series timers  # noqa: E501
        """
        pass

    def test_get_livetv_seriestimers_by_id(self):
        """Test case for get_livetv_seriestimers_by_id

        Gets a live tv series timer  # noqa: E501
        """
        pass

    def test_get_livetv_timers(self):
        """Test case for get_livetv_timers

        Gets live tv timers  # noqa: E501
        """
        pass

    def test_get_livetv_timers_by_id(self):
        """Test case for get_livetv_timers_by_id

        Gets a live tv timer  # noqa: E501
        """
        pass

    def test_get_livetv_timers_defaults(self):
        """Test case for get_livetv_timers_defaults

        Gets default values for a new timer  # noqa: E501
        """
        pass

    def test_get_livetv_tunerhosts(self):
        """Test case for get_livetv_tunerhosts

        Gets tuner hosts  # noqa: E501
        """
        pass

    def test_get_livetv_tunerhosts_types(self):
        """Test case for get_livetv_tunerhosts_types

        """
        pass

    def test_get_livetv_tuners_discvover(self):
        """Test case for get_livetv_tuners_discvover

        """
        pass

    def test_head_livetv_channelmappingoptions(self):
        """Test case for head_livetv_channelmappingoptions

        """
        pass

    def test_head_livetv_channelmappings(self):
        """Test case for head_livetv_channelmappings

        """
        pass

    def test_options_livetv_channelmappingoptions(self):
        """Test case for options_livetv_channelmappingoptions

        """
        pass

    def test_options_livetv_channelmappings(self):
        """Test case for options_livetv_channelmappings

        """
        pass

    def test_patch_livetv_channelmappingoptions(self):
        """Test case for patch_livetv_channelmappingoptions

        """
        pass

    def test_patch_livetv_channelmappings(self):
        """Test case for patch_livetv_channelmappings

        """
        pass

    def test_post_livetv_channelmappingoptions(self):
        """Test case for post_livetv_channelmappingoptions

        """
        pass

    def test_post_livetv_channelmappings(self):
        """Test case for post_livetv_channelmappings

        """
        pass

    def test_post_livetv_listingproviders(self):
        """Test case for post_livetv_listingproviders

        Adds a listing provider  # noqa: E501
        """
        pass

    def test_post_livetv_programs(self):
        """Test case for post_livetv_programs

        Gets available live tv epgs..  # noqa: E501
        """
        pass

    def test_post_livetv_seriestimers(self):
        """Test case for post_livetv_seriestimers

        Creates a live tv series timer  # noqa: E501
        """
        pass

    def test_post_livetv_seriestimers_by_id(self):
        """Test case for post_livetv_seriestimers_by_id

        Updates a live tv series timer  # noqa: E501
        """
        pass

    def test_post_livetv_timers(self):
        """Test case for post_livetv_timers

        Creates a live tv timer  # noqa: E501
        """
        pass

    def test_post_livetv_timers_by_id(self):
        """Test case for post_livetv_timers_by_id

        Updates a live tv timer  # noqa: E501
        """
        pass

    def test_post_livetv_tunerhosts(self):
        """Test case for post_livetv_tunerhosts

        Adds a tuner host  # noqa: E501
        """
        pass

    def test_post_livetv_tuners_by_id_reset(self):
        """Test case for post_livetv_tuners_by_id_reset

        Resets a tv tuner  # noqa: E501
        """
        pass

    def test_put_livetv_channelmappingoptions(self):
        """Test case for put_livetv_channelmappingoptions

        """
        pass

    def test_put_livetv_channelmappings(self):
        """Test case for put_livetv_channelmappings

        """
        pass


if __name__ == '__main__':
    unittest.main()