import pytest
import os
import time

from hubspot.cms.hubdb import HubDbTableV3Request
from hubspot.cms.hubdb.exceptions import NotFoundException


HUB_DB_TABLE_REQUEST = HubDbTableV3Request(
    name="test_table",
    label="Test Table",
    use_for_pages=True,
    allow_public_api_access=False,
    allow_child_tables=True,
    enable_child_table_pages=False,
    columns=[
        {
            "name": "text_column",
            "label": "Text Column",
            "id": "1",
            "type": "TEXT"
        }
    ],
    dynamic_meta_tags={}
)


@pytest.fixture
def get_or_create_table(api_client):
    try:
        table = api_client.cms.hubdb.tables_api.get_table_details(
            table_id_or_name=HUB_DB_TABLE_REQUEST.name
        )
    except NotFoundException:
        table = api_client.cms.hubdb.tables_api.create_table(HUB_DB_TABLE_REQUEST)

    time.sleep(3)
    yield table

    api_client.cms.hubdb.tables_api.archive_table(table_id_or_name=table.name)


def test_hub_db__get_all_tables(api_client):
    result = api_client.cms.hubdb.tables_api.get_all_tables()

    assert result


def test_hub_db__get_or_create_table(api_client, get_or_create_table):

    assert get_or_create_table


def test_hub_db__archive_table(api_client):
    table = api_client.cms.hubdb.tables_api.create_table(HUB_DB_TABLE_REQUEST)

    result = api_client.cms.hubdb.tables_api.archive_table(table_id_or_name=table.name)

    assert result is None


def test_hub_db__get_all_draft_tables(api_client):
    result = api_client.cms.hubdb.tables_api.get_all_draft_tables()

    assert result


def test_hub_db__get_table_details(api_client, get_or_create_table):
    result = api_client.cms.hubdb.tables_api.get_table_details(table_id_or_name=get_or_create_table.name)

    assert result


def test_hub_db__export_draft_table(api_client, get_or_create_table):
    result = api_client.cms.hubdb.tables_api.export_draft_table(
        table_id_or_name=get_or_create_table.name,
        format="CSV"
    )

    assert result

    os.remove(result)


def test_hub_db__get_table_rows(api_client, get_or_create_table):
    result = api_client.cms.hubdb.rows_api.get_table_rows(table_id_or_name=get_or_create_table.name)

    assert result


def test_hub_db__unpublish_table(api_client, get_or_create_table):
    result = api_client.cms.hubdb.tables_api.unpublish_table(table_id_or_name=get_or_create_table.name)

    assert result


def test_hub_db__update_draft_table(api_client, get_or_create_table):
    HUB_DB_TABLE_REQUEST.label = "updated label"

    result = api_client.cms.hubdb.tables_api.update_draft_table(
        table_id_or_name=get_or_create_table.id,
        hub_db_table_v3_request=HUB_DB_TABLE_REQUEST
    )

    assert result
