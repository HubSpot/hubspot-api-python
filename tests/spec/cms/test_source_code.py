from hubspot import HubSpot
from hubspot.cms.source_code import ContentApi, ExtractApi, MetadataApi, ValidationApi


def test_is_discoverable():
    apis = HubSpot().cms.source_code
    assert isinstance(apis.content_api, ContentApi)
    assert isinstance(apis.extract_api, ExtractApi)
    assert isinstance(apis.metadata_api, MetadataApi)
    assert isinstance(apis.validation_api, ValidationApi)
