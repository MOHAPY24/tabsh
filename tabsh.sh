#!/bin/bash 
# tabsh script wrapper

set -e # ends if error

prev_shell=$SHELL # Record shell before change

if [    $(pwd) == "/bin/tabsh"  ]; then # check if the shell is in /bin/
    printf ' \n'
else
    printf "WARNING: Shell not in /bin \n" # Warn if not
    sleep 1
fi


export SHELL="$(pwd)/tabsh.sh" # change shell
if [    "$1" == ""  ]; then # if there is no arguments run the shell, otherwise run the script given
    python3 tabsh.py 
else
    python3 tabsh.py $1
fi

export SHELL="$prev_shell" # change shell after exit back to normal