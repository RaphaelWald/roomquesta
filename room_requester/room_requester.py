import sqlite3

from datetime import datetime

from entry_handler.entry_handler import get_new_entries


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


while True:
    new_entries = get_new_entries()
    if new_entries:
        for entry in new_entries:
            print(f"[{get_current_time()}] New Entry: {entry}")
