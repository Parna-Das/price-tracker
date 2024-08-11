"""File to house all the `Constants`"""

from datetime import datetime
import re
import logging
from pathlib import Path

# URL_REGEX = re.compile(
#     r"^(https?|ftp):\/\/"  # protocol
#     r"(((([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])|([a-zA-Z0-9]+))\.)*[a-zA-Z]{2,})"  # domain name
#     r"(:\d+)?"  # optional port
#     r"(\/[a-zA-Z0-9._\/%-]*)?"  # path
#     r"(\?[a-zA-Z0-9&%=._-]*)?"  # query string
#     r"(#.*)?$",  # fragment
#     re.IGNORECASE,
# )
URL_REGEX = re.compile(r"^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)$")

TEST_INTERNET_CONNECTION = "ping -n 1 www.google.com"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

# Logging constants
LOG_FILENAME = Path("logs", f'price-tracker-{datetime.now().strftime("%Y%m%d%H%M%S")}.log')
LOG_FILENAME.parent.mkdir(parents=True, exist_ok=True)
LOG_FORMAT = "%(asctime)s\t%(levelname)s\tModule:%(module)s\t\tFunction:%(funcName)s\t%(message)s"
LOG_LEVEL = logging.INFO
