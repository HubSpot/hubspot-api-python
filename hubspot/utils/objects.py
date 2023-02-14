PAGE_MAX_SIZE = 100


def fetch_all(get_page_api_client, **kwargs):
    results = []
    after = None
    if not kwargs.get("limit"):
        kwargs["limit"] = PAGE_MAX_SIZE

    while True:
        page = get_page_api_client.get_page(after=after, **kwargs)
        results.extend(page.results)
        if page.paging is None:
            break
        after = page.paging.next.after

    return results
