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

class THORNameDetails(object):
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
        'entries': 'list[THORNameEntry]',
        'expire': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'entries': 'entries',
        'expire': 'expire',
        'owner': 'owner'
    }

    def __init__(self, entries=None, expire=None, owner=None):  # noqa: E501
        """THORNameDetails - a model defined in Swagger"""  # noqa: E501
        self._entries = None
        self._expire = None
        self._owner = None
        self.discriminator = None
        self.entries = entries
        self.expire = expire
        self.owner = owner

    @property
    def entries(self):
        """Gets the entries of this THORNameDetails.  # noqa: E501

        List details of all chains and their addresses for a given THORName  # noqa: E501

        :return: The entries of this THORNameDetails.  # noqa: E501
        :rtype: list[THORNameEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this THORNameDetails.

        List details of all chains and their addresses for a given THORName  # noqa: E501

        :param entries: The entries of this THORNameDetails.  # noqa: E501
        :type: list[THORNameEntry]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def expire(self):
        """Gets the expire of this THORNameDetails.  # noqa: E501

        Int64, THORChain block height in which THORName expires  # noqa: E501

        :return: The expire of this THORNameDetails.  # noqa: E501
        :rtype: str
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this THORNameDetails.

        Int64, THORChain block height in which THORName expires  # noqa: E501

        :param expire: The expire of this THORNameDetails.  # noqa: E501
        :type: str
        """
        if expire is None:
            raise ValueError("Invalid value for `expire`, must not be `None`")  # noqa: E501

        self._expire = expire

    @property
    def owner(self):
        """Gets the owner of this THORNameDetails.  # noqa: E501

        owner's THOR address  # noqa: E501

        :return: The owner of this THORNameDetails.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this THORNameDetails.

        owner's THOR address  # noqa: E501

        :param owner: The owner of this THORNameDetails.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

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
        if issubclass(THORNameDetails, dict):
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
        if not isinstance(other, THORNameDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
