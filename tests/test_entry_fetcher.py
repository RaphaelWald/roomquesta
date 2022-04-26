# from roomquesta.entry_handler import entry_fetcher
import roomquesta.entry_handler.entry_fetcher as entry_fetcher


def test_should_find_new_list_elements():
    list1 = ["test1", "test2", "test3"]
    list2 = ["test2", "test3"]
    entry_urls = entry_fetcher._find_new_entry_urls(list1, list2)

    assert entry_urls == ["test1"]
