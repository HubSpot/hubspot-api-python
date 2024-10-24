import pytest
import json
from unittest.mock import patch
import requests

from hubspot.utils.requests.http_request_builder import Request

BASE_PATH = "/contacts/v1/contact"

COMMON_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "custom-python-client/1.0",
    "Accept": "application/json, */*;q=0.8"
}


@pytest.fixture
def config():
    return {
        "access_token": "test_access_token",
        "api_key": "test_api_key"
    }


@pytest.fixture
def options():
    return {
        "method": "POST",
        "path": BASE_PATH,
        "qs": {"param1": "value1"},
        "body": {"key": "value"}
    }


@pytest.mark.parametrize(
    "options, config, expected_url, expected_headers",
    [
        (
            {
                "path": BASE_PATH,
                "auth_type": "api_key",
            },
            {
                "api_key": "test_api_key",
            },
            f"https://api.hubapi.com{BASE_PATH}?hapikey=test_api_key",
            COMMON_HEADERS
        ),
        (
            {
                "path": BASE_PATH,
                "auth_type": "access_token",
            },
            {
                "access_token": "test_access_token",
                "api_key": "test_api_key"
            },
            f"https://api.hubapi.com{BASE_PATH}",
            {
                **COMMON_HEADERS,
                "Authorization": "Bearer test_access_token"
            }
        ),
    ]
)
def test_generate_url(options, config, expected_url, expected_headers):
    req = Request(config, options)
    assert req.get_url() == expected_url
    assert req.headers == expected_headers


@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "DELETE"])
def test_http_methods(config, method):
    options = {
        "method": method,
        "path": BASE_PATH
    }
    req = Request(config, options)
    assert req.method == method


def test_body_serialization_dict(config):
    options = {
        "body": {"key": "value"}
    }
    req = Request(config, options)
    expected_body = json.dumps({"key": "value"})
    assert req.body == expected_body


def test_body_serialization_list(config):
    options = {
        "body": [{"key": "value"}]
    }
    req = Request(config, options)
    expected_body = json.dumps([{"key": "value"}])
    assert req.body == expected_body


def test_body_string(config):
    options = {
        "body": "raw_string_data"
    }
    req = Request(config, options)
    assert req.body == "raw_string_data"


def test_empty_body(config):
    options = {
        "body": {}
    }
    req = Request(config, options)
    assert req.body == "{}"


@patch("requests.post")
def test_request_exception_handling(mock_post, config, options):
    mock_post.side_effect = requests.exceptions.RequestException("Test exception")

    req = Request(config, options)

    with pytest.raises(requests.exceptions.RequestException):
        req.send()


def test_headers_initialization(config, options):
    req = Request(config, options)
    assert req.headers["Content-Type"] == "application/json"
    assert req.headers["User-Agent"] == "custom-python-client/1.0"
