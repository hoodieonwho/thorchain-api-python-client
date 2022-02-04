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


class Node(object):
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
        'node_address': 'str',
        'status': 'str',
        'pub_key_set': 'object',
        'validator_cons_pub_key': 'str',
        'bond': 'str',
        'active_block_height': 'str',
        'bond_address': 'str',
        'status_since': 'str',
        'signer_membership': 'list[object]',
        'requested_to_leave': 'bool',
        'forced_to_leave': 'bool',
        'ip_address': 'str',
        'version': 'str',
        'slash_points': 'str',
        'jail': 'object',
        'current_award': 'str',
        'observe_chains': 'str',
        'preflight_status': 'object'
    }

    attribute_map = {
        'node_address': 'node_address',
        'status': 'status',
        'pub_key_set': 'pub_key_set',
        'validator_cons_pub_key': 'validator_cons_pub_key',
        'bond': 'bond',
        'active_block_height': 'active_block_height',
        'bond_address': 'bond_address',
        'status_since': 'status_since',
        'signer_membership': 'signer_membership',
        'requested_to_leave': 'requested_to_leave',
        'forced_to_leave': 'forced_to_leave',
        'ip_address': 'ip_address',
        'version': 'version',
        'slash_points': 'slash_points',
        'jail': 'jail',
        'current_award': 'current_award',
        'observe_chains': 'observe_chains',
        'preflight_status': 'preflight_status'
    }

    def __init__(self, node_address=None, status=None, pub_key_set=None, validator_cons_pub_key=None, bond=None, active_block_height=None, bond_address=None, status_since=None, signer_membership=None, requested_to_leave=None, forced_to_leave=None, ip_address=None, version=None, slash_points=None, jail=None, current_award=None, observe_chains=None, preflight_status=None, _configuration=None):  # noqa: E501
        """Node - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_address = None
        self._status = None
        self._pub_key_set = None
        self._validator_cons_pub_key = None
        self._bond = None
        self._active_block_height = None
        self._bond_address = None
        self._status_since = None
        self._signer_membership = None
        self._requested_to_leave = None
        self._forced_to_leave = None
        self._ip_address = None
        self._version = None
        self._slash_points = None
        self._jail = None
        self._current_award = None
        self._observe_chains = None
        self._preflight_status = None
        self.discriminator = None

        if node_address is not None:
            self.node_address = node_address
        if status is not None:
            self.status = status
        if pub_key_set is not None:
            self.pub_key_set = pub_key_set
        if validator_cons_pub_key is not None:
            self.validator_cons_pub_key = validator_cons_pub_key
        if bond is not None:
            self.bond = bond
        if active_block_height is not None:
            self.active_block_height = active_block_height
        if bond_address is not None:
            self.bond_address = bond_address
        if status_since is not None:
            self.status_since = status_since
        if signer_membership is not None:
            self.signer_membership = signer_membership
        if requested_to_leave is not None:
            self.requested_to_leave = requested_to_leave
        if forced_to_leave is not None:
            self.forced_to_leave = forced_to_leave
        if ip_address is not None:
            self.ip_address = ip_address
        if version is not None:
            self.version = version
        if slash_points is not None:
            self.slash_points = slash_points
        if jail is not None:
            self.jail = jail
        if current_award is not None:
            self.current_award = current_award
        if observe_chains is not None:
            self.observe_chains = observe_chains
        if preflight_status is not None:
            self.preflight_status = preflight_status

    @property
    def node_address(self):
        """Gets the node_address of this Node.  # noqa: E501

        node address  # noqa: E501

        :return: The node_address of this Node.  # noqa: E501
        :rtype: str
        """
        return self._node_address

    @node_address.setter
    def node_address(self, node_address):
        """Sets the node_address of this Node.

        node address  # noqa: E501

        :param node_address: The node_address of this Node.  # noqa: E501
        :type: str
        """

        self._node_address = node_address

    @property
    def status(self):
        """Gets the status of this Node.  # noqa: E501

        status , values can be active,disabled,standby  # noqa: E501

        :return: The status of this Node.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Node.

        status , values can be active,disabled,standby  # noqa: E501

        :param status: The status of this Node.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def pub_key_set(self):
        """Gets the pub_key_set of this Node.  # noqa: E501


        :return: The pub_key_set of this Node.  # noqa: E501
        :rtype: object
        """
        return self._pub_key_set

    @pub_key_set.setter
    def pub_key_set(self, pub_key_set):
        """Sets the pub_key_set of this Node.


        :param pub_key_set: The pub_key_set of this Node.  # noqa: E501
        :type: object
        """

        self._pub_key_set = pub_key_set

    @property
    def validator_cons_pub_key(self):
        """Gets the validator_cons_pub_key of this Node.  # noqa: E501

        the consensus pubkey used by the node  # noqa: E501

        :return: The validator_cons_pub_key of this Node.  # noqa: E501
        :rtype: str
        """
        return self._validator_cons_pub_key

    @validator_cons_pub_key.setter
    def validator_cons_pub_key(self, validator_cons_pub_key):
        """Sets the validator_cons_pub_key of this Node.

        the consensus pubkey used by the node  # noqa: E501

        :param validator_cons_pub_key: The validator_cons_pub_key of this Node.  # noqa: E501
        :type: str
        """

        self._validator_cons_pub_key = validator_cons_pub_key

    @property
    def bond(self):
        """Gets the bond of this Node.  # noqa: E501

        current bond  # noqa: E501

        :return: The bond of this Node.  # noqa: E501
        :rtype: str
        """
        return self._bond

    @bond.setter
    def bond(self, bond):
        """Sets the bond of this Node.

        current bond  # noqa: E501

        :param bond: The bond of this Node.  # noqa: E501
        :type: str
        """

        self._bond = bond

    @property
    def active_block_height(self):
        """Gets the active_block_height of this Node.  # noqa: E501

        block height this node become active  # noqa: E501

        :return: The active_block_height of this Node.  # noqa: E501
        :rtype: str
        """
        return self._active_block_height

    @active_block_height.setter
    def active_block_height(self, active_block_height):
        """Sets the active_block_height of this Node.

        block height this node become active  # noqa: E501

        :param active_block_height: The active_block_height of this Node.  # noqa: E501
        :type: str
        """

        self._active_block_height = active_block_height

    @property
    def bond_address(self):
        """Gets the bond_address of this Node.  # noqa: E501

        bond address  # noqa: E501

        :return: The bond_address of this Node.  # noqa: E501
        :rtype: str
        """
        return self._bond_address

    @bond_address.setter
    def bond_address(self, bond_address):
        """Sets the bond_address of this Node.

        bond address  # noqa: E501

        :param bond_address: The bond_address of this Node.  # noqa: E501
        :type: str
        """

        self._bond_address = bond_address

    @property
    def status_since(self):
        """Gets the status_since of this Node.  # noqa: E501

        block height this node become current status  # noqa: E501

        :return: The status_since of this Node.  # noqa: E501
        :rtype: str
        """
        return self._status_since

    @status_since.setter
    def status_since(self, status_since):
        """Sets the status_since of this Node.

        block height this node become current status  # noqa: E501

        :param status_since: The status_since of this Node.  # noqa: E501
        :type: str
        """

        self._status_since = status_since

    @property
    def signer_membership(self):
        """Gets the signer_membership of this Node.  # noqa: E501

        a list of vault public key that this node is a member of  # noqa: E501

        :return: The signer_membership of this Node.  # noqa: E501
        :rtype: list[object]
        """
        return self._signer_membership

    @signer_membership.setter
    def signer_membership(self, signer_membership):
        """Sets the signer_membership of this Node.

        a list of vault public key that this node is a member of  # noqa: E501

        :param signer_membership: The signer_membership of this Node.  # noqa: E501
        :type: list[object]
        """

        self._signer_membership = signer_membership

    @property
    def requested_to_leave(self):
        """Gets the requested_to_leave of this Node.  # noqa: E501

        indicate whether this node had requested to leave_height  # noqa: E501

        :return: The requested_to_leave of this Node.  # noqa: E501
        :rtype: bool
        """
        return self._requested_to_leave

    @requested_to_leave.setter
    def requested_to_leave(self, requested_to_leave):
        """Sets the requested_to_leave of this Node.

        indicate whether this node had requested to leave_height  # noqa: E501

        :param requested_to_leave: The requested_to_leave of this Node.  # noqa: E501
        :type: bool
        """

        self._requested_to_leave = requested_to_leave

    @property
    def forced_to_leave(self):
        """Gets the forced_to_leave of this Node.  # noqa: E501

        indicate whether this node had been forced to leave by the network or not, if this field is true , usually means this node had been banned  # noqa: E501

        :return: The forced_to_leave of this Node.  # noqa: E501
        :rtype: bool
        """
        return self._forced_to_leave

    @forced_to_leave.setter
    def forced_to_leave(self, forced_to_leave):
        """Sets the forced_to_leave of this Node.

        indicate whether this node had been forced to leave by the network or not, if this field is true , usually means this node had been banned  # noqa: E501

        :param forced_to_leave: The forced_to_leave of this Node.  # noqa: E501
        :type: bool
        """

        self._forced_to_leave = forced_to_leave

    @property
    def ip_address(self):
        """Gets the ip_address of this Node.  # noqa: E501

        node ip address  # noqa: E501

        :return: The ip_address of this Node.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Node.

        node ip address  # noqa: E501

        :param ip_address: The ip_address of this Node.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def version(self):
        """Gets the version of this Node.  # noqa: E501

        the version of thornode software this node is running  # noqa: E501

        :return: The version of this Node.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Node.

        the version of thornode software this node is running  # noqa: E501

        :param version: The version of this Node.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def slash_points(self):
        """Gets the slash_points of this Node.  # noqa: E501

        the slash points the node accumulated when they are active , slash points will be reset next time when node become active  # noqa: E501

        :return: The slash_points of this Node.  # noqa: E501
        :rtype: str
        """
        return self._slash_points

    @slash_points.setter
    def slash_points(self, slash_points):
        """Sets the slash_points of this Node.

        the slash points the node accumulated when they are active , slash points will be reset next time when node become active  # noqa: E501

        :param slash_points: The slash_points of this Node.  # noqa: E501
        :type: str
        """

        self._slash_points = slash_points

    @property
    def jail(self):
        """Gets the jail of this Node.  # noqa: E501


        :return: The jail of this Node.  # noqa: E501
        :rtype: object
        """
        return self._jail

    @jail.setter
    def jail(self, jail):
        """Sets the jail of this Node.


        :param jail: The jail of this Node.  # noqa: E501
        :type: object
        """

        self._jail = jail

    @property
    def current_award(self):
        """Gets the current_award of this Node.  # noqa: E501

        node current award  # noqa: E501

        :return: The current_award of this Node.  # noqa: E501
        :rtype: str
        """
        return self._current_award

    @current_award.setter
    def current_award(self, current_award):
        """Sets the current_award of this Node.

        node current award  # noqa: E501

        :param current_award: The current_award of this Node.  # noqa: E501
        :type: str
        """

        self._current_award = current_award

    @property
    def observe_chains(self):
        """Gets the observe_chains of this Node.  # noqa: E501

        chain and block heights this node is observing , this is useful to know whether a node is falling behind in regards to observing  # noqa: E501

        :return: The observe_chains of this Node.  # noqa: E501
        :rtype: str
        """
        return self._observe_chains

    @observe_chains.setter
    def observe_chains(self, observe_chains):
        """Sets the observe_chains of this Node.

        chain and block heights this node is observing , this is useful to know whether a node is falling behind in regards to observing  # noqa: E501

        :param observe_chains: The observe_chains of this Node.  # noqa: E501
        :type: str
        """

        self._observe_chains = observe_chains

    @property
    def preflight_status(self):
        """Gets the preflight_status of this Node.  # noqa: E501


        :return: The preflight_status of this Node.  # noqa: E501
        :rtype: object
        """
        return self._preflight_status

    @preflight_status.setter
    def preflight_status(self, preflight_status):
        """Sets the preflight_status of this Node.


        :param preflight_status: The preflight_status of this Node.  # noqa: E501
        :type: object
        """

        self._preflight_status = preflight_status

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
        if issubclass(Node, dict):
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
        if not isinstance(other, Node):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Node):
            return True

        return self.to_dict() != other.to_dict()
