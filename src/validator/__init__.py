""""Module to house all the `validator` files"""

import logging
from validator.validator import (
    is_internet_available,
    is_timeout_valid,
    is_target_price_valid,
    is_frequency_valid,
    is_url_valid,
)


def validate_inputs(url: str, frequency: int, price: float, timeout: int) -> bool:
    status = all(
        [
            is_url_valid(url),
            is_frequency_valid(frequency),
            is_target_price_valid(price),
            is_timeout_valid(timeout),
            is_internet_available(),
        ]
    )
    if not status:
        print("Invalid inputs received. Please check and retry")
        raise KeyboardInterrupt
    print("All inputs are valid")
    logging.info("All inputs are valid")
    return status
