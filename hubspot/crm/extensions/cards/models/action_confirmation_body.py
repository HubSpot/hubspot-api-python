# coding: utf-8

"""
    Public App Crm Cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

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

from hubspot.crm.extensions.cards.configuration import Configuration


class ActionConfirmationBody(object):
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
    openapi_types = {"confirm_button_label": "str", "cancel_button_label": "str", "prompt": "str"}

    attribute_map = {"confirm_button_label": "confirmButtonLabel", "cancel_button_label": "cancelButtonLabel", "prompt": "prompt"}

    def __init__(self, confirm_button_label=None, cancel_button_label=None, prompt=None, local_vars_configuration=None):  # noqa: E501
        """ActionConfirmationBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._confirm_button_label = None
        self._cancel_button_label = None
        self._prompt = None
        self.discriminator = None

        self.confirm_button_label = confirm_button_label
        self.cancel_button_label = cancel_button_label
        self.prompt = prompt

    @property
    def confirm_button_label(self):
        """Gets the confirm_button_label of this ActionConfirmationBody.  # noqa: E501


        :return: The confirm_button_label of this ActionConfirmationBody.  # noqa: E501
        :rtype: str
        """
        return self._confirm_button_label

    @confirm_button_label.setter
    def confirm_button_label(self, confirm_button_label):
        """Sets the confirm_button_label of this ActionConfirmationBody.


        :param confirm_button_label: The confirm_button_label of this ActionConfirmationBody.  # noqa: E501
        :type confirm_button_label: str
        """
        if self.local_vars_configuration.client_side_validation and confirm_button_label is None:  # noqa: E501
            raise ValueError("Invalid value for `confirm_button_label`, must not be `None`")  # noqa: E501

        self._confirm_button_label = confirm_button_label

    @property
    def cancel_button_label(self):
        """Gets the cancel_button_label of this ActionConfirmationBody.  # noqa: E501


        :return: The cancel_button_label of this ActionConfirmationBody.  # noqa: E501
        :rtype: str
        """
        return self._cancel_button_label

    @cancel_button_label.setter
    def cancel_button_label(self, cancel_button_label):
        """Sets the cancel_button_label of this ActionConfirmationBody.


        :param cancel_button_label: The cancel_button_label of this ActionConfirmationBody.  # noqa: E501
        :type cancel_button_label: str
        """
        if self.local_vars_configuration.client_side_validation and cancel_button_label is None:  # noqa: E501
            raise ValueError("Invalid value for `cancel_button_label`, must not be `None`")  # noqa: E501

        self._cancel_button_label = cancel_button_label

    @property
    def prompt(self):
        """Gets the prompt of this ActionConfirmationBody.  # noqa: E501


        :return: The prompt of this ActionConfirmationBody.  # noqa: E501
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this ActionConfirmationBody.


        :param prompt: The prompt of this ActionConfirmationBody.  # noqa: E501
        :type prompt: str
        """
        if self.local_vars_configuration.client_side_validation and prompt is None:  # noqa: E501
            raise ValueError("Invalid value for `prompt`, must not be `None`")  # noqa: E501

        self._prompt = prompt

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
        if not isinstance(other, ActionConfirmationBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionConfirmationBody):
            return True

        return self.to_dict() != other.to_dict()
