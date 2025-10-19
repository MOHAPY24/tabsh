#!/bin/bash 

set -e # ends if error

if [    "$1" == ""  ]; then # if there is no arguments run the shell, otherwise run the script given
    python3 tabsh.py 
else
    python3 tabsh.py $1
fi