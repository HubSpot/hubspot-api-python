# coding: utf-8

"""
    CRM Deal Splits

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

from hubspot.crm.objects.deal_splits.configuration import Configuration


class ErrorDetail(object):
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
    openapi_types = {"sub_category": "str", "code": "str", "_in": "str", "context": "dict[str, list[str]]", "message": "str"}

    attribute_map = {"sub_category": "subCategory", "code": "code", "_in": "in", "context": "context", "message": "message"}

    def __init__(self, sub_category=None, code=None, _in=None, context=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ErrorDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sub_category = None
        self._code = None
        self.__in = None
        self._context = None
        self._message = None
        self.discriminator = None

        if sub_category is not None:
            self.sub_category = sub_category
        if code is not None:
            self.code = code
        if _in is not None:
            self._in = _in
        if context is not None:
            self.context = context
        self.message = message

    @property
    def sub_category(self):
        """Gets the sub_category of this ErrorDetail.  # noqa: E501

        A specific category that contains more specific detail about the error  # noqa: E501

        :return: The sub_category of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this ErrorDetail.

        A specific category that contains more specific detail about the error  # noqa: E501

        :param sub_category: The sub_category of this ErrorDetail.  # noqa: E501
        :type sub_category: str
        """

        self._sub_category = sub_category

    @property
    def code(self):
        """Gets the code of this ErrorDetail.  # noqa: E501

        The status code associated with the error detail  # noqa: E501

        :return: The code of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetail.

        The status code associated with the error detail  # noqa: E501

        :param code: The code of this ErrorDetail.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def _in(self):
        """Gets the _in of this ErrorDetail.  # noqa: E501

        The name of the field or parameter in which the error was found.  # noqa: E501

        :return: The _in of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this ErrorDetail.

        The name of the field or parameter in which the error was found.  # noqa: E501

        :param _in: The _in of this ErrorDetail.  # noqa: E501
        :type _in: str
        """

        self.__in = _in

    @property
    def context(self):
        """Gets the context of this ErrorDetail.  # noqa: E501

        Context about the error condition  # noqa: E501

        :return: The context of this ErrorDetail.  # noqa: E501
        :rtype: dict[str, list[str]]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ErrorDetail.

        Context about the error condition  # noqa: E501

        :param context: The context of this ErrorDetail.  # noqa: E501
        :type context: dict[str, list[str]]
        """

        self._context = context

    @property
    def message(self):
        """Gets the message of this ErrorDetail.  # noqa: E501

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :return: The message of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetail.

        A human readable message describing the error along with remediation steps where appropriate  # noqa: E501

        :param message: The message of this ErrorDetail.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()
