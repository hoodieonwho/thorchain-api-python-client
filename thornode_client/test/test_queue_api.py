# coding: utf-8

"""
    THORChain API

    This documentation outlines the API for THORChain.  NOTE: This document is a **work in progress**.  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thornode_client
from thornode_client.api.queue_api import QueueApi  # noqa: E501
from thornode_client.rest import ApiException


class TestQueueApi(unittest.TestCase):
    """QueueApi unit test stubs"""

    def setUp(self):
        self.api = thornode_client.api.queue_api.QueueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_outbound_queue(self):
        """Test case for get_outbound_queue

        Get outbound queue  # noqa: E501
        """
        pass

    def test_get_outbound_queue_detail(self):
        """Test case for get_outbound_queue_detail

        Get outbound queue detail  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()