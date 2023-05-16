import base64
import hmac
import hashlib

from datetime import datetime

from hubspot.exceptions import InvalidSignatureVersionError, InvalidSignatureTimestampError


class Signature:
    MAX_ALLOWED_TIMESTAMP = 3000

    @staticmethod
    def is_valid(
        signature: str,
        client_secret: str,
        request_body: str,
        http_uri: str = None,
        http_method: str = "POST",
        signature_version: str = "v2",
        timestamp: float = None
    ) -> bool:
        if signature_version == "v3":
            current_time = datetime.now()
            if timestamp is None or current_time.timestamp() - timestamp > Signature.MAX_ALLOWED_TIMESTAMP:
                raise InvalidSignatureTimestampError(timestamp=timestamp)
        hashed_signature = Signature.get_signature(
            client_secret,
            request_body,
            signature_version,
            http_uri,
            http_method,
            timestamp
        )

        return signature == hashed_signature

    @staticmethod
    def get_signature(
        client_secret: str,
        request_body: str,
        signature_version: str,
        http_uri: str = None,
        http_method: str = "POST",
        timestamp: float = None,
    ) -> str:
        if signature_version == "v1":
            source_string = f"{client_secret}{request_body}"
            return hashlib.sha256(source_string.encode("utf-8")).hexdigest()
        elif signature_version == "v2":
            source_string = f"{client_secret}{http_method}{http_uri}{request_body}"
            return hashlib.sha256(source_string.encode("utf-8")).hexdigest()
        elif signature_version == "v3":
            source_string = f"{http_method}{http_uri}{request_body}{timestamp}"
            hashed_signature = base64.b64encode(
                hmac.new(
                        client_secret.encode("utf-8"),
                        msg=source_string.encode("utf-8"),
                        digestmod=hashlib.sha256
                        ).digest()
            ).decode()
            return hashed_signature
        else:
            raise InvalidSignatureVersionError(signature_version=signature_version)
