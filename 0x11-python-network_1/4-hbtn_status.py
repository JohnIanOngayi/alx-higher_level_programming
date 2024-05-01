#!/usr/bin/python3
"""
Module uses requests to send GET request
"""


if __name__ == "__main__":
    import requests

    url = f"https://alx-intranet.hbtn.io/status"
    resp = requests.get(url=url)
    print(f"Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")
