from hubspot import HubSpot
from hubspot.marketing.emails import MarketingEmailsApi, StatisticsApi


def test_is_discoverable():
    apis = HubSpot().marketing.emails
    assert isinstance(apis.marketing_emails_api, MarketingEmailsApi)
    assert isinstance(apis.statistics_api, StatisticsApi)
