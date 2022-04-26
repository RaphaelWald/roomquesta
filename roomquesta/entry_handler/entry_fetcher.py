"""This module implements the functionality to find new entries/entry urls by comparing the urls.

    Public functions:
        get_new_entry_urls: Returns new urls that belong to entries on wgzimmer.ch
"""

import requests
import re
import sqlite3
from entry_request import COOKIES, HEADERS, DATA


def get_new_entry_urls() -> list[str]:
    """Returns new urls that belong to entries on wgzimmer.ch

       This function compares the stored urls to the newly fetched urls and
       returns any new urls.
    """
    stored_url_list = _read_entry_url_list()
    current_url_list = _get_current_entry_url_list()
    new_entry_urls = _find_new_entry_urls(current_url_list, stored_url_list)
    if new_entry_urls:
        _save_entry_url_list(current_url_list)

    return new_entry_urls


def _read_entry_url_list() -> list[str]:
    con = sqlite3.connect('databases/entry.db')
    c = con.cursor()
    c.execute("SELECT * FROM links")
    entry_list = c.fetchall()
    con.commit()
    con.close()

    return [entry[0] for entry in entry_list]


def _get_current_entry_url_list() -> list[str]:
    response = requests.post('https://www.wgzimmer.ch/wgzimmer/search/mate.html?',
                             headers=HEADERS, cookies=COOKIES, data=DATA)

    entry_url_regex = "/de/wgzimmer/search/mate/ch/\S+.html"
    entry_url_list = re.findall(entry_url_regex, response.text)
    return [f"https://www.wgzimmer.ch{entry_url}" for entry_url in entry_url_list]


def _find_new_entry_urls(new_list: list[str], old_list: list[str]) -> list[str]:
    return [entry_url for entry_url in new_list if entry_url not in old_list]


def _save_entry_url_list(entry_urls: list[str]) -> None:
    con = sqlite3.connect('databases/entry.db')
    c = con.cursor()
    c.execute("DROP TABLE IF EXISTS links")
    c.execute("CREATE TABLE links (Link text not null)")
    for entry_url in entry_urls:
        c.execute(f"INSERT INTO links VALUES ('{entry_url}')")
    con.commit()
    con.close()
