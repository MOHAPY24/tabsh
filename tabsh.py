#!/usr/bin/env python3

# ____IMPORTS______
from translations import commands
import subprocess
import utils
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import sys
from handle_scripts import script_handler
from rc_handler import handle_rc
from colorama import init, Fore, Style

init(True)

# For directory tracking
global curr_dir
curr_dir = ""

# handle_scripts.py
script_handler(curr_dir, sys.argv)

# command history and cycling
history = FileHistory('.tabshhistory')
session = PromptSession(history=history)

# to be written to .tabshhistory
command_history = []

r = open(".tabshhistory", 'a')

# rc_handler.py
curr_dir = handle_rc(curr_dir)

while True:
    try:
        cmd = session.prompt(f"{curr_dir} $$ ").strip() # Clean prompt
        command_history.append(cmd) # add to command history
    except KeyboardInterrupt: # Safe end
        r.write(str(command_history).replace("]", '').replace("[", '').replace(",", '').strip())
        r.close()
        break
    if not cmd: # prevent empty commands
        continue
    if cmd == "خروج" or cmd == "quit" or cmd == "exit":  # exit
        r.write(str(command_history).replace("]", '').replace("[", '').replace(",", '').strip())
        r.close()
        break

    # utils.py
    translated_cmd = utils.replace_all_keywords(cmd, commands) 
    base = translated_cmd.split()[0]

    if base == "cd": # Handle directory changes safely
        parts = translated_cmd.split(maxsplit=1)
        path = parts[1] if len(parts) > 1 else os.path.expanduser("~")

        try:
            os.chdir(os.path.expanduser(path))
            curr_dir = os.getcwd()
        except FileNotFoundError:
            print(Fore.RED + f"cd: no such file or directory: {path}")
        except NotADirectoryError:
            print(Fore.RED + f"cd: not a directory: {path}")
        except PermissionError:
            print(Fore.RED + f"cd: permission denied: {path}")
    else:
        try:
            subprocess.run(translated_cmd, shell=True)
        except Exception as e:
            print(Fore.RED + e) # error handling
