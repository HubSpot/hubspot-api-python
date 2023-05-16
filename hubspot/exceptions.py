class InvalidSignatureVersionError(Exception):
    def __init__(
        self, signature_version
    ):
        super().__init__(f"Invalid signature version passed to request: {signature_version}")


class InvalidSignatureTimestampError(Exception):
    def __init__(
        self, timestamp
    ):
        self.timestamp = timestamp
        super().__init__(
            f"Signature timestamp is invalid: {timestamp}."
        )
