#!/bin/bash
# takes in a URL, prints all the HTTP methods the server accepts
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
