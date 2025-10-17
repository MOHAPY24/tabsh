#!/bin/bash 

set -e

if [    "$1" == ""  ]; then
    python3 tabsh.py 
else
    python3 tabsh.py $1
fi