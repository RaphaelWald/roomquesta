"""This module defines the Entry-Class, that handles new entry-url by extracting important data."""

import requests
import re
from lxml import html
from user import User

MOVE_IN_XPATH = '//*[@id="content"]/div[5]/div[2]/p[1]'
UNLIMITED_XPATH = '//*[@id="content"]/div[5]/div[2]/p[2]'
PRICE_XPATH = '//*[@id="content"]/div[5]/div[2]/p[3]'
REGION_XPATH = '//*[@id="content"]/div[5]/div[3]/p[1]'
ADDRESS_XPATH = '//*[@id="content"]/div[5]/div[3]/p[2]'
LOCATION_XPATH = '//*[@id="content"]/div[5]/div[3]/p[3]'


class Entry:
    """Stores entry properties and sends requests from matching users.

    This class has two main functions:
        1. Page Content
            - request page content
            - extract important information based on page content
            - store information in properties
        2. Request sending
            - Find matching users
            - Send requests to entry from all matching users

    Attributes:
        url: URL of the entry.
        page: Response to GET-Request for 'url'.
        tree: HTML tree based on the page content.
        move_in: Earliest move-in date.
        move_out: Move-out date if not unlimited.
        unlimited: True if there is no move_out date.
        price: Monthly rental fee in CHF.
        region: Closer environment.
        house_number:
        postal_code:
        location: City to corresponding postal_code

    Public methods:
        update: Reinitializes entry properties after requesting current page content.
        print_entry: Prints out all entry properties in human readable format.
        send_requests: Finds all matching users and sends requests for them.
    """

    def __init__(self, url):
        """Initializes the attributes based on the received page content."""
        self.url: str = url
        self.page: requests.models.Response = requests.get(url)
        self.tree: html.HtmlElement = html.fromstring(self.page.content)
        self.move_in: str = self._get_move_in()
        self.move_out: str = self._get_move_out()
        self.unlimited: str = bool(self.move_out == "Unbefristet")
        self.price: int = self._get_price()
        self.region: str = self._get_region()
        self.house_number: int = self._get_house_number()
        self.street: str = self._get_street()
        self.postal_code: int = self._get_postal_code()
        self.location: str = self._get_location(
        )

    def update(self) -> None:
        """Requests page content and reinitializes entry properties."""
        self.__init__(self, self.url)

    def print_entry(self) -> None:
        """Prints all properties of Entry-instance."""
        print(f"URL: {self.url}")
        print(f"Move_in: {self.move_in}")
        print(f"Unlimited: {self.unlimited}")
        print(f"Price: {self.price}")
        print(f"Region: {self.region}")
        print(f"Location: {self.location}")
        print(f"Postal Code: {self.postal_code}")
        print(f"Street: {self.street}")
        print(f"House_number: {self.house_number}")

    def send_requests(self) -> bool:
        """Gets all matching users and tries to sent a request from each of them."""
        matching_users = self._get_matching_users()
        if matching_users:
            for user in matching_users:
                self._send_request_from_user(user)

    def _get_matching_users(self) -> list[User]:
        """Returns list of users whose criteria matches the properties of this entry"""
        return []

    def _send_request_from_user(self, user: User) -> bool:
        """Tries to send request from specified user and returns whether sending was successful."""
        print(f"{user.name} sent request to entry: {self.url}")
        return True

    def _get_move_in(self) -> str:
        html_element = self.tree.xpath(MOVE_IN_XPATH)[0]
        content = html_element.text_content()
        move_in_date = content[8:]
        return move_in_date

    def _get_move_out(self) -> str:
        html_element = self.tree.xpath(UNLIMITED_XPATH)[0]
        content = html_element.text_content()
        move_out_date = content[4:]
        return move_out_date

    def _get_price(self) -> int:
        html_element = self.tree.xpath(PRICE_XPATH)[0]
        content = html_element.text_content()
        price = re.findall("\d+", content)[0]
        return int(price)

    def _get_region(self) -> str:
        html_element = self.tree.xpath(REGION_XPATH)[0]
        content = html_element.text_content()
        region = content[8:]
        return region

    def _get_house_number(self) -> int:
        html_element = self.tree.xpath(ADDRESS_XPATH)[0]
        content = html_element.text_content()[9:]
        number = re.findall("\d+", content)
        if number:
            return int(number[0])
        else:
            return False

    def _get_street(self) -> str:
        html_element = self.tree.xpath(ADDRESS_XPATH)[0]
        content = html_element.text_content()[9:]
        street = re.findall(".+?\d", content)
        if street:
            return street[0][:-2]
        else:
            return ""

    def _get_postal_code(self) -> int:
        html_element = self.tree.xpath(LOCATION_XPATH)[0]
        content = html_element.text_content()
        postal_code = re.findall("\d+", content)[0]
        return int(postal_code)

    def _get_location(self) -> str:
        html_element = self.tree.xpath(LOCATION_XPATH)[0]
        content = html_element.text_content()
        location = re.findall("\d (.*)", content)
        if location:
            return location[0]
        else:
            return ""
