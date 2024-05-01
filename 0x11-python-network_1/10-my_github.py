#!/usr/bin/python3
"""
Module interats with the GitHub API to print said user's ID
"""


if __name__ == "__main__":
    import requests
    from requests import auth
    import sys

    url = 'https://api.github.com/user'
    auth = auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
