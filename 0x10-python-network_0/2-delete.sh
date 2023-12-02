#!/bin/bash
# sends a DELETE request to the 1st arg (URL)
#prins the respons's body
curl -sX DELETE $1 -L
