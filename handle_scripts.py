import utils
import os
import subprocess
import sys

def script_handler(current_dir, argvs:list): # handle scripts passed as arguments
    try:
        script = argvs[1]
        with open(script, 'r') as f:
            scode = f.read().strip() # get script contents without trailing newlines/whitespaces
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