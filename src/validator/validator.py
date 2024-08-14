""""File to house all the `validator` files"""

import logging
from subprocess import run, DEVNULL
from constants.constants import TEST_INTERNET_CONNECTION, URL_REGEX


def is_url_valid(url: str) -> bool:
    """Method to validate the URL given by user

    Args:
        url (str): provided URL

    Returns:
        bool: True or False based on action
    """
    status = bool(URL_REGEX.match(url))
    logging.info("Valid url received - '%s'", url) if status else logging.error("Invalid url received - '%s'", url)
    return status


def is_frequency_valid(frequency: int) -> bool:
    """Method to validate the input's data type

    Args:
        frequency (int): Frequency given by user

    Returns:
        bool: True or False based on action
    """
    status = bool(1 <= frequency <= 60)
    logging.info("Valid frequency received") if status else logging.error("Invalid frequency received")
    return status


def is_target_price_valid(price: float) -> bool:
    """Method to validate the input's data type

    Args:
        price (float): Target price given by user

    Returns:
        bool: True or False based on action
    """
    status = bool(price > 0)
    logging.info("Valid price received") if status else logging.error("Invalid price received")
    return status


def is_timeout_valid(timeout: int) -> bool:
    """Method to validate the input's data type

    Args:
        timeout (int): Timeout given by user

    Returns:
        bool: True or False based on action
    """
    status = bool(0 < timeout <= 24)
    logging.info("Valid timeout received") if status else logging.error("Invalid timeout received")
    return status


def is_internet_available() -> bool:
    """Method to check internet connection

    Returns:
        bool: True or False based on action
    """
    status = not bool(run(TEST_INTERNET_CONNECTION, shell=True, check=True, stdout=DEVNULL, stderr=DEVNULL).returncode)
    logging.info("Internet is available") if status else logging.error("No internet connection")
    return status
