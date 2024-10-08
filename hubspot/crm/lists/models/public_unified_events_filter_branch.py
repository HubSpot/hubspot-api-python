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


class PublicUnifiedEventsFilterBranch(object):
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
        "event_type_id": "str",
        "coalescing_refine_by": "PublicFormSubmissionFilterCoalescingRefineBy",
        "filter_branch_operator": "str",
        "filters": "list[PublicPropertyAssociationFilterBranchFiltersInner]",
        "operator": "str",
    }

    attribute_map = {
        "filter_branch_type": "filterBranchType",
        "filter_branches": "filterBranches",
        "event_type_id": "eventTypeId",
        "coalescing_refine_by": "coalescingRefineBy",
        "filter_branch_operator": "filterBranchOperator",
        "filters": "filters",
        "operator": "operator",
    }

    def __init__(
        self,
        filter_branch_type="UNIFIED_EVENTS",
        filter_branches=None,
        event_type_id=None,
        coalescing_refine_by=None,
        filter_branch_operator=None,
        filters=None,
        operator=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicUnifiedEventsFilterBranch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_branch_type = None
        self._filter_branches = None
        self._event_type_id = None
        self._coalescing_refine_by = None
        self._filter_branch_operator = None
        self._filters = None
        self._operator = None
        self.discriminator = None

        self.filter_branch_type = filter_branch_type
        self.filter_branches = filter_branches
        self.event_type_id = event_type_id
        if coalescing_refine_by is not None:
            self.coalescing_refine_by = coalescing_refine_by
        self.filter_branch_operator = filter_branch_operator
        self.filters = filters
        self.operator = operator

    @property
    def filter_branch_type(self):
        """Gets the filter_branch_type of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The filter_branch_type of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: str
        """
        return self._filter_branch_type

    @filter_branch_type.setter
    def filter_branch_type(self, filter_branch_type):
        """Sets the filter_branch_type of this PublicUnifiedEventsFilterBranch.


        :param filter_branch_type: The filter_branch_type of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type filter_branch_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_branch_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_type`, must not be `None`")  # noqa: E501
        allowed_values = ["UNIFIED_EVENTS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_branch_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_type` ({0}), must be one of {1}".format(filter_branch_type, allowed_values))  # noqa: E501

        self._filter_branch_type = filter_branch_type

    @property
    def filter_branches(self):
        """Gets the filter_branches of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The filter_branches of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: list[PublicPropertyAssociationFilterBranchFilterBranchesInner]
        """
        return self._filter_branches

    @filter_branches.setter
    def filter_branches(self, filter_branches):
        """Sets the filter_branches of this PublicUnifiedEventsFilterBranch.


        :param filter_branches: The filter_branches of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type filter_branches: list[PublicPropertyAssociationFilterBranchFilterBranchesInner]
        """
        if self.local_vars_configuration.client_side_validation and filter_branches is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branches`, must not be `None`")  # noqa: E501

        self._filter_branches = filter_branches

    @property
    def event_type_id(self):
        """Gets the event_type_id of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The event_type_id of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this PublicUnifiedEventsFilterBranch.


        :param event_type_id: The event_type_id of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type event_type_id: str
        """
        if self.local_vars_configuration.client_side_validation and event_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type_id`, must not be `None`")  # noqa: E501

        self._event_type_id = event_type_id

    @property
    def coalescing_refine_by(self):
        """Gets the coalescing_refine_by of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The coalescing_refine_by of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: PublicFormSubmissionFilterCoalescingRefineBy
        """
        return self._coalescing_refine_by

    @coalescing_refine_by.setter
    def coalescing_refine_by(self, coalescing_refine_by):
        """Sets the coalescing_refine_by of this PublicUnifiedEventsFilterBranch.


        :param coalescing_refine_by: The coalescing_refine_by of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type coalescing_refine_by: PublicFormSubmissionFilterCoalescingRefineBy
        """

        self._coalescing_refine_by = coalescing_refine_by

    @property
    def filter_branch_operator(self):
        """Gets the filter_branch_operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The filter_branch_operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: str
        """
        return self._filter_branch_operator

    @filter_branch_operator.setter
    def filter_branch_operator(self, filter_branch_operator):
        """Sets the filter_branch_operator of this PublicUnifiedEventsFilterBranch.


        :param filter_branch_operator: The filter_branch_operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type filter_branch_operator: str
        """
        if self.local_vars_configuration.client_side_validation and filter_branch_operator is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_branch_operator`, must not be `None`")  # noqa: E501

        self._filter_branch_operator = filter_branch_operator

    @property
    def filters(self):
        """Gets the filters of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The filters of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: list[PublicPropertyAssociationFilterBranchFiltersInner]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this PublicUnifiedEventsFilterBranch.


        :param filters: The filters of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type filters: list[PublicPropertyAssociationFilterBranchFiltersInner]
        """
        if self.local_vars_configuration.client_side_validation and filters is None:  # noqa: E501
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501

        self._filters = filters

    @property
    def operator(self):
        """Gets the operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501


        :return: The operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicUnifiedEventsFilterBranch.


        :param operator: The operator of this PublicUnifiedEventsFilterBranch.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["HAS_COMPLETED", "HAS_NOT_COMPLETED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `operator` ({0}), must be one of {1}".format(operator, allowed_values))  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, PublicUnifiedEventsFilterBranch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicUnifiedEventsFilterBranch):
            return True

        return self.to_dict() != other.to_dict()
