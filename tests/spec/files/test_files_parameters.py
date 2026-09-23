import os
import tempfile
from io import BytesIO

from hubspot.files.api_client import ApiClient


def test_files_parameters_accepts_path_bytes_and_file_object():
    client = ApiClient()
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as handle:
        handle.write(b"from disk")
        path = handle.name
    try:
        from_path = client.files_parameters({"file": path})
        assert from_path[0][1][1] == b"from disk"
        assert from_path[0][1][0] == os.path.basename(path)
    finally:
        os.remove(path)

    from_bytes = client.files_parameters({"file": b"from memory"})
    assert from_bytes[0][1][1] == b"from memory"

    named = BytesIO(b"from buffer")
    named.name = "notes.txt"
    from_buffer = client.files_parameters({"file": named})
    assert from_buffer[0][1] == ("notes.txt", b"from buffer", "text/plain")
