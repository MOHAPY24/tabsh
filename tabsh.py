from translations import commands
import subprocess
import utils
import os


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
    global curr_dir
    curr_dir = os.path.expanduser("~")

while True:
    cmd = input(f"{curr_dir} $$ ").strip()
    if not cmd:
        continue
    if cmd == "خروج":  # exit
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
