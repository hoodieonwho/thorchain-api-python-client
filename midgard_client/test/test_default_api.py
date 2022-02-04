# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.5.12
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import midgard_client
from midgard_client.api.default_api import DefaultApi  # noqa: E501
from midgard_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_actions(self):
        """Test case for get_actions

        Actions List  # noqa: E501
        """
        pass

    def test_get_depth_history(self):
        """Test case for get_depth_history

        Depth and Price History  # noqa: E501
        """
        pass

    def test_get_earnings_history(self):
        """Test case for get_earnings_history

        Earnings History  # noqa: E501
        """
        pass

    def test_get_health(self):
        """Test case for get_health

        Health Info  # noqa: E501
        """
        pass

    def test_get_liquidity_history(self):
        """Test case for get_liquidity_history

        Liquidity Changes History  # noqa: E501
        """
        pass

    def test_get_member_detail(self):
        """Test case for get_member_detail

        Member Details  # noqa: E501
        """
        pass

    def test_get_members_adresses(self):
        """Test case for get_members_adresses

        Members List  # noqa: E501
        """
        pass

    def test_get_network_data(self):
        """Test case for get_network_data

        Network Data  # noqa: E501
        """
        pass

    def test_get_nodes(self):
        """Test case for get_nodes

        Nodes List  # noqa: E501
        """
        pass

    def test_get_pool(self):
        """Test case for get_pool

        Details of a Pool  # noqa: E501
        """
        pass

    def test_get_pool_stats(self):
        """Test case for get_pool_stats

        Pool Statistics  # noqa: E501
        """
        pass

    def test_get_pools(self):
        """Test case for get_pools

        Pools List  # noqa: E501
        """
        pass

    def test_get_proxied_constants(self):
        """Test case for get_proxied_constants

        Proxied THORChain Constants  # noqa: E501
        """
        pass

    def test_get_proxied_inbound_addresses(self):
        """Test case for get_proxied_inbound_addresses

        Proxied THORChain Inbound Addresses  # noqa: E501
        """
        pass

    def test_get_proxied_lastblock(self):
        """Test case for get_proxied_lastblock

        Proxied THORChain Lastblock  # noqa: E501
        """
        pass

    def test_get_proxied_nodes(self):
        """Test case for get_proxied_nodes

        Proxied THORChain Nodes  # noqa: E501
        """
        pass

    def test_get_proxied_queue(self):
        """Test case for get_proxied_queue

        Proxied THORChain Queue  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        Global Stats  # noqa: E501
        """
        pass

    def test_get_swap_history(self):
        """Test case for get_swap_history

        Swaps History  # noqa: E501
        """
        pass

    def test_get_thor_name_detail(self):
        """Test case for get_thor_name_detail

        THORName Details  # noqa: E501
        """
        pass

    def test_get_thor_names_by_address(self):
        """Test case for get_thor_names_by_address

        Gives a list of THORNames by reverse lookup  # noqa: E501
        """
        pass

    def test_get_tvl_history(self):
        """Test case for get_tvl_history

        Total Value Locked History  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
