from hubspot import HubSpot
from hubspot.cms.hubdb import RowsApi, RowsBatchApi, TablesApi


def test_is_discoverable():
    apis = HubSpot().cms.hubdb
    assert isinstance(apis.rows_api, RowsApi)
    assert isinstance(apis.rows_batch_api, RowsBatchApi)
    assert isinstance(apis.tables_api, TablesApi)
