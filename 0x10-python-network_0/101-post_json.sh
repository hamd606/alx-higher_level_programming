#!/bin/bash
# sends a JSON POST request to the passed URL
# prints the body of the response
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
