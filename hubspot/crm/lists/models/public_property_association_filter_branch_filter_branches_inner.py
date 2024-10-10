# coding: utf-8

"""
    Lists

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

from hubspot.crm.lists.configuration import Configuration


class PublicPropertyAssociationFilterBranchFilterBranchesInner(object):
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
        "filter_branch_type": "str",
        "filter_branches": "list[PublicPropertyAssociationFilterBranchFilterBranchesInner]",
        "filter_branch_operator": "str",
        "filters": "list[PublicPropertyAssociationFilterBranchFiltersInner]",
        "event_type_id": "str",
        "coalescing_refine_by": "PublicFormSubmissionFilterCoalescingRefineBy",
        "operator": "str",
        "object_type_id": "str",
        "property_with_object_id": "str",
        "association_type_id": "int",
        "association_category": "str",
    }

    attribute_map = {
        "filter_branch_type": "filterBranchType",
        "filter_branches": "filterBranches",
        "filter_branch_operator": "filterBranchOperator",
        "filters": "filters",
        "event_type_id": "eventTypeId",
        "coalescing_refine_by": "coalescingRefineBy",
        "operator": "operator",
        "object_type_id": "objectTypeId",
        "property_with_object_id": "propertyWithObjectId",
        "association_type_id": "associationTypeId",
        "association_category": "associationCategory",
    }

    def __init__(
        self,
        filter_branch_type="ASSOCIATION",
        filter_branches=None,
        filter_branch_operator=None,
        filters=None,
        event_type_id=None,
        coalescing_refine_by=None,
        operator=None,
        object_type_id=None,
        property_with_object_id=None,
        association_type_id=None,
        association_category=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicPropertyAssociationFilterBranchFilterBranchesInner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_branch_type = None
        self._filter_branches = None
        self._filter_branch_operator = None
        self._filters = None
        self._event_type_id = None
        self._coalescing_refine_by = None
        self._operator = None
        self._object_type_id = None
        self._property_with_object_id = None
        self._association_type_id = None
        self._association_category = None
        self.discriminator = None

        self.filter_branch_type = filter_branch_type
        self.filter_branches = filter_branches
        self.filter_branch_operator = filter_branch_operator
        self.filters = filters
        self.event_type_id = event_type_id
        if coalescing_refine_by is not None:
            self.coalescing_refine_by = coalescing_refine_by
        self.operator = operator
        self.object_type_id = object_type_id
        self.property_with_object_id = property_with_object_id
        self.association_type_id = association_type_id
        self.association_category = association_category

    @property
    def filter_branch_type(self):
        """Gets the filter_branch_type of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The filter_branch_type of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._filter_branch_type

    @filter_branch_type.setter
    def filter_branch_type(self, filter_branch_type):
        """Sets the filter_branch_type of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param filter_branch_type: The filter_branch_type of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type filter_branch_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_branch_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ASSOCIATION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_branch_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_type` ({0}), must be one of {1}".format(filter_branch_type, allowed_values))  # noqa: E501

        self._filter_branch_type = filter_branch_type

    @property
    def filter_branches(self):
        """Gets the filter_branches of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The filter_branches of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: list[PublicPropertyAssociationFilterBranchFilterBranchesInner]
        """
        return self._filter_branches

    @filter_branches.setter
    def filter_branches(self, filter_branches):
        """Sets the filter_branches of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param filter_branches: The filter_branches of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type filter_branches: list[PublicPropertyAssociationFilterBranchFilterBranchesInner]
        """
        if self.local_vars_configuration.client_side_validation and filter_branches is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branches`, must not be `None`")  # noqa: E501

        self._filter_branches = filter_branches

    @property
    def filter_branch_operator(self):
        """Gets the filter_branch_operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The filter_branch_operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._filter_branch_operator

    @filter_branch_operator.setter
    def filter_branch_operator(self, filter_branch_operator):
        """Sets the filter_branch_operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param filter_branch_operator: The filter_branch_operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type filter_branch_operator: str
        """
        if self.local_vars_configuration.client_side_validation and filter_branch_operator is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_operator`, must not be `None`")  # noqa: E501

        self._filter_branch_operator = filter_branch_operator

    @property
    def filters(self):
        """Gets the filters of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The filters of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: list[PublicPropertyAssociationFilterBranchFiltersInner]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param filters: The filters of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type filters: list[PublicPropertyAssociationFilterBranchFiltersInner]
        """
        if self.local_vars_configuration.client_side_validation and filters is None:  # noqa: E501
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501

        self._filters = filters

    @property
    def event_type_id(self):
        """Gets the event_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The event_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param event_type_id: The event_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type event_type_id: str
        """
        if self.local_vars_configuration.client_side_validation and event_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type_id`, must not be `None`")  # noqa: E501

        self._event_type_id = event_type_id

    @property
    def coalescing_refine_by(self):
        """Gets the coalescing_refine_by of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The coalescing_refine_by of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: PublicFormSubmissionFilterCoalescingRefineBy
        """
        return self._coalescing_refine_by

    @coalescing_refine_by.setter
    def coalescing_refine_by(self, coalescing_refine_by):
        """Sets the coalescing_refine_by of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param coalescing_refine_by: The coalescing_refine_by of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type coalescing_refine_by: PublicFormSubmissionFilterCoalescingRefineBy
        """

        self._coalescing_refine_by = coalescing_refine_by

    @property
    def operator(self):
        """Gets the operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param operator: The operator of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def object_type_id(self):
        """Gets the object_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The object_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param object_type_id: The object_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type object_type_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def property_with_object_id(self):
        """Gets the property_with_object_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The property_with_object_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._property_with_object_id

    @property_with_object_id.setter
    def property_with_object_id(self, property_with_object_id):
        """Sets the property_with_object_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param property_with_object_id: The property_with_object_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type property_with_object_id: str
        """
        if self.local_vars_configuration.client_side_validation and property_with_object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `property_with_object_id`, must not be `None`")  # noqa: E501

        self._property_with_object_id = property_with_object_id

    @property
    def association_type_id(self):
        """Gets the association_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The association_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: int
        """
        return self._association_type_id

    @association_type_id.setter
    def association_type_id(self, association_type_id):
        """Sets the association_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param association_type_id: The association_type_id of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type association_type_id: int
        """
        if self.local_vars_configuration.client_side_validation and association_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `association_type_id`, must not be `None`")  # noqa: E501

        self._association_type_id = association_type_id

    @property
    def association_category(self):
        """Gets the association_category of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501


        :return: The association_category of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :rtype: str
        """
        return self._association_category

    @association_category.setter
    def association_category(self, association_category):
        """Sets the association_category of this PublicPropertyAssociationFilterBranchFilterBranchesInner.


        :param association_category: The association_category of this PublicPropertyAssociationFilterBranchFilterBranchesInner.  # noqa: E501
        :type association_category: str
        """
        if self.local_vars_configuration.client_side_validation and association_category is None:  # noqa: E501
            raise ValueError("Invalid value for `association_category`, must not be `None`")  # noqa: E501

        self._association_category = association_category

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
        if not isinstance(other, PublicPropertyAssociationFilterBranchFilterBranchesInner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicPropertyAssociationFilterBranchFilterBranchesInner):
            return True

        return self.to_dict() != other.to_dict()
