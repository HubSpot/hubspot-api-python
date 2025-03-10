import pytest

from hubspot.utils.requests.http_auth import Auth


@pytest.mark.parametrize(
    "source,key,expected", [
        ({"auth_value": "test_value"}, "auth_value", True),
        ({}, "key", False)
    ]
)
def test_has_auth_value(source, key, expected):
    assert Auth._has_auth_value(source, key) is expected


@pytest.mark.parametrize(
    "config, options, expected", [
        # Valid data in options
        ({"access_token": "test_api_key"},
         {"auth_type": "access_token"},
         {"auth_type": "access_token"}),

        # Valid data in config, options is invalid
        ({"api_key": "test_api_key"},
         {"auth_type": "access_token"},
         {"auth_type": "api_key"}),

        # Invalid data in both options and config
        ({"invalid_type": None},
         {"auth_type": "invalid_type"},
         {"auth_type": None}),

        # auth_value missing in options, config is also not valid
        ({"api_key": None},
         {"auth_type": "access_token"},
         {"auth_type": None}),
    ]
)
def test_choose_auth(config, options, expected):
    result = Auth.choose_auth(config, options)
    assert result == expected
