#!/usr/bin/env python3

from translations import commands
import subprocess
import utils
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import sys

global curr_dir
curr_dir = ""

try:
    script = sys.argv[1]
    with open(script, 'r') as f:
        scode = f.read().strip()
        for cmd in scode.splitlines():
            if not cmd:
                continue
            if cmd == "خروج" or cmd == "quit" or cmd == "exit":  # exit
                break


            # Translate command keywords
            translated_cmd = utils.replace_all_keywords(cmd, commands)
            base = translated_cmd.split()[0]

            if base == "cd":
                parts = translated_cmd.split(maxsplit=1)
                path = parts[1] if len(parts) > 1 else os.path.expanduser("~")

                try:
                    os.chdir(os.path.expanduser(path))
                    curr_dir = os.getcwd()
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {path}")
                except NotADirectoryError:
                    print(f"cd: not a directory: {path}")
                except PermissionError:
                    print(f"cd: permission denied: {path}")
            else:
                try:
                    subprocess.run(translated_cmd, shell=True)
                except Exception as e:
                    print(e)
    quit()

except IndexError:
    pass


history = FileHistory('.tabshhistory')
session = PromptSession(history=history)

command_history = []

r = open(".tabshhistory", 'a')

with open(".tabshrc", 'r') as f:
    code = f.read()
    for cmd in code.strip().splitlines():
        if cmd in "\n\t ":
            continue
        elif cmd.split()[0] in commands:
            base = utils.replace_all_keywords(cmd, commands)
            os.system(f"{base}")
        else:
            os.system(cmd)
    
    curr_dir = os.path.expanduser("~")
    os.chdir(curr_dir)

while True:
    try:
        cmd = session.prompt(f"{curr_dir} $$ ").strip()
        command_history.append(cmd)
    except KeyboardInterrupt:
        r.write(str(command_history).replace("]", '').replace("[", '').replace(",", '').strip())
        r.close()
        break
    if not cmd:
        continue
    if cmd == "خروج" or cmd == "quit" or cmd == "exit":  # exit
        r.write(str(command_history).replace("]", '').replace("[", '').replace(",", '').strip())
        r.close()
        break


    # Translate command keywords
    translated_cmd = utils.replace_all_keywords(cmd, commands)
    base = translated_cmd.split()[0]

    if base == "cd":
        parts = translated_cmd.split(maxsplit=1)
        path = parts[1] if len(parts) > 1 else os.path.expanduser("~")

        try:
            os.chdir(os.path.expanduser(path))
            curr_dir = os.getcwd()
        except FileNotFoundError:
            print(f"cd: no such file or directory: {path}")
        except NotADirectoryError:
            print(f"cd: not a directory: {path}")
        except PermissionError:
            print(f"cd: permission denied: {path}")
    else:
        try:
            subprocess.run(translated_cmd, shell=True)
        except Exception as e:
            print(e)
