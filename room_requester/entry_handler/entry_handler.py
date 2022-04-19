import requests
import re
from entry_request import cookies, headers, data


def save_entry_list(entries):
    with open('entry_list.txt', 'w') as file:
        for entry in entries:
            file.write(f"{entry}\n")


def read_entry_list():
    with open('entry_list.txt') as file:
        entry_list = file.readlines()

    return [entry.rstrip("\n") for entry in entry_list]


def get_current_entry_list():
    response = requests.post('https://www.wgzimmer.ch/wgzimmer/search/mate.html?',
                             headers=headers, cookies=cookies, data=data)

    entry_regex = "/de/wgzimmer/search/mate/ch/\S+.html"
    entry_list = re.findall(entry_regex, response.text)
    return [f"https://www.wgzimmer.ch{entry}" for entry in entry_list]


def find_new_entries(new_list, old_list):
    return [entry for entry in new_list if entry not in old_list]


def get_new_entries():
    stored_list = read_entry_list()
    current_list = get_current_entry_list()
    new_entries = find_new_entries(current_list, stored_list)
    if new_entries:
        save_entry_list(current_list)

    return new_entries
