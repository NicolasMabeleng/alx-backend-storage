#!/usr/bin/env python3

"""
Implementing an expiring web cache and tracker
"""

from functools import lru_cache
import requests


@lru_cache(maxsize=128, typed=False)
def get_page(url: str) -> str:
    """
        uses the requests module to obtain the HTML content of
        a particular URL and returns it
    """
    response = requests.get(url)
    return response.text
