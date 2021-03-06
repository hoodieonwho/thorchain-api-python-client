# coding: utf-8

"""
    THORChain API

    This documentation outlines the API for THORChain.  NOTE: This document is a **work in progress**.  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from thornode_client.configuration import Configuration


class ObservedTx(object):
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
        'id': 'str',
        'chain': 'str',
        'from_address': 'str',
        'to_address': 'str',
        'coins': 'list[object]',
        'gas': 'list[object]',
        'memo': 'str'
    }

    attribute_map = {
        'id': 'id',
        'chain': 'chain',
        'from_address': 'from_address',
        'to_address': 'to_address',
        'coins': 'coins',
        'gas': 'gas',
        'memo': 'memo'
    }

    def __init__(self, id=None, chain=None, from_address=None, to_address=None, coins=None, gas=None, memo=None, _configuration=None):  # noqa: E501
        """ObservedTx - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._chain = None
        self._from_address = None
        self._to_address = None
        self._coins = None
        self._gas = None
        self._memo = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if chain is not None:
            self.chain = chain
        if from_address is not None:
            self.from_address = from_address
        if to_address is not None:
            self.to_address = to_address
        if coins is not None:
            self.coins = coins
        if gas is not None:
            self.gas = gas
        if memo is not None:
            self.memo = memo

    @property
    def id(self):
        """Gets the id of this ObservedTx.  # noqa: E501

        transaction hash  # noqa: E501

        :return: The id of this ObservedTx.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObservedTx.

        transaction hash  # noqa: E501

        :param id: The id of this ObservedTx.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def chain(self):
        """Gets the chain of this ObservedTx.  # noqa: E501

        chain  # noqa: E501

        :return: The chain of this ObservedTx.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this ObservedTx.

        chain  # noqa: E501

        :param chain: The chain of this ObservedTx.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def from_address(self):
        """Gets the from_address of this ObservedTx.  # noqa: E501

        from address  # noqa: E501

        :return: The from_address of this ObservedTx.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this ObservedTx.

        from address  # noqa: E501

        :param from_address: The from_address of this ObservedTx.  # noqa: E501
        :type: str
        """

        self._from_address = from_address

    @property
    def to_address(self):
        """Gets the to_address of this ObservedTx.  # noqa: E501

        to address  # noqa: E501

        :return: The to_address of this ObservedTx.  # noqa: E501
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """Sets the to_address of this ObservedTx.

        to address  # noqa: E501

        :param to_address: The to_address of this ObservedTx.  # noqa: E501
        :type: str
        """

        self._to_address = to_address

    @property
    def coins(self):
        """Gets the coins of this ObservedTx.  # noqa: E501

        coins  # noqa: E501

        :return: The coins of this ObservedTx.  # noqa: E501
        :rtype: list[object]
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this ObservedTx.

        coins  # noqa: E501

        :param coins: The coins of this ObservedTx.  # noqa: E501
        :type: list[object]
        """

        self._coins = coins

    @property
    def gas(self):
        """Gets the gas of this ObservedTx.  # noqa: E501

        amount of gas paid by the tx  # noqa: E501

        :return: The gas of this ObservedTx.  # noqa: E501
        :rtype: list[object]
        """
        return self._gas

    @gas.setter
    def gas(self, gas):
        """Sets the gas of this ObservedTx.

        amount of gas paid by the tx  # noqa: E501

        :param gas: The gas of this ObservedTx.  # noqa: E501
        :type: list[object]
        """

        self._gas = gas

    @property
    def memo(self):
        """Gets the memo of this ObservedTx.  # noqa: E501

        memo  # noqa: E501

        :return: The memo of this ObservedTx.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this ObservedTx.

        memo  # noqa: E501

        :param memo: The memo of this ObservedTx.  # noqa: E501
        :type: str
        """

        self._memo = memo

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
        if issubclass(ObservedTx, dict):
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
        if not isinstance(other, ObservedTx):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObservedTx):
            return True

        return self.to_dict() != other.to_dict()
