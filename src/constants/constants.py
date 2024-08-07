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
