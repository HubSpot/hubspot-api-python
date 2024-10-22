import pytest

from hubspot.utils.requests.http_auth import Auth


@pytest.mark.parametrize(
    "source,expected", [
        ({"auth_value": "test_value"}, True),
        ({}, False)
    ]
)
def test_has_auth_value(source, expected):
    assert Auth._has_auth_value(source) is expected


@pytest.mark.parametrize(
    "options, config, expected", [
        # Valid data in options
        ({"auth_type": "accessToken", "auth_value": "test_token"},
         {"auth_type": "hapikey", "auth_value": "test_apikey"},
         {"auth_type": "accessToken", "auth_value": "test_token"}),

        # Valid data in config, options is invalid
        ({"auth_type": "invalidType", "auth_value": None},
         {"auth_type": "hapikey", "auth_value": "test_apikey"},
         {"auth_type": "hapikey", "auth_value": "test_apikey"}),

        # Invalid data in both options and config
        ({"auth_type": "invalidType", "auth_value": None},
         {"auth_type": "invalidType", "auth_value": None},
         {"auth_type": None, "auth_value": None}),

        # auth_value missing in options, config is also not valid
        ({"auth_type": "accessToken"},
         {"auth_type": "hapikey", "auth_value": None},
         {"auth_type": None, "auth_value": None}),
    ]
)
def test_choose_auth(options, config, expected):
    result = Auth.choose_auth(options, config)
    assert result == expected
