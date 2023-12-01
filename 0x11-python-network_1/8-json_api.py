#!/usr/bin/python3
"""Takes a letter as arg and sends a POST request to the address
http://0.0.0.0:5000/search_user with the letter as parameter"""


from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    reqst = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        response = reqst.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
