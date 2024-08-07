""""File to house all the `validator` files"""

import os
from constants.constants import TEST_INTERNET_CONNECTION, URL_REGEX


def is_url_valid(url: str) -> bool:
    """Method to validate the URL given by user

    Args:
        url (str): provided URL

    Returns:
        bool: _description_
    """
    return bool(URL_REGEX.match(url))


def is_frequency_valid(frequency: int) -> bool:
    return bool(frequency >= 1 and frequency <= 60)


def is_target_price_valid(price: float) -> bool:
    return bool(price > 0)


def is_timeout_valid(timeout: int) -> bool:
    return bool(timeout <= 24)


def is_internet_available() -> bool:
    return not bool(os.system(TEST_INTERNET_CONNECTION))
