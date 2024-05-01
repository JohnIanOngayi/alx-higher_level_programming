#!/usr/bin/python3
"""
Module prints body or an errorcode of >= 400
"""


if __name__ == "__main__":
    import requests
    import sys

    url = f"{sys.argv[1]}"
    resp = requests.get(url=url)
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    elif resp.status_code == 200:
        print(resp.text)
