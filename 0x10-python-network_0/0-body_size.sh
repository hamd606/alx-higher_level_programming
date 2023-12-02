#!/bin/bash
# takes in a URL
#sends a request to the URL
#prints the size of the response's  body
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
