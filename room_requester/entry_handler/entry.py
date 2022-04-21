import requests
import re
from lxml import html
import pyppeteer

xpath_move_in = '//*[@id="content"]/div[5]/div[2]/p[1]'
xpath_unlimited = '//*[@id="content"]/div[5]/div[2]/p[2]'
xpath_price = '//*[@id="content"]/div[5]/div[2]/p[3]'
xpath_address = '//*[@id="content"]/div[5]/div[3]/p[2]'
xpath_location = '//*[@id="content"]/div[5]/div[3]/p[3]'


class Entry:
    def __init__(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        self.url = url
        self.move_in = tree.xpath(xpath_move_in)[0].text_content()[8:]
        self.unlimited = bool(tree.xpath(xpath_unlimited)[
                              0].text_content()[4:] == "Unbefristet")
        self.price = int(re.findall(
            "\d+", tree.xpath(xpath_price)[0].text_content())[0])
        self.street = self.get_street(tree.xpath(xpath_address)
                                      [0].text_content()[9:])
        self.house_number = self.get_house_number(
            tree.xpath(xpath_address)[0].text_content())
        self.postal_code = int(re.findall(
            "\d+", tree.xpath(xpath_location)[0].text_content())[0])
        self.location = self.get_location(
            tree.xpath(xpath_location)[0].text_content())

    def get_house_number(self, content):
        number = re.findall("\d+", content)
        if len(number) > 0:
            return int(number[0])
        else:
            return False

    def get_street(self, content):
        street = re.findall(".+?\d", content)
        if len(street) > 0:
            return street[0][:-2]
        else:
            return ""

    def get_location(self, content):
        location = re.findall("\d (.*)", content)
        if len(location) > 0:
            return location[0]
        else:
            return ""

    def print_entry(self):
        print(f"URL: {self.url}")
        print(f"Move_in: {self.move_in}")
        print(f"Unlimited: {self.unlimited}")
        print(f"Price: {self.price}")
        print(f"Location: {self.location}")
        print(f"Postal Code: {self.postal_code}")
        print(f"Street: {self.street}")
        print(f"House_number: {self.house_number}")

    def get_matching_users(self):
        return []

    def send_request_from_user(self, user):
        print(f"{user.name} sent request to entry: {self.url}")

    def send_request_from_all_matching_profiles(self):
        matching_users = self.get_matching_profiles()
        if matching_users:
            for user in matching_users:
                self.send_request_from_user(user)
