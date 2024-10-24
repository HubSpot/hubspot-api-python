PAGE_MAX_SIZE = 100
PROPERTY_HISTORY_MAX_SIZE = 50


def fetch_all(get_page_api_client, **kwargs):
    results = []
    after = None

    max_page_size = PROPERTY_HISTORY_MAX_SIZE if "properties_with_history" in kwargs else PAGE_MAX_SIZE
    limit = kwargs.pop("limit", None)
    total_fetched = 0

    while True:
        limit_for_current_page = min(max_page_size, limit - total_fetched) if limit else max_page_size
        page = get_page_api_client.get_page(after=after, limit=limit_for_current_page, **kwargs)

        results.extend(page.results)
        total_fetched += len(page.results)

        if limit and total_fetched >= limit:
            break

        if page.paging is None or page.paging.next is None:
            break

        after = page.paging.next.after

    return results
