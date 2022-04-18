import requests
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from entry_handler import get_new_entries

""" driver = webdriver.Chrome()
driver.get("https://www.google.de")
driver.close() """


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


while True:
    new_entries = get_new_entries()
    if new_entries:
        for entry in new_entries:
            print(f"[{get_current_time()}] New Entry: {entry}")
