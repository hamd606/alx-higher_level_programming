#!/usr/bin/python3
"""Takes in a URL as arg and sends a request to the URL and 
prints the value of the variable X-Request-Id in the response header"""


import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    reqst = requests.get(url)

    print(reqst.headers.get("X-Request-Id"))
