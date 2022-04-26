"""Main module that runs the application."""

from entry_handler import entry_fetcher
from entry_handler import entry

while True:
    new_entry_urls = entry_fetcher.get_new_entry_urls()
    if new_entry_urls:
        for new_entry_url in new_entry_urls:
            new_entry = entry.Entry(new_entry_url)
            new_entry.send_requests()
            new_entry.print_entry()
