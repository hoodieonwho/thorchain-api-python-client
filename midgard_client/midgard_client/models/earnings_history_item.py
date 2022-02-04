# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.5.12
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EarningsHistoryItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'avg_node_count': 'str',
        'block_rewards': 'str',
        'bonding_earnings': 'str',
        'earnings': 'str',
        'end_time': 'str',
        'liquidity_earnings': 'str',
        'liquidity_fees': 'str',
        'pools': 'list[EarningsHistoryItemPool]',
        'rune_price_usd': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'avg_node_count': 'avgNodeCount',
        'block_rewards': 'blockRewards',
        'bonding_earnings': 'bondingEarnings',
        'earnings': 'earnings',
        'end_time': 'endTime',
        'liquidity_earnings': 'liquidityEarnings',
        'liquidity_fees': 'liquidityFees',
        'pools': 'pools',
        'rune_price_usd': 'runePriceUSD',
        'start_time': 'startTime'
    }

    def __init__(self, avg_node_count=None, block_rewards=None, bonding_earnings=None, earnings=None, end_time=None, liquidity_earnings=None, liquidity_fees=None, pools=None, rune_price_usd=None, start_time=None):  # noqa: E501
        """EarningsHistoryItem - a model defined in Swagger"""  # noqa: E501
        self._avg_node_count = None
        self._block_rewards = None
        self._bonding_earnings = None
        self._earnings = None
        self._end_time = None
        self._liquidity_earnings = None
        self._liquidity_fees = None
        self._pools = None
        self._rune_price_usd = None
        self._start_time = None
        self.discriminator = None
        self.avg_node_count = avg_node_count
        self.block_rewards = block_rewards
        self.bonding_earnings = bonding_earnings
        self.earnings = earnings
        self.end_time = end_time
        self.liquidity_earnings = liquidity_earnings
        self.liquidity_fees = liquidity_fees
        self.pools = pools
        self.rune_price_usd = rune_price_usd
        self.start_time = start_time

    @property
    def avg_node_count(self):
        """Gets the avg_node_count of this EarningsHistoryItem.  # noqa: E501

        float64, Average amount of active nodes during the time interval  # noqa: E501

        :return: The avg_node_count of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._avg_node_count

    @avg_node_count.setter
    def avg_node_count(self, avg_node_count):
        """Sets the avg_node_count of this EarningsHistoryItem.

        float64, Average amount of active nodes during the time interval  # noqa: E501

        :param avg_node_count: The avg_node_count of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if avg_node_count is None:
            raise ValueError("Invalid value for `avg_node_count`, must not be `None`")  # noqa: E501

        self._avg_node_count = avg_node_count

    @property
    def block_rewards(self):
        """Gets the block_rewards of this EarningsHistoryItem.  # noqa: E501

        Int64(e8), Total block rewards emitted during the time interval  # noqa: E501

        :return: The block_rewards of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._block_rewards

    @block_rewards.setter
    def block_rewards(self, block_rewards):
        """Sets the block_rewards of this EarningsHistoryItem.

        Int64(e8), Total block rewards emitted during the time interval  # noqa: E501

        :param block_rewards: The block_rewards of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if block_rewards is None:
            raise ValueError("Invalid value for `block_rewards`, must not be `None`")  # noqa: E501

        self._block_rewards = block_rewards

    @property
    def bonding_earnings(self):
        """Gets the bonding_earnings of this EarningsHistoryItem.  # noqa: E501

        Int64(e8), Share of earnings sent to nodes during the time interval  # noqa: E501

        :return: The bonding_earnings of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._bonding_earnings

    @bonding_earnings.setter
    def bonding_earnings(self, bonding_earnings):
        """Sets the bonding_earnings of this EarningsHistoryItem.

        Int64(e8), Share of earnings sent to nodes during the time interval  # noqa: E501

        :param bonding_earnings: The bonding_earnings of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if bonding_earnings is None:
            raise ValueError("Invalid value for `bonding_earnings`, must not be `None`")  # noqa: E501

        self._bonding_earnings = bonding_earnings

    @property
    def earnings(self):
        """Gets the earnings of this EarningsHistoryItem.  # noqa: E501

        Int64(e8), System income generated during the time interval. It is the sum of liquidity fees and block rewards  # noqa: E501

        :return: The earnings of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._earnings

    @earnings.setter
    def earnings(self, earnings):
        """Sets the earnings of this EarningsHistoryItem.

        Int64(e8), System income generated during the time interval. It is the sum of liquidity fees and block rewards  # noqa: E501

        :param earnings: The earnings of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if earnings is None:
            raise ValueError("Invalid value for `earnings`, must not be `None`")  # noqa: E501

        self._earnings = earnings

    @property
    def end_time(self):
        """Gets the end_time of this EarningsHistoryItem.  # noqa: E501

        Int64, The end time of interval in unix timestamp  # noqa: E501

        :return: The end_time of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EarningsHistoryItem.

        Int64, The end time of interval in unix timestamp  # noqa: E501

        :param end_time: The end_time of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def liquidity_earnings(self):
        """Gets the liquidity_earnings of this EarningsHistoryItem.  # noqa: E501

        Int64(e8), Share of earnings sent to pools during the time interval  # noqa: E501

        :return: The liquidity_earnings of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._liquidity_earnings

    @liquidity_earnings.setter
    def liquidity_earnings(self, liquidity_earnings):
        """Sets the liquidity_earnings of this EarningsHistoryItem.

        Int64(e8), Share of earnings sent to pools during the time interval  # noqa: E501

        :param liquidity_earnings: The liquidity_earnings of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if liquidity_earnings is None:
            raise ValueError("Invalid value for `liquidity_earnings`, must not be `None`")  # noqa: E501

        self._liquidity_earnings = liquidity_earnings

    @property
    def liquidity_fees(self):
        """Gets the liquidity_fees of this EarningsHistoryItem.  # noqa: E501

        Int64(e8), Total liquidity fees, converted to RUNE, collected during the time interval  # noqa: E501

        :return: The liquidity_fees of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._liquidity_fees

    @liquidity_fees.setter
    def liquidity_fees(self, liquidity_fees):
        """Sets the liquidity_fees of this EarningsHistoryItem.

        Int64(e8), Total liquidity fees, converted to RUNE, collected during the time interval  # noqa: E501

        :param liquidity_fees: The liquidity_fees of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if liquidity_fees is None:
            raise ValueError("Invalid value for `liquidity_fees`, must not be `None`")  # noqa: E501

        self._liquidity_fees = liquidity_fees

    @property
    def pools(self):
        """Gets the pools of this EarningsHistoryItem.  # noqa: E501

        Earnings data for each pool for the time interval  # noqa: E501

        :return: The pools of this EarningsHistoryItem.  # noqa: E501
        :rtype: list[EarningsHistoryItemPool]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this EarningsHistoryItem.

        Earnings data for each pool for the time interval  # noqa: E501

        :param pools: The pools of this EarningsHistoryItem.  # noqa: E501
        :type: list[EarningsHistoryItemPool]
        """
        if pools is None:
            raise ValueError("Invalid value for `pools`, must not be `None`")  # noqa: E501

        self._pools = pools

    @property
    def rune_price_usd(self):
        """Gets the rune_price_usd of this EarningsHistoryItem.  # noqa: E501

        Float, the price of Rune based on the deepest USD pool at the end of the interval.   # noqa: E501

        :return: The rune_price_usd of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._rune_price_usd

    @rune_price_usd.setter
    def rune_price_usd(self, rune_price_usd):
        """Sets the rune_price_usd of this EarningsHistoryItem.

        Float, the price of Rune based on the deepest USD pool at the end of the interval.   # noqa: E501

        :param rune_price_usd: The rune_price_usd of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if rune_price_usd is None:
            raise ValueError("Invalid value for `rune_price_usd`, must not be `None`")  # noqa: E501

        self._rune_price_usd = rune_price_usd

    @property
    def start_time(self):
        """Gets the start_time of this EarningsHistoryItem.  # noqa: E501

        Int64, The beginning time of interval in unix timestamp  # noqa: E501

        :return: The start_time of this EarningsHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EarningsHistoryItem.

        Int64, The beginning time of interval in unix timestamp  # noqa: E501

        :param start_time: The start_time of this EarningsHistoryItem.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EarningsHistoryItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EarningsHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other