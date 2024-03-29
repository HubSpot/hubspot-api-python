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


class PropertyCreate(object):
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
        "hidden": "bool",
        "display_order": "int",
        "description": "str",
        "label": "str",
        "type": "str",
        "form_field": "bool",
        "group_name": "str",
        "referenced_object_type": "str",
        "name": "str",
        "options": "list[OptionInput]",
        "calculation_formula": "str",
        "has_unique_value": "bool",
        "field_type": "str",
        "external_options": "bool",
    }

    attribute_map = {
        "hidden": "hidden",
        "display_order": "displayOrder",
        "description": "description",
        "label": "label",
        "type": "type",
        "form_field": "formField",
        "group_name": "groupName",
        "referenced_object_type": "referencedObjectType",
        "name": "name",
        "options": "options",
        "calculation_formula": "calculationFormula",
        "has_unique_value": "hasUniqueValue",
        "field_type": "fieldType",
        "external_options": "externalOptions",
    }

    def __init__(
        self,
        hidden=None,
        display_order=None,
        description=None,
        label=None,
        type=None,
        form_field=None,
        group_name=None,
        referenced_object_type=None,
        name=None,
        options=None,
        calculation_formula=None,
        has_unique_value=None,
        field_type=None,
        external_options=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PropertyCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hidden = None
        self._display_order = None
        self._description = None
        self._label = None
        self._type = None
        self._form_field = None
        self._group_name = None
        self._referenced_object_type = None
        self._name = None
        self._options = None
        self._calculation_formula = None
        self._has_unique_value = None
        self._field_type = None
        self._external_options = None
        self.discriminator = None

        if hidden is not None:
            self.hidden = hidden
        if display_order is not None:
            self.display_order = display_order
        if description is not None:
            self.description = description
        self.label = label
        self.type = type
        if form_field is not None:
            self.form_field = form_field
        self.group_name = group_name
        if referenced_object_type is not None:
            self.referenced_object_type = referenced_object_type
        self.name = name
        if options is not None:
            self.options = options
        if calculation_formula is not None:
            self.calculation_formula = calculation_formula
        if has_unique_value is not None:
            self.has_unique_value = has_unique_value
        self.field_type = field_type
        if external_options is not None:
            self.external_options = external_options

    @property
    def hidden(self):
        """Gets the hidden of this PropertyCreate.  # noqa: E501

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :return: The hidden of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this PropertyCreate.

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :param hidden: The hidden of this PropertyCreate.  # noqa: E501
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def display_order(self):
        """Gets the display_order of this PropertyCreate.  # noqa: E501

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values.  # noqa: E501

        :return: The display_order of this PropertyCreate.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PropertyCreate.

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values.  # noqa: E501

        :param display_order: The display_order of this PropertyCreate.  # noqa: E501
        :type display_order: int
        """

        self._display_order = display_order

    @property
    def description(self):
        """Gets the description of this PropertyCreate.  # noqa: E501

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :return: The description of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PropertyCreate.

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :param description: The description of this PropertyCreate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this PropertyCreate.  # noqa: E501

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PropertyCreate.

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this PropertyCreate.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def type(self):
        """Gets the type of this PropertyCreate.  # noqa: E501

        The data type of the property.  # noqa: E501

        :return: The type of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyCreate.

        The data type of the property.  # noqa: E501

        :param type: The type of this PropertyCreate.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "date", "datetime", "enumeration", "bool"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def form_field(self):
        """Gets the form_field of this PropertyCreate.  # noqa: E501

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :return: The form_field of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._form_field

    @form_field.setter
    def form_field(self, form_field):
        """Sets the form_field of this PropertyCreate.

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :param form_field: The form_field of this PropertyCreate.  # noqa: E501
        :type form_field: bool
        """

        self._form_field = form_field

    @property
    def group_name(self):
        """Gets the group_name of this PropertyCreate.  # noqa: E501

        The name of the property group the property belongs to.  # noqa: E501

        :return: The group_name of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PropertyCreate.

        The name of the property group the property belongs to.  # noqa: E501

        :param group_name: The group_name of this PropertyCreate.  # noqa: E501
        :type group_name: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def referenced_object_type(self):
        """Gets the referenced_object_type of this PropertyCreate.  # noqa: E501

        Should be set to 'OWNER' when 'externalOptions' is true, which causes the property to dynamically pull option values from the current HubSpot users.  # noqa: E501

        :return: The referenced_object_type of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._referenced_object_type

    @referenced_object_type.setter
    def referenced_object_type(self, referenced_object_type):
        """Sets the referenced_object_type of this PropertyCreate.

        Should be set to 'OWNER' when 'externalOptions' is true, which causes the property to dynamically pull option values from the current HubSpot users.  # noqa: E501

        :param referenced_object_type: The referenced_object_type of this PropertyCreate.  # noqa: E501
        :type referenced_object_type: str
        """

        self._referenced_object_type = referenced_object_type

    @property
    def name(self):
        """Gets the name of this PropertyCreate.  # noqa: E501

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :return: The name of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyCreate.

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :param name: The name of this PropertyCreate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def options(self):
        """Gets the options of this PropertyCreate.  # noqa: E501

        A list of valid options for the property. This field is required for enumerated properties.  # noqa: E501

        :return: The options of this PropertyCreate.  # noqa: E501
        :rtype: list[OptionInput]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PropertyCreate.

        A list of valid options for the property. This field is required for enumerated properties.  # noqa: E501

        :param options: The options of this PropertyCreate.  # noqa: E501
        :type options: list[OptionInput]
        """

        self._options = options

    @property
    def calculation_formula(self):
        """Gets the calculation_formula of this PropertyCreate.  # noqa: E501

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :return: The calculation_formula of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._calculation_formula

    @calculation_formula.setter
    def calculation_formula(self, calculation_formula):
        """Sets the calculation_formula of this PropertyCreate.

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :param calculation_formula: The calculation_formula of this PropertyCreate.  # noqa: E501
        :type calculation_formula: str
        """

        self._calculation_formula = calculation_formula

    @property
    def has_unique_value(self):
        """Gets the has_unique_value of this PropertyCreate.  # noqa: E501

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :return: The has_unique_value of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._has_unique_value

    @has_unique_value.setter
    def has_unique_value(self, has_unique_value):
        """Sets the has_unique_value of this PropertyCreate.

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :param has_unique_value: The has_unique_value of this PropertyCreate.  # noqa: E501
        :type has_unique_value: bool
        """

        self._has_unique_value = has_unique_value

    @property
    def field_type(self):
        """Gets the field_type of this PropertyCreate.  # noqa: E501

        Controls how the property appears in HubSpot.  # noqa: E501

        :return: The field_type of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this PropertyCreate.

        Controls how the property appears in HubSpot.  # noqa: E501

        :param field_type: The field_type of this PropertyCreate.  # noqa: E501
        :type field_type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501
        allowed_values = ["textarea", "text", "date", "file", "number", "select", "radio", "checkbox", "booleancheckbox", "calculation_equation"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `field_type` ({0}), must be one of {1}".format(field_type, allowed_values))  # noqa: E501

        self._field_type = field_type

    @property
    def external_options(self):
        """Gets the external_options of this PropertyCreate.  # noqa: E501

        Applicable only for 'enumeration' type properties.  Should be set to true in conjunction with a 'referencedObjectType' of 'OWNER'.  Otherwise false.  # noqa: E501

        :return: The external_options of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._external_options

    @external_options.setter
    def external_options(self, external_options):
        """Sets the external_options of this PropertyCreate.

        Applicable only for 'enumeration' type properties.  Should be set to true in conjunction with a 'referencedObjectType' of 'OWNER'.  Otherwise false.  # noqa: E501

        :param external_options: The external_options of this PropertyCreate.  # noqa: E501
        :type external_options: bool
        """

        self._external_options = external_options

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
        if not isinstance(other, PropertyCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyCreate):
            return True

        return self.to_dict() != other.to_dict()
