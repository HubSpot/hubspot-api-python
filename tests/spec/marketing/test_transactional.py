from hubspot import HubSpot
from hubspot.marketing.transactional import PublicSMTPTokensApi, SingleSendApi


def test_is_discoverable():
    apis = HubSpot().marketing.transactional
    assert isinstance(apis.public_smtp_tokens_api, PublicSMTPTokensApi)
    assert isinstance(apis.single_send_api, SingleSendApi)
