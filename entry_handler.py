import requests
import re

cookies = {
    'adnzVisitorId': '3478750464785655052',
    'adnzVisitorId': '3478750464785655052',
    'wc_language': 'de',
    'wc_currencyLocale': 'de_CH',
    'wc_color': 'babyblue',
    'wc_email': '"info@wgzimmer.ch"',
    'wc_currencySign': 'sFr.',
    '_ga': 'GA1.2.623226590.1649932887',
    'adnzVisitorId': '3478750464785655052',
    '__gads': 'ID=adcc2a67e676ffb8:T=1649932877:S=ALNI_MZLY38p4hJa9eMjAJbjtU3yOLfBJg',
    'JSESSIONID': '6B6B0389EA531FDFD67E4AF4BC26F632',
    '_gid': 'GA1.2.1649645174.1650292202',
    '__gpi': 'UID=000004c4910cdeab:T=1649932877:RT=1650292184:S=ALNI_MbUYN1HJ2H-LhAs1C7AVcvn7qPOLQ',
    'bclk': '6752371182556125',
}

headers = {
    'authority': 'www.wgzimmer.ch',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'adnzVisitorId=3478750464785655052; adnzVisitorId=3478750464785655052; wc_language=de; wc_currencyLocale=de_CH; wc_color=babyblue; wc_email="info@wgzimmer.ch"; wc_currencySign=sFr.; _ga=GA1.2.623226590.1649932887; adnzVisitorId=3478750464785655052; __gads=ID=adcc2a67e676ffb8:T=1649932877:S=ALNI_MZLY38p4hJa9eMjAJbjtU3yOLfBJg; JSESSIONID=6B6B0389EA531FDFD67E4AF4BC26F632; _gid=GA1.2.1649645174.1650292202; __gpi=UID=000004c4910cdeab:T=1649932877:RT=1650292184:S=ALNI_MbUYN1HJ2H-LhAs1C7AVcvn7qPOLQ; bclk=6752371182556125',
    'origin': 'https://www.wgzimmer.ch',
    'referer': 'https://www.wgzimmer.ch/wgzimmer/search/mate.html',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
}

data = {
    'query': '',
    'priceMin': '200',
    'priceMax': '1500',
    'state': 'all',
    'permanent': 'all',
    'student': 'none',
    'typeofwg': 'all',
    'orderBy': '@sortDate',
    'orderDir': 'descending',
    'startSearchMate': 'true',
    'wgStartSearch': 'true',
    'start': '0',
}


def save_entry_list(entries):
    with open('fetch.txt', 'w') as f:
        for entry in entries:
            f.write(f"{entry}\n")


def read_entry_list():
    with open("fetch.txt") as file:
        lines = file.readlines()
    entry_list = []
    for line in lines:
        entry_list.append(line.rstrip("\n"))
    return entry_list


def get_current_entry_list():
    response = requests.post('https://www.wgzimmer.ch/wgzimmer/search/mate.html?',
                             headers=headers, cookies=cookies, data=data)

    entry_regex = "/de/wgzimmer/search/mate/ch/\S+.html"
    entries = re.findall(entry_regex, response.text)

    new_entries = []
    for entry in entries:
        entry_url = f"https://wg.zimmer.ch{entry}"
        new_entries.append(entry_url)
    return new_entries


def find_different_entries(new_list, old_list):
    new_entries = []
    for entry in new_list:
        if entry not in old_list:
            new_entries.append(entry)
    return new_entries


def get_new_entries():
    stored_list = read_entry_list()
    current_list = get_current_entry_list()
    new_entries = find_different_entries(current_list, stored_list)
    if new_entries:
        save_entry_list(current_list)

    return new_entries
