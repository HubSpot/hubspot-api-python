
def fetch_all(get_page_api_client, **kwargs):
    results = []
    after = 0
    while True:
        page = get_page_api_client.get_page(after=after, limit=100, **kwargs)
        results.extend(page.results)
        if page.paging is None:
            break
        after = page.paging.next.after

    return results
