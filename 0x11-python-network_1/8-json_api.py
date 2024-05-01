#!/usr/bin/python3
"""
Module searches for user
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q = f"{sys.argv[1]}" if len(sys.argv[1]) == 1 else f""
    data = {'q': q}
    try:
        res = requests.post(url=url, data=data)
        if len(res.json()) != 0:
            print(f"[{res.json().get('id')}] {res.json().get('name')}")
        else:
            print(f"No result")
    except ValueError:
        print(f"Not a valid JSON")
