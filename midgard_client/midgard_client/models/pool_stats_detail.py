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

class PoolStatsDetail(object):
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
        'add_asset_liquidity_volume': 'str',
        'add_liquidity_count': 'str',
        'add_liquidity_volume': 'str',
        'add_rune_liquidity_volume': 'str',
        'asset': 'str',
        'asset_depth': 'str',
        'asset_price': 'str',
        'asset_price_usd': 'str',
        'average_slip': 'str',
        'impermanent_loss_protection_paid': 'str',
        'liquidity_units': 'str',
        'pool_apy': 'str',
        'rune_depth': 'str',
        'status': 'str',
        'swap_count': 'str',
        'swap_volume': 'str',
        'synth_supply': 'str',
        'synth_units': 'str',
        'to_asset_average_slip': 'str',
        'to_asset_count': 'str',
        'to_asset_fees': 'str',
        'to_asset_volume': 'str',
        'to_rune_average_slip': 'str',
        'to_rune_count': 'str',
        'to_rune_fees': 'str',
        'to_rune_volume': 'str',
        'total_fees': 'str',
        'unique_member_count': 'str',
        'unique_swapper_count': 'str',
        'units': 'str',
        'withdraw_asset_volume': 'str',
        'withdraw_count': 'str',
        'withdraw_rune_volume': 'str',
        'withdraw_volume': 'str'
    }

    attribute_map = {
        'add_asset_liquidity_volume': 'addAssetLiquidityVolume',
        'add_liquidity_count': 'addLiquidityCount',
        'add_liquidity_volume': 'addLiquidityVolume',
        'add_rune_liquidity_volume': 'addRuneLiquidityVolume',
        'asset': 'asset',
        'asset_depth': 'assetDepth',
        'asset_price': 'assetPrice',
        'asset_price_usd': 'assetPriceUSD',
        'average_slip': 'averageSlip',
        'impermanent_loss_protection_paid': 'impermanentLossProtectionPaid',
        'liquidity_units': 'liquidityUnits',
        'pool_apy': 'poolAPY',
        'rune_depth': 'runeDepth',
        'status': 'status',
        'swap_count': 'swapCount',
        'swap_volume': 'swapVolume',
        'synth_supply': 'synthSupply',
        'synth_units': 'synthUnits',
        'to_asset_average_slip': 'toAssetAverageSlip',
        'to_asset_count': 'toAssetCount',
        'to_asset_fees': 'toAssetFees',
        'to_asset_volume': 'toAssetVolume',
        'to_rune_average_slip': 'toRuneAverageSlip',
        'to_rune_count': 'toRuneCount',
        'to_rune_fees': 'toRuneFees',
        'to_rune_volume': 'toRuneVolume',
        'total_fees': 'totalFees',
        'unique_member_count': 'uniqueMemberCount',
        'unique_swapper_count': 'uniqueSwapperCount',
        'units': 'units',
        'withdraw_asset_volume': 'withdrawAssetVolume',
        'withdraw_count': 'withdrawCount',
        'withdraw_rune_volume': 'withdrawRuneVolume',
        'withdraw_volume': 'withdrawVolume'
    }

    def __init__(self, add_asset_liquidity_volume=None, add_liquidity_count=None, add_liquidity_volume=None, add_rune_liquidity_volume=None, asset=None, asset_depth=None, asset_price=None, asset_price_usd=None, average_slip=None, impermanent_loss_protection_paid=None, liquidity_units=None, pool_apy=None, rune_depth=None, status=None, swap_count=None, swap_volume=None, synth_supply=None, synth_units=None, to_asset_average_slip=None, to_asset_count=None, to_asset_fees=None, to_asset_volume=None, to_rune_average_slip=None, to_rune_count=None, to_rune_fees=None, to_rune_volume=None, total_fees=None, unique_member_count=None, unique_swapper_count=None, units=None, withdraw_asset_volume=None, withdraw_count=None, withdraw_rune_volume=None, withdraw_volume=None):  # noqa: E501
        """PoolStatsDetail - a model defined in Swagger"""  # noqa: E501
        self._add_asset_liquidity_volume = None
        self._add_liquidity_count = None
        self._add_liquidity_volume = None
        self._add_rune_liquidity_volume = None
        self._asset = None
        self._asset_depth = None
        self._asset_price = None
        self._asset_price_usd = None
        self._average_slip = None
        self._impermanent_loss_protection_paid = None
        self._liquidity_units = None
        self._pool_apy = None
        self._rune_depth = None
        self._status = None
        self._swap_count = None
        self._swap_volume = None
        self._synth_supply = None
        self._synth_units = None
        self._to_asset_average_slip = None
        self._to_asset_count = None
        self._to_asset_fees = None
        self._to_asset_volume = None
        self._to_rune_average_slip = None
        self._to_rune_count = None
        self._to_rune_fees = None
        self._to_rune_volume = None
        self._total_fees = None
        self._unique_member_count = None
        self._unique_swapper_count = None
        self._units = None
        self._withdraw_asset_volume = None
        self._withdraw_count = None
        self._withdraw_rune_volume = None
        self._withdraw_volume = None
        self.discriminator = None
        self.add_asset_liquidity_volume = add_asset_liquidity_volume
        self.add_liquidity_count = add_liquidity_count
        self.add_liquidity_volume = add_liquidity_volume
        self.add_rune_liquidity_volume = add_rune_liquidity_volume
        self.asset = asset
        self.asset_depth = asset_depth
        self.asset_price = asset_price
        self.asset_price_usd = asset_price_usd
        self.average_slip = average_slip
        self.impermanent_loss_protection_paid = impermanent_loss_protection_paid
        self.liquidity_units = liquidity_units
        self.pool_apy = pool_apy
        self.rune_depth = rune_depth
        self.status = status
        self.swap_count = swap_count
        self.swap_volume = swap_volume
        self.synth_supply = synth_supply
        self.synth_units = synth_units
        self.to_asset_average_slip = to_asset_average_slip
        self.to_asset_count = to_asset_count
        self.to_asset_fees = to_asset_fees
        self.to_asset_volume = to_asset_volume
        self.to_rune_average_slip = to_rune_average_slip
        self.to_rune_count = to_rune_count
        self.to_rune_fees = to_rune_fees
        self.to_rune_volume = to_rune_volume
        self.total_fees = total_fees
        self.unique_member_count = unique_member_count
        self.unique_swapper_count = unique_swapper_count
        self.units = units
        self.withdraw_asset_volume = withdraw_asset_volume
        self.withdraw_count = withdraw_count
        self.withdraw_rune_volume = withdraw_rune_volume
        self.withdraw_volume = withdraw_volume

    @property
    def add_asset_liquidity_volume(self):
        """Gets the add_asset_liquidity_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:addAssetLiquidityVolume  # noqa: E501

        :return: The add_asset_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._add_asset_liquidity_volume

    @add_asset_liquidity_volume.setter
    def add_asset_liquidity_volume(self, add_asset_liquidity_volume):
        """Sets the add_asset_liquidity_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:addAssetLiquidityVolume  # noqa: E501

        :param add_asset_liquidity_volume: The add_asset_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if add_asset_liquidity_volume is None:
            raise ValueError("Invalid value for `add_asset_liquidity_volume`, must not be `None`")  # noqa: E501

        self._add_asset_liquidity_volume = add_asset_liquidity_volume

    @property
    def add_liquidity_count(self):
        """Gets the add_liquidity_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as history/liquidity_changes:addLiquidityCount  # noqa: E501

        :return: The add_liquidity_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._add_liquidity_count

    @add_liquidity_count.setter
    def add_liquidity_count(self, add_liquidity_count):
        """Sets the add_liquidity_count of this PoolStatsDetail.

        Int64, same as history/liquidity_changes:addLiquidityCount  # noqa: E501

        :param add_liquidity_count: The add_liquidity_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if add_liquidity_count is None:
            raise ValueError("Invalid value for `add_liquidity_count`, must not be `None`")  # noqa: E501

        self._add_liquidity_count = add_liquidity_count

    @property
    def add_liquidity_volume(self):
        """Gets the add_liquidity_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:addLiquidityVolume  # noqa: E501

        :return: The add_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._add_liquidity_volume

    @add_liquidity_volume.setter
    def add_liquidity_volume(self, add_liquidity_volume):
        """Sets the add_liquidity_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:addLiquidityVolume  # noqa: E501

        :param add_liquidity_volume: The add_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if add_liquidity_volume is None:
            raise ValueError("Invalid value for `add_liquidity_volume`, must not be `None`")  # noqa: E501

        self._add_liquidity_volume = add_liquidity_volume

    @property
    def add_rune_liquidity_volume(self):
        """Gets the add_rune_liquidity_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:addRuneLiquidityVolume  # noqa: E501

        :return: The add_rune_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._add_rune_liquidity_volume

    @add_rune_liquidity_volume.setter
    def add_rune_liquidity_volume(self, add_rune_liquidity_volume):
        """Sets the add_rune_liquidity_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:addRuneLiquidityVolume  # noqa: E501

        :param add_rune_liquidity_volume: The add_rune_liquidity_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if add_rune_liquidity_volume is None:
            raise ValueError("Invalid value for `add_rune_liquidity_volume`, must not be `None`")  # noqa: E501

        self._add_rune_liquidity_volume = add_rune_liquidity_volume

    @property
    def asset(self):
        """Gets the asset of this PoolStatsDetail.  # noqa: E501


        :return: The asset of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this PoolStatsDetail.


        :param asset: The asset of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def asset_depth(self):
        """Gets the asset_depth of this PoolStatsDetail.  # noqa: E501

        Int64(e8), the amount of Asset in the pool  # noqa: E501

        :return: The asset_depth of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset_depth

    @asset_depth.setter
    def asset_depth(self, asset_depth):
        """Sets the asset_depth of this PoolStatsDetail.

        Int64(e8), the amount of Asset in the pool  # noqa: E501

        :param asset_depth: The asset_depth of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if asset_depth is None:
            raise ValueError("Invalid value for `asset_depth`, must not be `None`")  # noqa: E501

        self._asset_depth = asset_depth

    @property
    def asset_price(self):
        """Gets the asset_price of this PoolStatsDetail.  # noqa: E501

        Float, price of asset in rune. I.e. rune amount / asset amount  # noqa: E501

        :return: The asset_price of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset_price

    @asset_price.setter
    def asset_price(self, asset_price):
        """Sets the asset_price of this PoolStatsDetail.

        Float, price of asset in rune. I.e. rune amount / asset amount  # noqa: E501

        :param asset_price: The asset_price of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if asset_price is None:
            raise ValueError("Invalid value for `asset_price`, must not be `None`")  # noqa: E501

        self._asset_price = asset_price

    @property
    def asset_price_usd(self):
        """Gets the asset_price_usd of this PoolStatsDetail.  # noqa: E501

        Float, the price of asset in USD (based on the deepest USD pool).  # noqa: E501

        :return: The asset_price_usd of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset_price_usd

    @asset_price_usd.setter
    def asset_price_usd(self, asset_price_usd):
        """Sets the asset_price_usd of this PoolStatsDetail.

        Float, the price of asset in USD (based on the deepest USD pool).  # noqa: E501

        :param asset_price_usd: The asset_price_usd of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if asset_price_usd is None:
            raise ValueError("Invalid value for `asset_price_usd`, must not be `None`")  # noqa: E501

        self._asset_price_usd = asset_price_usd

    @property
    def average_slip(self):
        """Gets the average_slip of this PoolStatsDetail.  # noqa: E501

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:averageSlip  # noqa: E501

        :return: The average_slip of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._average_slip

    @average_slip.setter
    def average_slip(self, average_slip):
        """Sets the average_slip of this PoolStatsDetail.

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:averageSlip  # noqa: E501

        :param average_slip: The average_slip of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if average_slip is None:
            raise ValueError("Invalid value for `average_slip`, must not be `None`")  # noqa: E501

        self._average_slip = average_slip

    @property
    def impermanent_loss_protection_paid(self):
        """Gets the impermanent_loss_protection_paid of this PoolStatsDetail.  # noqa: E501

        Int64(e8), part of the withdrawRuneVolume which was payed because of impermanent loss protection.   # noqa: E501

        :return: The impermanent_loss_protection_paid of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._impermanent_loss_protection_paid

    @impermanent_loss_protection_paid.setter
    def impermanent_loss_protection_paid(self, impermanent_loss_protection_paid):
        """Sets the impermanent_loss_protection_paid of this PoolStatsDetail.

        Int64(e8), part of the withdrawRuneVolume which was payed because of impermanent loss protection.   # noqa: E501

        :param impermanent_loss_protection_paid: The impermanent_loss_protection_paid of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if impermanent_loss_protection_paid is None:
            raise ValueError("Invalid value for `impermanent_loss_protection_paid`, must not be `None`")  # noqa: E501

        self._impermanent_loss_protection_paid = impermanent_loss_protection_paid

    @property
    def liquidity_units(self):
        """Gets the liquidity_units of this PoolStatsDetail.  # noqa: E501

        Int64, Liquidity Units in the pool  # noqa: E501

        :return: The liquidity_units of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._liquidity_units

    @liquidity_units.setter
    def liquidity_units(self, liquidity_units):
        """Sets the liquidity_units of this PoolStatsDetail.

        Int64, Liquidity Units in the pool  # noqa: E501

        :param liquidity_units: The liquidity_units of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if liquidity_units is None:
            raise ValueError("Invalid value for `liquidity_units`, must not be `None`")  # noqa: E501

        self._liquidity_units = liquidity_units

    @property
    def pool_apy(self):
        """Gets the pool_apy of this PoolStatsDetail.  # noqa: E501

        Float, Average Percentage Yield: annual return estimated using last weeks income, taking compound interest into account.  # noqa: E501

        :return: The pool_apy of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_apy

    @pool_apy.setter
    def pool_apy(self, pool_apy):
        """Sets the pool_apy of this PoolStatsDetail.

        Float, Average Percentage Yield: annual return estimated using last weeks income, taking compound interest into account.  # noqa: E501

        :param pool_apy: The pool_apy of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if pool_apy is None:
            raise ValueError("Invalid value for `pool_apy`, must not be `None`")  # noqa: E501

        self._pool_apy = pool_apy

    @property
    def rune_depth(self):
        """Gets the rune_depth of this PoolStatsDetail.  # noqa: E501

        Int64(e8), the amount of Rune in the pool  # noqa: E501

        :return: The rune_depth of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._rune_depth

    @rune_depth.setter
    def rune_depth(self, rune_depth):
        """Sets the rune_depth of this PoolStatsDetail.

        Int64(e8), the amount of Rune in the pool  # noqa: E501

        :param rune_depth: The rune_depth of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if rune_depth is None:
            raise ValueError("Invalid value for `rune_depth`, must not be `None`")  # noqa: E501

        self._rune_depth = rune_depth

    @property
    def status(self):
        """Gets the status of this PoolStatsDetail.  # noqa: E501

        The state of the pool, e.g. Available, Staged  # noqa: E501

        :return: The status of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PoolStatsDetail.

        The state of the pool, e.g. Available, Staged  # noqa: E501

        :param status: The status of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def swap_count(self):
        """Gets the swap_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as history/swaps:totalCount  # noqa: E501

        :return: The swap_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._swap_count

    @swap_count.setter
    def swap_count(self, swap_count):
        """Sets the swap_count of this PoolStatsDetail.

        Int64, same as history/swaps:totalCount  # noqa: E501

        :param swap_count: The swap_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if swap_count is None:
            raise ValueError("Invalid value for `swap_count`, must not be `None`")  # noqa: E501

        self._swap_count = swap_count

    @property
    def swap_volume(self):
        """Gets the swap_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:totalVolume  # noqa: E501

        :return: The swap_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._swap_volume

    @swap_volume.setter
    def swap_volume(self, swap_volume):
        """Sets the swap_volume of this PoolStatsDetail.

        Int64(e8), same as history/swaps:totalVolume  # noqa: E501

        :param swap_volume: The swap_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if swap_volume is None:
            raise ValueError("Invalid value for `swap_volume`, must not be `None`")  # noqa: E501

        self._swap_volume = swap_volume

    @property
    def synth_supply(self):
        """Gets the synth_supply of this PoolStatsDetail.  # noqa: E501

        Int64, Synth supply in the pool  # noqa: E501

        :return: The synth_supply of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._synth_supply

    @synth_supply.setter
    def synth_supply(self, synth_supply):
        """Sets the synth_supply of this PoolStatsDetail.

        Int64, Synth supply in the pool  # noqa: E501

        :param synth_supply: The synth_supply of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if synth_supply is None:
            raise ValueError("Invalid value for `synth_supply`, must not be `None`")  # noqa: E501

        self._synth_supply = synth_supply

    @property
    def synth_units(self):
        """Gets the synth_units of this PoolStatsDetail.  # noqa: E501

        Int64, Synth Units in the pool  # noqa: E501

        :return: The synth_units of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._synth_units

    @synth_units.setter
    def synth_units(self, synth_units):
        """Sets the synth_units of this PoolStatsDetail.

        Int64, Synth Units in the pool  # noqa: E501

        :param synth_units: The synth_units of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if synth_units is None:
            raise ValueError("Invalid value for `synth_units`, must not be `None`")  # noqa: E501

        self._synth_units = synth_units

    @property
    def to_asset_average_slip(self):
        """Gets the to_asset_average_slip of this PoolStatsDetail.  # noqa: E501

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:toAssetAverageSlip  # noqa: E501

        :return: The to_asset_average_slip of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_average_slip

    @to_asset_average_slip.setter
    def to_asset_average_slip(self, to_asset_average_slip):
        """Sets the to_asset_average_slip of this PoolStatsDetail.

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:toAssetAverageSlip  # noqa: E501

        :param to_asset_average_slip: The to_asset_average_slip of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_asset_average_slip is None:
            raise ValueError("Invalid value for `to_asset_average_slip`, must not be `None`")  # noqa: E501

        self._to_asset_average_slip = to_asset_average_slip

    @property
    def to_asset_count(self):
        """Gets the to_asset_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as history/swaps:toAssetCount  # noqa: E501

        :return: The to_asset_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_count

    @to_asset_count.setter
    def to_asset_count(self, to_asset_count):
        """Sets the to_asset_count of this PoolStatsDetail.

        Int64, same as history/swaps:toAssetCount  # noqa: E501

        :param to_asset_count: The to_asset_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_asset_count is None:
            raise ValueError("Invalid value for `to_asset_count`, must not be `None`")  # noqa: E501

        self._to_asset_count = to_asset_count

    @property
    def to_asset_fees(self):
        """Gets the to_asset_fees of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:toAssetFees  # noqa: E501

        :return: The to_asset_fees of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_fees

    @to_asset_fees.setter
    def to_asset_fees(self, to_asset_fees):
        """Sets the to_asset_fees of this PoolStatsDetail.

        Int64(e8), same as history/swaps:toAssetFees  # noqa: E501

        :param to_asset_fees: The to_asset_fees of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_asset_fees is None:
            raise ValueError("Invalid value for `to_asset_fees`, must not be `None`")  # noqa: E501

        self._to_asset_fees = to_asset_fees

    @property
    def to_asset_volume(self):
        """Gets the to_asset_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:toAssetVolume  # noqa: E501

        :return: The to_asset_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_volume

    @to_asset_volume.setter
    def to_asset_volume(self, to_asset_volume):
        """Sets the to_asset_volume of this PoolStatsDetail.

        Int64(e8), same as history/swaps:toAssetVolume  # noqa: E501

        :param to_asset_volume: The to_asset_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_asset_volume is None:
            raise ValueError("Invalid value for `to_asset_volume`, must not be `None`")  # noqa: E501

        self._to_asset_volume = to_asset_volume

    @property
    def to_rune_average_slip(self):
        """Gets the to_rune_average_slip of this PoolStatsDetail.  # noqa: E501

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:toRuneAverageSlip  # noqa: E501

        :return: The to_rune_average_slip of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_rune_average_slip

    @to_rune_average_slip.setter
    def to_rune_average_slip(self, to_rune_average_slip):
        """Sets the to_rune_average_slip of this PoolStatsDetail.

        Float64 (Basis points, 0-10000, where 10000=100%), same as history/swaps:toRuneAverageSlip  # noqa: E501

        :param to_rune_average_slip: The to_rune_average_slip of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_rune_average_slip is None:
            raise ValueError("Invalid value for `to_rune_average_slip`, must not be `None`")  # noqa: E501

        self._to_rune_average_slip = to_rune_average_slip

    @property
    def to_rune_count(self):
        """Gets the to_rune_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as history/swaps:toRuneCount  # noqa: E501

        :return: The to_rune_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_rune_count

    @to_rune_count.setter
    def to_rune_count(self, to_rune_count):
        """Sets the to_rune_count of this PoolStatsDetail.

        Int64, same as history/swaps:toRuneCount  # noqa: E501

        :param to_rune_count: The to_rune_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_rune_count is None:
            raise ValueError("Invalid value for `to_rune_count`, must not be `None`")  # noqa: E501

        self._to_rune_count = to_rune_count

    @property
    def to_rune_fees(self):
        """Gets the to_rune_fees of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:toRuneFees  # noqa: E501

        :return: The to_rune_fees of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_rune_fees

    @to_rune_fees.setter
    def to_rune_fees(self, to_rune_fees):
        """Sets the to_rune_fees of this PoolStatsDetail.

        Int64(e8), same as history/swaps:toRuneFees  # noqa: E501

        :param to_rune_fees: The to_rune_fees of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_rune_fees is None:
            raise ValueError("Invalid value for `to_rune_fees`, must not be `None`")  # noqa: E501

        self._to_rune_fees = to_rune_fees

    @property
    def to_rune_volume(self):
        """Gets the to_rune_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:toRuneVolume  # noqa: E501

        :return: The to_rune_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._to_rune_volume

    @to_rune_volume.setter
    def to_rune_volume(self, to_rune_volume):
        """Sets the to_rune_volume of this PoolStatsDetail.

        Int64(e8), same as history/swaps:toRuneVolume  # noqa: E501

        :param to_rune_volume: The to_rune_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if to_rune_volume is None:
            raise ValueError("Invalid value for `to_rune_volume`, must not be `None`")  # noqa: E501

        self._to_rune_volume = to_rune_volume

    @property
    def total_fees(self):
        """Gets the total_fees of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/swaps:totalFees  # noqa: E501

        :return: The total_fees of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._total_fees

    @total_fees.setter
    def total_fees(self, total_fees):
        """Sets the total_fees of this PoolStatsDetail.

        Int64(e8), same as history/swaps:totalFees  # noqa: E501

        :param total_fees: The total_fees of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if total_fees is None:
            raise ValueError("Invalid value for `total_fees`, must not be `None`")  # noqa: E501

        self._total_fees = total_fees

    @property
    def unique_member_count(self):
        """Gets the unique_member_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as len(history/members?pool=POOL)  # noqa: E501

        :return: The unique_member_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._unique_member_count

    @unique_member_count.setter
    def unique_member_count(self, unique_member_count):
        """Sets the unique_member_count of this PoolStatsDetail.

        Int64, same as len(history/members?pool=POOL)  # noqa: E501

        :param unique_member_count: The unique_member_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if unique_member_count is None:
            raise ValueError("Invalid value for `unique_member_count`, must not be `None`")  # noqa: E501

        self._unique_member_count = unique_member_count

    @property
    def unique_swapper_count(self):
        """Gets the unique_swapper_count of this PoolStatsDetail.  # noqa: E501

        Int64, number of unique adresses that initiated swaps transactions in the period.   # noqa: E501

        :return: The unique_swapper_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._unique_swapper_count

    @unique_swapper_count.setter
    def unique_swapper_count(self, unique_swapper_count):
        """Sets the unique_swapper_count of this PoolStatsDetail.

        Int64, number of unique adresses that initiated swaps transactions in the period.   # noqa: E501

        :param unique_swapper_count: The unique_swapper_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if unique_swapper_count is None:
            raise ValueError("Invalid value for `unique_swapper_count`, must not be `None`")  # noqa: E501

        self._unique_swapper_count = unique_swapper_count

    @property
    def units(self):
        """Gets the units of this PoolStatsDetail.  # noqa: E501

        Int64, Total Units (synthUnits + liquidityUnits) in the pool  # noqa: E501

        :return: The units of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this PoolStatsDetail.

        Int64, Total Units (synthUnits + liquidityUnits) in the pool  # noqa: E501

        :param units: The units of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def withdraw_asset_volume(self):
        """Gets the withdraw_asset_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:withdrawAssetVolume  # noqa: E501

        :return: The withdraw_asset_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_asset_volume

    @withdraw_asset_volume.setter
    def withdraw_asset_volume(self, withdraw_asset_volume):
        """Sets the withdraw_asset_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:withdrawAssetVolume  # noqa: E501

        :param withdraw_asset_volume: The withdraw_asset_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if withdraw_asset_volume is None:
            raise ValueError("Invalid value for `withdraw_asset_volume`, must not be `None`")  # noqa: E501

        self._withdraw_asset_volume = withdraw_asset_volume

    @property
    def withdraw_count(self):
        """Gets the withdraw_count of this PoolStatsDetail.  # noqa: E501

        Int64, same as history/liquidity_changes:withdrawCount  # noqa: E501

        :return: The withdraw_count of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_count

    @withdraw_count.setter
    def withdraw_count(self, withdraw_count):
        """Sets the withdraw_count of this PoolStatsDetail.

        Int64, same as history/liquidity_changes:withdrawCount  # noqa: E501

        :param withdraw_count: The withdraw_count of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if withdraw_count is None:
            raise ValueError("Invalid value for `withdraw_count`, must not be `None`")  # noqa: E501

        self._withdraw_count = withdraw_count

    @property
    def withdraw_rune_volume(self):
        """Gets the withdraw_rune_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:withdrawRuneVolume  # noqa: E501

        :return: The withdraw_rune_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_rune_volume

    @withdraw_rune_volume.setter
    def withdraw_rune_volume(self, withdraw_rune_volume):
        """Sets the withdraw_rune_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:withdrawRuneVolume  # noqa: E501

        :param withdraw_rune_volume: The withdraw_rune_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if withdraw_rune_volume is None:
            raise ValueError("Invalid value for `withdraw_rune_volume`, must not be `None`")  # noqa: E501

        self._withdraw_rune_volume = withdraw_rune_volume

    @property
    def withdraw_volume(self):
        """Gets the withdraw_volume of this PoolStatsDetail.  # noqa: E501

        Int64(e8), same as history/liquidity_changes:withdrawVolume  # noqa: E501

        :return: The withdraw_volume of this PoolStatsDetail.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_volume

    @withdraw_volume.setter
    def withdraw_volume(self, withdraw_volume):
        """Sets the withdraw_volume of this PoolStatsDetail.

        Int64(e8), same as history/liquidity_changes:withdrawVolume  # noqa: E501

        :param withdraw_volume: The withdraw_volume of this PoolStatsDetail.  # noqa: E501
        :type: str
        """
        if withdraw_volume is None:
            raise ValueError("Invalid value for `withdraw_volume`, must not be `None`")  # noqa: E501

        self._withdraw_volume = withdraw_volume

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
        if issubclass(PoolStatsDetail, dict):
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
        if not isinstance(other, PoolStatsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
