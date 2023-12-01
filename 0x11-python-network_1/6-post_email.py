#!/usr/bin/python3
"""Takes in a URL and an email address as args sends a POST 
request to the URL with the email as parameter then prints the body
of the response"""


import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    reqst = requests.post(url, data=value)

    print(reqst.text)
