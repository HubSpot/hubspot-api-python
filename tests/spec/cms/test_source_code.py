from hubspot import HubSpot
from hubspot.cms.source_code import ContentApi, ExtractApi, MetadataApi, SourceCodeExtractApi, ValidationApi 


def test_is_discoverable():
    apis = HubSpot().cms.source_code
    assert isinstance(apis.content_api, ContentApi)
    assert isinstance(apis.extract_api, ExtractApi)
    assert isinstance(apis.metadata_api, MetadataApi)
    assert isinstance(apis.source_code_extract_api, SourceCodeExtractApi)
    assert isinstance(apis.validation_api, ValidationApi)
