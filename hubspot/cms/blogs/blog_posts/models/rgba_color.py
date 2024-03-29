# coding: utf-8

"""
    Posts

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

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

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class RGBAColor(object):
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
    openapi_types = {"a": "float", "r": "int", "b": "int", "g": "int"}

    attribute_map = {"a": "a", "r": "r", "b": "b", "g": "g"}

    def __init__(self, a=None, r=None, b=None, g=None, local_vars_configuration=None):  # noqa: E501
        """RGBAColor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._a = None
        self._r = None
        self._b = None
        self._g = None
        self.discriminator = None

        self.a = a
        self.r = r
        self.b = b
        self.g = g

    @property
    def a(self):
        """Gets the a of this RGBAColor.  # noqa: E501

        Alpha.  # noqa: E501

        :return: The a of this RGBAColor.  # noqa: E501
        :rtype: float
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this RGBAColor.

        Alpha.  # noqa: E501

        :param a: The a of this RGBAColor.  # noqa: E501
        :type a: float
        """
        if self.local_vars_configuration.client_side_validation and a is None:  # noqa: E501
            raise ValueError("Invalid value for `a`, must not be `None`")  # noqa: E501

        self._a = a

    @property
    def r(self):
        """Gets the r of this RGBAColor.  # noqa: E501

        Red.  # noqa: E501

        :return: The r of this RGBAColor.  # noqa: E501
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this RGBAColor.

        Red.  # noqa: E501

        :param r: The r of this RGBAColor.  # noqa: E501
        :type r: int
        """
        if self.local_vars_configuration.client_side_validation and r is None:  # noqa: E501
            raise ValueError("Invalid value for `r`, must not be `None`")  # noqa: E501

        self._r = r

    @property
    def b(self):
        """Gets the b of this RGBAColor.  # noqa: E501

        Blue.  # noqa: E501

        :return: The b of this RGBAColor.  # noqa: E501
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this RGBAColor.

        Blue.  # noqa: E501

        :param b: The b of this RGBAColor.  # noqa: E501
        :type b: int
        """
        if self.local_vars_configuration.client_side_validation and b is None:  # noqa: E501
            raise ValueError("Invalid value for `b`, must not be `None`")  # noqa: E501

        self._b = b

    @property
    def g(self):
        """Gets the g of this RGBAColor.  # noqa: E501

        Green.  # noqa: E501

        :return: The g of this RGBAColor.  # noqa: E501
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this RGBAColor.

        Green.  # noqa: E501

        :param g: The g of this RGBAColor.  # noqa: E501
        :type g: int
        """
        if self.local_vars_configuration.client_side_validation and g is None:  # noqa: E501
            raise ValueError("Invalid value for `g`, must not be `None`")  # noqa: E501

        self._g = g

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
        if not isinstance(other, RGBAColor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RGBAColor):
            return True

        return self.to_dict() != other.to_dict()
