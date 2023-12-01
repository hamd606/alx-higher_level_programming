#!/usr/bin/python3
"""Takes GitHub credentials then uses the GitHub API to print the id"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    reqst = requests.get("https://api.github.com/user", auth=auth)

    print(reqst.json().get("id"))
