from hubspot import HubSpot
from hubspot.marketing.transactional import PublicSmtpTokensApi, SingleSendApi


def test_is_discoverable():
    apis = HubSpot().marketing.transactional 
    assert isinstance(apis.public_smtp_tokens_api, PublicSmtpTokensApi)
    assert isinstance(apis.single_send_api, SingleSendApi)
