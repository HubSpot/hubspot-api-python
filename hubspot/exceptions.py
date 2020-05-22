class InvalidSignatureError(Exception):
    def __init__(
        self, msg=None, signature=None, signature_version=None, hash_result=None
    ):
        self.signature = signature
        self.signature_version = signature_version
        self.hash_result = hash_result
        if msg is None:
            msg = "Invalid signature passed to request"
        super(InvalidSignatureError, self).__init__(msg)
