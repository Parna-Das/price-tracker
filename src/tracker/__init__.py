"""Main module for `price-tracker` application"""

import argparse
import logging

from constants.constants import LOG_FILENAME, LOG_FORMAT, LOG_LEVEL
from helper.helper import (
    confirm_product,
    start_tracking,
    tear_down,
    trigger_notification,
)
from validator import validate_inputs


def main() -> None:
    """Method to run `Price Tracker Application`"""
    notify, confirm = False, False
    logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, format=LOG_FORMAT)

    parser = argparse.ArgumentParser(
        usage="price-tracker -u <product url> -p <target price> -f <frequency in minutes> -t<timeout window>",
        description="Application to track price on web",
        add_help=True,
    )
    parser.add_argument("-u", "--url", required=True, help="Provide the product URL")
    parser.add_argument("-p", "--target_price", required=True, help="Provide the desired product price")
    parser.add_argument(
        "-f",
        "--frequency",
        required=True,
        help="Provide the frequency to check the price",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        required=True,
        help="Maximum time to reach product to desired target",
    )

    # ! Step 1 : Consume inputs
    args = parser.parse_args()

    try:
        # ! Step 2 : validate inputs
        validate_inputs(f"{args.url}", int(args.frequency), float(args.target_price), int(args.timeout))
        logging.info("Inputs are in correct format")

        # ! Step 3 : Confirm and proceed
        confirm = confirm_product(f"{args.url}")
        logging.info("Product is correct")

        # ! Step 4 : Initializing tracking
        if confirm:
            notify = start_tracking(url=f"{args.url}", target_price=float(args.target_price), frequency=int(args.frequency), timeout=int(args.timeout))

        # ! Step 5 : Notify the user
        if notify:
            trigger_notification()

    except KeyboardInterrupt:
        logging.error("Keyboard interrupt detected. Exiting gracefully")

    finally:
        # ! Step 6 : Exit
        tear_down()


if __name__ == "__main__":
    main()
