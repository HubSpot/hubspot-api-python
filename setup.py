# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "hubspot-api-client"
VERSION = "1.0.0-beta"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
TESTS_REQUIRE = ["pytest"]

setup(
    name=NAME,
    packages=find_packages(),
    version=VERSION,
    description="HubSpot API client",
    url="https://github.com/HubSpot/hubspot-api-python",
    author='HubSpot',
    author_email='support@hubspot.com',
    install_requires=REQUIRES,
    extras_require={'test': TESTS_REQUIRE},
    python_requires=">=3.4",
    include_package_data=True,
)
