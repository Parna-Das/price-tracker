"""File to house all the `Helper` functions"""

import requests


def confirm_product(url: str) -> bool:

    return True


def start_tracking() -> bool:
    return True


def trigger_notification() -> bool:
    return True


def tear_down(): ...


def resolve_url(url: str) -> tuple[str, float, str]:
    response = requests.get(url=url, verify=True, timeout=30)
    if response.status_code == 200:
        print(response.text)
    return ("Sample Product", 100, "Available")


if __name__ == "__main__":
    resolve_url(
        "https://www.amazon.in/Samsung-Galaxy-Smartphone-Olive-Green/dp/B0C1Z8WTS6/ref=sr_1_1?_encoding=UTF8&s=electronics&sr=1"
    )

    # from bs4 import BeautifulSoup as bs
    # resp = requests.get(r"https://www.amazon.in/dp/B0CB3Z4DZL?ref_=cm_sw_r_cso_wa_apin_dp_TFKA9B85TXMTR9R6EBYB&starsLeft=1&skipTwisterOG=2",headers=headers).content
    # a = bs(resp,"html.parser")
    # a.find("span", {"id": "productTitle", "class": "a-size-large product-title-word-break"}).text.strip()
    # a.find("span", {"class": "a-price-whole"}).text.strip()[:-1]
    # a.find("span", {"class": "a-size-medium a-color-success"}).text.strip()
