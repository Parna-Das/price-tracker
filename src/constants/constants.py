"""File to house all the `Constants`"""

import logging
import re
from datetime import datetime
from pathlib import Path

# Website regex pattern
URL_REGEX = re.compile(r"^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)$")

# Internet connection check
TEST_INTERNET_CONNECTION = "ping -n 1 www.google.com"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

# Logging constants
LOG_FILENAME = Path("logs", f'price-tracker-{datetime.now().strftime("%Y%m%d%H%M%S")}.log')
LOG_FILENAME.parent.mkdir(parents=True, exist_ok=True)
LOG_FORMAT = "%(asctime)s\t%(levelname)s\tModule:%(module)s\t\tFunction:%(funcName)s\t%(message)s"
LOG_LEVEL = logging.INFO

# Pdoc commands
GENERATE_DOCUMENTATION = "pdoc3 --html src/ --output-dir docs --force"
