#!/usr/bin/python3
"""Takes in a URL as arg and sends a request to the URL
and prints displays the body of the response"""


from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    reqst = requests.get(url)

    if reqst.status_code >= 400:
        print("Error code: {}".format(reqst.status_code))
    else:
        print(reqst.text)
