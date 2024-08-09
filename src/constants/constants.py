"""File to house all the `Constants`"""

import re

URL_REGEX = re.compile(
    r"^(https?|ftp):\/\/"  # protocol
    r"(((([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])|([a-zA-Z0-9]+))\.)*[a-zA-Z]{2,})"  # domain name
    r"(:\d+)?"  # optional port
    r"(\/[a-zA-Z0-9._\/%-]*)?"  # path
    r"(\?[a-zA-Z0-9&%=._-]*)?"  # query string
    r"(#.*)?$",  # fragment
    re.IGNORECASE,
)

TEST_INTERNET_CONNECTION = "ping -n 1 www.google.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
