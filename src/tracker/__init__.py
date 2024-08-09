"""Main module for `price-tracker` application"""

import argparse

from helper.helper import (
    confirm_product,
    start_tracking,
    tear_down,
    trigger_notification,
)
from validator import validate_inputs


def main() -> None:
    """method to run `price-tracker` application"""
    parser = argparse.ArgumentParser(
        usage="price-tracker -u <product url> -p <target price> -f <frequency in minutes> -t<timeout window>",
        description="Application to track price on web",
        add_help=True,
    )
    parser.add_argument("-u", "--url", required=True, help="Provide the product URL")
    parser.add_argument(
        "-p", "--target_price", required=True, help="Provide the desired product price"
    )
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
        validate_inputs(
            args.url, int(args.frequency), float(args.target_price), int(args.timeout)
        )

        # ! Step 3 : Confirm and proceed
        confirm_product(args.url)

        # ! Step 4 : Initializing tracking
        start_tracking()

        # ! Step 5 : Notify the user
        trigger_notification()

    except KeyboardInterrupt:
        print("Exiting gracefully")

    finally:
        # ! Step 6 : Exit
        tear_down()


if __name__ == "__main__":
    main()
