#!/bin/bash
# sends a request to the passed URL, prints the status code of the response
curl -o /dev/null -sw "%{http_code}" $1
