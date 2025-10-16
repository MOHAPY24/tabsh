from translations import commands
import os

with open(".tabshrc", 'r') as f:
    code = f.read()
    for cmd in code.splitlines():
        if cmd.split()[0] in commands:
            base = commands[cmd.split()[0]]
            rest = " ".join(cmd.split()[1:])
            os.system(f"{base} {rest}")
        else:
            os.system(cmd)

while True:
    cmd = input("tabsh/$ ").strip()
    if cmd == "خروج":  # exit
        break
    elif cmd.split()[0] in commands:
        base = commands[cmd.split()[0]]
        rest = " ".join(cmd.split()[1:])
        os.system(f"{base} {rest}")
    else:
        os.system(cmd)