from hubspot import HubSpot
from hubspot.files import FilesApi, FoldersApi


def test_is_discoverable():
    apis = HubSpot().files
    assert isinstance(apis.files_api, FilesApi)
    assert isinstance(apis.folders_api, FoldersApi)
