from roomquesta.entry_handler import entry_fetcher


def test_should_find_new_list_elements():
    url1 = "https://www.wgzimmer.ch/de/wgzimmer/search/mate/ch/zurich-stadt/8-6-2022-31-agosto--600-zurich-stadt.html"
    url2 = "https://www.wgzimmer.ch/de/wgzimmer/search/mate/ch/zurich-stadt/8-6-2022-31-agosto--600-zurich-stadt.html"
    url3 = "https://www.wgzimmer.ch/de/wgzimmer/search/mate/ch/zurich-lake/24-3-2022--1250-zurich-lake.html"
    list1 = [url1, url2]
    list2 = list1 + [url3]

    urls1 = entry_fetcher._find_new_entry_urls(list1, list1)
    urls2 = entry_fetcher._find_new_entry_urls(list1, list2)
    urls3 = entry_fetcher._find_new_entry_urls(list2, list1)
    urls4 = entry_fetcher._find_new_entry_urls(list1, [])

    assert urls1 == []
    assert urls2 == []
    assert urls3 == [url3]
    assert urls4 == list1
