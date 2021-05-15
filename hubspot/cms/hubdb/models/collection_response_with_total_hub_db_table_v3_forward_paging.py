"""
    HubDB endpoints

    HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [in the HubSpot CMS](https://knowledge.hubspot.com/cos-general/how-to-edit-hubdb-tables), but you can also use the API endpoints documented here. For more information on HubDB tables and using their data on a HubSpot site, see the [CMS developers site](https://designers.hubspot.com/docs/tools/hubdb). You can also see the [documentation for dynamic pages](https://designers.hubspot.com/docs/tutorials/how-to-build-dynamic-pages-with-hubdb) for more details about the `useForPages` field.  HubDB tables support `draft` and `live` versions and you can publish and unpublish the live version. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages using the existing data. Draft data can be reviewed, pushed to live version, and published by a user working in HubSpot or published via the API. Draft data can also be discarded, allowing users to go back to the live version of the data without disrupting it. If a table is set to be `allowed for public access`, you can access the published version of the table and rows without any authentication.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.hubdb.configuration import Configuration


class CollectionResponseWithTotalHubDbTableV3ForwardPaging:
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
        "total": "int",
        "results": "list[HubDbTableV3]",
        "paging": "ForwardPaging",
    }

    attribute_map = {"total": "total", "results": "results", "paging": "paging"}

    def __init__(
        self, total=None, results=None, paging=None, local_vars_configuration=None
    ):  # noqa: E501
        """CollectionResponseWithTotalHubDbTableV3ForwardPaging - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._results = None
        self._paging = None
        self.discriminator = None

        self.total = total
        self.results = results
        if paging is not None:
            self.paging = paging

    @property
    def total(self):
        """Gets the total of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501


        :return: The total of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.


        :param total: The total of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and total is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `total`, must not be `None`"
            )  # noqa: E501

        self._total = total

    @property
    def results(self):
        """Gets the results of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501


        :return: The results of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :rtype: list[HubDbTableV3]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.


        :param results: The results of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :type: list[HubDbTableV3]
        """
        if (
            self.local_vars_configuration.client_side_validation and results is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `results`, must not be `None`"
            )  # noqa: E501

        self._results = results

    @property
    def paging(self):
        """Gets the paging of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501


        :return: The paging of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :rtype: ForwardPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.


        :param paging: The paging of this CollectionResponseWithTotalHubDbTableV3ForwardPaging.  # noqa: E501
        :type: ForwardPaging
        """

        self._paging = paging

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollectionResponseWithTotalHubDbTableV3ForwardPaging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionResponseWithTotalHubDbTableV3ForwardPaging):
            return True

        return self.to_dict() != other.to_dict()
