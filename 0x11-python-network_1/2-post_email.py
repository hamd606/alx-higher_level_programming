#!/usr/bin/python3
"""Sends a POST request to the passed url (email)
and prints the body of the response as utf-8"""


from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    reqst = Request(url, data)

    with urlopen(reqst) as response:
        print(response.read().decode("utf-8", "replace"))
