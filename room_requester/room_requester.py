from entry_handler.entry_fetcher import get_new_entries
from entry_handler.entry import Entry

while True:
    new_entries = get_new_entries()
    if new_entries:
        for url in new_entries:
            # get attributes of entry
            # find matching users in database
            # send request from every matching user
            entry = Entry(url)
            entry.print_entry()
