from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from hubspot.utils.objects import fetch_all


def test_zero_limit_does_not_fetch():
    client = Mock()
    client.get_page.return_value = SimpleNamespace(results=[1], paging=None)
    assert fetch_all(client, limit=0) == []
    client.get_page.assert_not_called()


def test_negative_limit_does_not_fetch():
    client = Mock()
    client.get_page.return_value = SimpleNamespace(results=[1], paging=None)
    with pytest.raises(ValueError, match="limit"):
        fetch_all(client, limit=-1)
    client.get_page.assert_not_called()


@pytest.mark.parametrize("limit", [None, 101])
def test_multiple_pages(limit):
    client = Mock()
    client.get_page.side_effect = [
        SimpleNamespace(
            results=list(range(100)),
            paging=SimpleNamespace(next=SimpleNamespace(after="next")),
        ),
        SimpleNamespace(results=[100], paging=None),
    ]
    assert fetch_all(client, limit=limit) == list(range(101))
    assert client.get_page.call_args_list[0].kwargs == {"after": None, "limit": 100}
    assert client.get_page.call_args_list[1].kwargs == {
        "after": "next",
        "limit": 1 if limit else 100,
    }
