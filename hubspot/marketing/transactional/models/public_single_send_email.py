# coding: utf-8

"""
    Transactional Single Send

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.marketing.transactional.configuration import Configuration


class PublicSingleSendEmail(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"cc": "list[str]", "send_id": "str", "bcc": "list[str]", "reply_to": "list[str]", "_from": "str", "to": "str"}

    attribute_map = {"cc": "cc", "send_id": "sendId", "bcc": "bcc", "reply_to": "replyTo", "_from": "from", "to": "to"}

    def __init__(self, cc=None, send_id=None, bcc=None, reply_to=None, _from=None, to=None, local_vars_configuration=None):  # noqa: E501
        """PublicSingleSendEmail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cc = None
        self._send_id = None
        self._bcc = None
        self._reply_to = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if cc is not None:
            self.cc = cc
        if send_id is not None:
            self.send_id = send_id
        if bcc is not None:
            self.bcc = bcc
        if reply_to is not None:
            self.reply_to = reply_to
        if _from is not None:
            self._from = _from
        self.to = to

    @property
    def cc(self):
        """Gets the cc of this PublicSingleSendEmail.  # noqa: E501

        List of email addresses to send as Cc.  # noqa: E501

        :return: The cc of this PublicSingleSendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this PublicSingleSendEmail.

        List of email addresses to send as Cc.  # noqa: E501

        :param cc: The cc of this PublicSingleSendEmail.  # noqa: E501
        :type cc: list[str]
        """

        self._cc = cc

    @property
    def send_id(self):
        """Gets the send_id of this PublicSingleSendEmail.  # noqa: E501

        ID for a particular send. No more than one email will be sent per sendId.  # noqa: E501

        :return: The send_id of this PublicSingleSendEmail.  # noqa: E501
        :rtype: str
        """
        return self._send_id

    @send_id.setter
    def send_id(self, send_id):
        """Sets the send_id of this PublicSingleSendEmail.

        ID for a particular send. No more than one email will be sent per sendId.  # noqa: E501

        :param send_id: The send_id of this PublicSingleSendEmail.  # noqa: E501
        :type send_id: str
        """

        self._send_id = send_id

    @property
    def bcc(self):
        """Gets the bcc of this PublicSingleSendEmail.  # noqa: E501

        List of email addresses to send as Bcc.  # noqa: E501

        :return: The bcc of this PublicSingleSendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this PublicSingleSendEmail.

        List of email addresses to send as Bcc.  # noqa: E501

        :param bcc: The bcc of this PublicSingleSendEmail.  # noqa: E501
        :type bcc: list[str]
        """

        self._bcc = bcc

    @property
    def reply_to(self):
        """Gets the reply_to of this PublicSingleSendEmail.  # noqa: E501

        List of Reply-To header values for the email.  # noqa: E501

        :return: The reply_to of this PublicSingleSendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this PublicSingleSendEmail.

        List of Reply-To header values for the email.  # noqa: E501

        :param reply_to: The reply_to of this PublicSingleSendEmail.  # noqa: E501
        :type reply_to: list[str]
        """

        self._reply_to = reply_to

    @property
    def _from(self):
        """Gets the _from of this PublicSingleSendEmail.  # noqa: E501

        The From header for the email.  # noqa: E501

        :return: The _from of this PublicSingleSendEmail.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this PublicSingleSendEmail.

        The From header for the email.  # noqa: E501

        :param _from: The _from of this PublicSingleSendEmail.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this PublicSingleSendEmail.  # noqa: E501

        The recipient of the email.  # noqa: E501

        :return: The to of this PublicSingleSendEmail.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PublicSingleSendEmail.

        The recipient of the email.  # noqa: E501

        :param to: The to of this PublicSingleSendEmail.  # noqa: E501
        :type to: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicSingleSendEmail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicSingleSendEmail):
            return True

        return self.to_dict() != other.to_dict()
