"""File to house all the `Helper` functions"""

import logging
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
import requests
import urllib3
from audioplayer import AudioPlayer
from bs4 import BeautifulSoup as bs
from constants.constants import HEADERS
from constants.filepaths import NOTIFICATION_FILE

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def confirm_product(url: str) -> bool:
    """Method to confirm product from the user

    Args:
        url (str): URL provided by the user

    Returns:
        bool: True or False based on action
    """
    logging.info("Triggering User confirmation")
    name, current_price, availability = resolve_url(url)
    logging.info("Showing User Confirmation prompt")
    choice = input(f"Confirm the following product details\nProduct Name - {name}\nProduct Price - {current_price}\nProduct Status - {availability}\nPress Y to continue : ")
    status = bool(choice.lower() == "y")
    if status:
        logging.info("User opted to proceed")
    else:
        logging.error("User requested abort")
        print("User confirmation - Declined")
        print("Please Check your product URL and Try Again")
    return status


def start_tracking(url: str, target_price: float, frequency: int = 1, timeout: int = 24) -> bool:
    """Method to start tracking of the product

    Args:
        url (str): URL provided by the user
        target_price (float): Targeted price given by user
        frequency (int, optional): Frequency given by user
        timeout (int, optional): Timeout given by user

    Returns:
        bool: True or False based on action
    """
    print("Product Tracking In-Progress!!")
    start_time = datetime.now()
    timeout_at = start_time + timedelta(hours=timeout)
    logging.info("Initializing Tracking at time - '%s'", start_time)
    logging.info("Tracing Timeout shall be triggered at - '%s'", timeout_at)
    try:
        while datetime.now() <= timeout_at:
            _, current_price, *_ = resolve_url(url)
            logging.info("Current Price retrieved as - '%s' against Target price - '%s'", current_price, target_price)
            if current_price <= target_price:
                logging.info("Target price reached. \n Current price is at %s", current_price)
                print(f"Target price reached!!\nCurrent price is at {current_price}")
                return True
            logging.info("Waiting for - '%s' minutes", frequency)
            time.sleep(frequency * 60)
    except KeyboardInterrupt:
        logging.warning("Keyboard Interrupt Intercepted, Triggering exit confirmation")
        choice = input("Keyboard interrupt detected!!!\nAre you sure you want to exit?\nPress 'Y' to exit, Press any key to continue : ")
        if choice.lower() != "y":
            logging.info("User opted to continue.. Tracking Restarted")
            return start_tracking(url, target_price, frequency, timeout)
    logging.warning("Triggering timeout of - '%s' hours", timeout)
    return False


def trigger_notification(file_path: Path = NOTIFICATION_FILE) -> None:
    """Method to trigger notification to user

    Args:
        file_path (Path, optional): File path to pick up the audio file
    """
    logging.info("Attempting to play notification sound using file - '%s'", file_path)
    AudioPlayer(str(file_path)).play(block=True)
    logging.info("Successfully notified user using file - '%s'", file_path)


def tear_down():
    """Method to exit from the application
    """
    print("Exiting Gracefully...")
    print("Thanks for using `Price Tracker`")
    sys.exit(0)


def resolve_url(url: str) -> tuple[str, float, str]:
    """Method to process url and other user inputs

    Args:
        url (str): URL provided by the user

    Raises:
        KeyboardInterrupt: Interruption for unwanted events

    Returns:
        tuple[str, float, str]: Tuple consists of product name, price and availability
    """
    response = requests.get(url=url, headers=HEADERS, timeout=10, verify=False)
    if response.status_code == 200:
        logging.info("URL - '%s' resolved with status code 200", url)
        html_content = bs(response.content, "html.parser")
        logging.debug("HTML Content received as \n%s", html_content)
        name = html_content.find("span", {"id": "productTitle", "class": "a-size-large product-title-word-break"}).text.strip()
        price = html_content.find("span", {"class": "a-price-whole"}).text.strip()[:-1]
        availability = html_content.find("span", {"class": "a-size-medium a-color-success"}).text.strip()
        logging.info("Name - '%s', Price - '%s', Availability - '%s'", name, price, availability)

        return (name, float(price.replace(",", "")), availability)
    logging.error("Failed to resolve URL with status code of - %s ", response.status_code)
    raise KeyboardInterrupt