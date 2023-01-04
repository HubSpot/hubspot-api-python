import hashlib
from hubspot.exceptions import InvalidSignatureError


# @deprecated
def validate_signature(
    signature: str,
    client_secret: str,
    http_uri: str,
    request_body: str,
    http_method="POST",
    signature_version="v2",
):
    if signature_version == "v1":
        source_string = client_secret + request_body
    elif signature_version == "v2":
        source_string = client_secret + http_method + http_uri + request_body
    else:
        raise ValueError(
            "Not supported signature version: {}".format(signature_version)
        )

    hash_result = hashlib.sha256(source_string.encode("utf-8")).hexdigest()

    if hash_result != signature:
        raise InvalidSignatureError(
            signature=signature,
            signature_version=signature_version,
            hash_result=hash_result,
        )
