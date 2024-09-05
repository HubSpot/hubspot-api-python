import pytest
from datetime import datetime
from hubspot.exceptions import InvalidSignatureVersionError, InvalidSignatureTimestampError
from hubspot.utils.signature import Signature


TEST_DATA = {
    "client_secret": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
    "request_body": "{'example_field':'example_value'}",
    "url": "https://www.example.com/webhook_uri",
    "http_method": "POST",
    "timestamp": str(int(datetime.now().timestamp() * 1000)),
}


def test_get_signature__v1():
    data = {
        "signature": "69fc6631a867edd4f9e9e627fc5c1148e3fbdd8b21837b6d2b8901c1fa57f750",
        "signature_version": "v1"
    }

    result = Signature.get_signature(
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        data["signature_version"]
    )

    assert data["signature"] == result


def test_get_signature__v2():
    data = {
        "signature": "4fe4e3a7d3cf09db53be39d0a58130e2aaba074ec123a9e355b876a689a1c383",
        "signature_version": "v2"
    }

    result = Signature.get_signature(
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        data["signature_version"],
        TEST_DATA["url"]
    )

    assert data["signature"] == result


def test_get_signature__v3():
    data = {
        "signature": "K36dawei4A+QBNolUOqo7s91KQDWQ5MXZ/QufNYuk/Y=",
        "signature_version": "v3",
    }

    data.update(TEST_DATA)
    data["timestamp"] = "1693657560000"

    signature = Signature.get_signature(
        data["client_secret"],
        data["request_body"],
        data["signature_version"],
        data["url"],
        data["http_method"],
        data["timestamp"],
    )

    assert data["signature"] == signature


def test_get_signature__wrong_version():
    with pytest.raises(InvalidSignatureVersionError):
        Signature.get_signature(
            TEST_DATA["client_secret"],
            TEST_DATA["request_body"],
            "wrong_signature_version"
        )


def test_is_valid__v1():
    signature = "69fc6631a867edd4f9e9e627fc5c1148e3fbdd8b21837b6d2b8901c1fa57f750"

    result = Signature.is_valid(
        signature,
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v1"
    )

    assert result


def test_is_valid__v2():
    signature = "4fe4e3a7d3cf09db53be39d0a58130e2aaba074ec123a9e355b876a689a1c383"

    result = Signature.is_valid(
        signature,
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v2",
        http_uri=TEST_DATA["url"]
    )

    assert result


def test_is_valid__v2_get_method():
    signature = "eee2dddcc73c94d699f5e395f4b9d454a069a6855fbfa152e91e88823087200e"

    result = Signature.is_valid(
        signature,
        TEST_DATA["client_secret"],
        request_body="",
        signature_version="v2",
        http_method="GET",
        http_uri=TEST_DATA["url"]
    )

    assert result


def test_is_valid__v3():
    signature = Signature.get_signature(
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v3",
        http_uri=TEST_DATA["url"],
        timestamp=TEST_DATA["timestamp"]
    )

    result = Signature.is_valid(
        signature,
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v3",
        http_uri=TEST_DATA["url"],
        timestamp=TEST_DATA["timestamp"]
    )

    assert result


def test_is_valid__none_timestamp():
    signature = Signature.get_signature(
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v3",
        http_uri=TEST_DATA["url"]
    )

    with pytest.raises(InvalidSignatureTimestampError):
        Signature.is_valid(
            signature,
            TEST_DATA["client_secret"],
            TEST_DATA["request_body"],
            signature_version="v3",
            http_uri=TEST_DATA["url"],
            timestamp=None
        )


def test_is_valid__expired_timestamp():
    expired_timestamp = str(int((datetime.now().timestamp() - Signature.MAX_ALLOWED_TIMESTAMP - 1) * 1000))

    signature = Signature.get_signature(
        TEST_DATA["client_secret"],
        TEST_DATA["request_body"],
        signature_version="v3",
        http_uri=TEST_DATA["url"],
        timestamp=expired_timestamp
    )

    with pytest.raises(InvalidSignatureTimestampError):
        Signature.is_valid(
            signature,
            TEST_DATA["client_secret"],
            TEST_DATA["request_body"],
            signature_version="v3",
            http_uri=TEST_DATA["url"],
            timestamp=expired_timestamp
        )


def test_is_timestamp_valid__valid_timestamp():
    current_timestamp = str(int(datetime.now().timestamp() * 1000))

    assert Signature._is_timestamp_valid(current_timestamp) is True


def test_is_timestamp_valid__expired_timestamp():
    expired_timestamp = str(int((datetime.now().timestamp() - Signature.MAX_ALLOWED_TIMESTAMP - 10) * 1000))

    assert Signature._is_timestamp_valid(expired_timestamp) is False
