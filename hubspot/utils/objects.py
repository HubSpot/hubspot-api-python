PAGE_MAX_SIZE = 100


def fetch_all(get_page_api_client, **kwargs):
    results = []
    after = None

    while True:
        page = get_page_api_client.get_page(after=after, limit=PAGE_MAX_SIZE, **kwargs)
        results.extend(page.results)
        if page.paging is None:
            break
        after = page.paging.next.after

    return results
