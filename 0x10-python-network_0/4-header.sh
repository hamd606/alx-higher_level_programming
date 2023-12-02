#!/bin/bash
# takes in a URL, sends a GET request to the URL, prints the response's body
curl -sX GET $1 -H "X-School-User-Id: 98" -L
