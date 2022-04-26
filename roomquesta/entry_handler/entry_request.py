"""This module defines the specific COOKIES, HEADERS and DATA to fetch the entry page from wgzimmer.ch"""

COOKIES = {
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

HEADERS = {
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

DATA = {
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
