#!/bin/bash
# takes in a URL
#sends a request to the URL
#prints the size of the response's body
curl -sX GET $1 -L
