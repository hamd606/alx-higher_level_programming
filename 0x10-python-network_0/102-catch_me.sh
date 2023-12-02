#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me, gets the response You got me!
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
