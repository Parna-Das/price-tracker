"""File to house all the `Helper` functions"""

from datetime import datetime, timedelta
import time
import requests
import logging
from audioplayer import AudioPlayer
from bs4 import BeautifulSoup as bs
from pathlib import Path
from constants.constants import HEADERS
from constants.filepaths import NOTIFICATION_FILE
import sys


def confirm_product(url: str) -> bool:
    name, current_price, availability = resolve_url(url)
    choice = input(f"Confirm the following product details\n{name}\n{current_price}\n{availability}\n Press Y to continue")
    return bool(choice.lower() == "Y")


def start_tracking(url:str, target_price : float, frequency : int = 1, timeout: int = 24) -> bool:
    start_time = datetime.now()
    timeout_at = start_time+timedelta(hours =timeout)
    while datetime.now() <= timeout_at:
        name, current_price, availability = resolve_url(url)
        if current_price <= target_price:
            logging.info("Target price reached. \n Current price is at %s",current_price)
            print(f"Target price reached. \n Current price is at {current_price}")
            return True
        logging.info("Waiting for - '%s' minutes", frequency)
        time.sleep(frequency*60)
    logging.warning("Triggering timeout of - '%s' hours", timeout)
    return False


def trigger_notification(file_path : Path = NOTIFICATION_FILE) -> None:
    logging.info("Attempting to play notification sound using file - '%s'", file_path)
    AudioPlayer(str(file_path)).play(block=True)
    logging.info("Successfuly notified user using file - '%s'", file_path)


def tear_down():
    sys.exit(0)


def resolve_url(url: str) -> tuple[str, float, str]:
    response = requests.get(url=url, headers=HEADERS, timeout=30)
    if response.status_code == 200:
        html_content = bs(response.content, "html.parser") 
        return (
                html_content.find("span", {"id": "productTitle", "class": "a-size-large product-title-word-break"}).text.strip(),
                float(html_content.find("span",{"class":"a-price-whole"}).text.strip()[:-1]), 
                html_content.find("span", {"class": "a-size-medium a-color-success"}).text.strip()
                )
    logging.error("Failed to resolve URL with status code of - %s ", response.status_code)
    raise KeyboardInterrupt


if __name__ == "__main__":
    resolve_url(
        "https://www.amazon.in/Samsung-Galaxy-Smartphone-Olive-Green/dp/B0C1Z8WTS6/ref=sr_1_1?_encoding=UTF8&s=electronics&sr=1"
    )
