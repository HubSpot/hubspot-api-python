# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

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

from hubspot.crm.properties.configuration import Configuration


class PropertyUpdate(object):
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
    openapi_types = {
        "group_name": "str",
        "hidden": "bool",
        "options": "list[OptionInput]",
        "display_order": "int",
        "description": "str",
        "calculation_formula": "str",
        "label": "str",
        "type": "str",
        "field_type": "str",
        "form_field": "bool",
    }

    attribute_map = {
        "group_name": "groupName",
        "hidden": "hidden",
        "options": "options",
        "display_order": "displayOrder",
        "description": "description",
        "calculation_formula": "calculationFormula",
        "label": "label",
        "type": "type",
        "field_type": "fieldType",
        "form_field": "formField",
    }

    def __init__(
        self,
        group_name=None,
        hidden=None,
        options=None,
        display_order=None,
        description=None,
        calculation_formula=None,
        label=None,
        type=None,
        field_type=None,
        form_field=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PropertyUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group_name = None
        self._hidden = None
        self._options = None
        self._display_order = None
        self._description = None
        self._calculation_formula = None
        self._label = None
        self._type = None
        self._field_type = None
        self._form_field = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if hidden is not None:
            self.hidden = hidden
        if options is not None:
            self.options = options
        if display_order is not None:
            self.display_order = display_order
        if description is not None:
            self.description = description
        if calculation_formula is not None:
            self.calculation_formula = calculation_formula
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if field_type is not None:
            self.field_type = field_type
        if form_field is not None:
            self.form_field = form_field

    @property
    def group_name(self):
        """Gets the group_name of this PropertyUpdate.  # noqa: E501

        The name of the property group the property belongs to.  # noqa: E501

        :return: The group_name of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PropertyUpdate.

        The name of the property group the property belongs to.  # noqa: E501

        :param group_name: The group_name of this PropertyUpdate.  # noqa: E501
        :type group_name: str
        """

        self._group_name = group_name

    @property
    def hidden(self):
        """Gets the hidden of this PropertyUpdate.  # noqa: E501

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :return: The hidden of this PropertyUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this PropertyUpdate.

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :param hidden: The hidden of this PropertyUpdate.  # noqa: E501
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def options(self):
        """Gets the options of this PropertyUpdate.  # noqa: E501

        A list of valid options for the property.  # noqa: E501

        :return: The options of this PropertyUpdate.  # noqa: E501
        :rtype: list[OptionInput]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PropertyUpdate.

        A list of valid options for the property.  # noqa: E501

        :param options: The options of this PropertyUpdate.  # noqa: E501
        :type options: list[OptionInput]
        """

        self._options = options

    @property
    def display_order(self):
        """Gets the display_order of this PropertyUpdate.  # noqa: E501

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the Property to be displayed after any positive values.  # noqa: E501

        :return: The display_order of this PropertyUpdate.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PropertyUpdate.

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the Property to be displayed after any positive values.  # noqa: E501

        :param display_order: The display_order of this PropertyUpdate.  # noqa: E501
        :type display_order: int
        """

        self._display_order = display_order

    @property
    def description(self):
        """Gets the description of this PropertyUpdate.  # noqa: E501

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :return: The description of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PropertyUpdate.

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :param description: The description of this PropertyUpdate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def calculation_formula(self):
        """Gets the calculation_formula of this PropertyUpdate.  # noqa: E501

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :return: The calculation_formula of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._calculation_formula

    @calculation_formula.setter
    def calculation_formula(self, calculation_formula):
        """Sets the calculation_formula of this PropertyUpdate.

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :param calculation_formula: The calculation_formula of this PropertyUpdate.  # noqa: E501
        :type calculation_formula: str
        """

        self._calculation_formula = calculation_formula

    @property
    def label(self):
        """Gets the label of this PropertyUpdate.  # noqa: E501

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PropertyUpdate.

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this PropertyUpdate.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this PropertyUpdate.  # noqa: E501

        The data type of the property.  # noqa: E501

        :return: The type of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyUpdate.

        The data type of the property.  # noqa: E501

        :param type: The type of this PropertyUpdate.  # noqa: E501
        :type type: str
        """
        allowed_values = ["string", "number", "date", "datetime", "enumeration", "bool"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def field_type(self):
        """Gets the field_type of this PropertyUpdate.  # noqa: E501

        Controls how the property appears in HubSpot.  # noqa: E501

        :return: The field_type of this PropertyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this PropertyUpdate.

        Controls how the property appears in HubSpot.  # noqa: E501

        :param field_type: The field_type of this PropertyUpdate.  # noqa: E501
        :type field_type: str
        """
        allowed_values = ["textarea", "text", "date", "file", "number", "select", "radio", "checkbox", "booleancheckbox", "calculation_equation"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `field_type` ({0}), must be one of {1}".format(field_type, allowed_values))  # noqa: E501

        self._field_type = field_type

    @property
    def form_field(self):
        """Gets the form_field of this PropertyUpdate.  # noqa: E501

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :return: The form_field of this PropertyUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._form_field

    @form_field.setter
    def form_field(self, form_field):
        """Sets the form_field of this PropertyUpdate.

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :param form_field: The form_field of this PropertyUpdate.  # noqa: E501
        :type form_field: bool
        """

        self._form_field = form_field

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
        if not isinstance(other, PropertyUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyUpdate):
            return True

        return self.to_dict() != other.to_dict()
