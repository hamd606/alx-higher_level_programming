#!/usr/bin/python3
"""Takes in a URL as arg and sends a request to the URL
prints the body of the response in utf-8"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    reqst = Request(url)

    try:
        with urlopen(reqst) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
