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


class Version(object):
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
        'current': 'str',
        'next': 'str'
    }

    attribute_map = {
        'current': 'current',
        'next': 'next'
    }

    def __init__(self, current=None, next=None, _configuration=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current = None
        self._next = None
        self.discriminator = None

        if current is not None:
            self.current = current
        if next is not None:
            self.next = next

    @property
    def current(self):
        """Gets the current of this Version.  # noqa: E501

        current version  # noqa: E501

        :return: The current of this Version.  # noqa: E501
        :rtype: str
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this Version.

        current version  # noqa: E501

        :param current: The current of this Version.  # noqa: E501
        :type: str
        """

        self._current = current

    @property
    def next(self):
        """Gets the next of this Version.  # noqa: E501

        next version  # noqa: E501

        :return: The next of this Version.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Version.

        next version  # noqa: E501

        :param next: The next of this Version.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Version):
            return True

        return self.to_dict() != other.to_dict()
