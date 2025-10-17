#!/usr/bin/env python3

import os
import utils
import subprocess
from colorama import init, Fore, Style
from translations import commands
init(True)


def handle_rc(current_dir): # handle .tabshrc
    # TODO: make .tabshrc work in a .config folder
    script = ".tabshrc" # get rc file
    with open(script, 'r') as f:
        scode = f.read().strip() # get rc contents without trailing newlines/whitespaces
        for cmd in scode.splitlines(): # for each line
            if not cmd:
                continue
            if cmd == "خروج" or cmd == "quit" or cmd == "exit":  # exit 
                break


            # Translate command keywords
            # utils.py
            translated_cmd = utils.replace_all_keywords(cmd, commands)
            base = translated_cmd.split()[0]

            if base == "cd":
                parts = translated_cmd.split(maxsplit=1)
                path = parts[1] if len(parts) > 1 else os.path.expanduser("~")

                try:
                    os.chdir(os.path.expanduser(path))
                    current_dir = os.getcwd()
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
                    print(Fore.RED + e)
    
    current_dir = os.path.expanduser("~")
    os.chdir(current_dir)
    return current_dir
