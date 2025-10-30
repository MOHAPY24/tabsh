#!/bin/sh

# This is an experimental script to try to fit the entirety of TABSH
# into a single .sh.

python3 - <<'PYTHON'
from translations import commands
import subprocess
import utils
import os
from prompt_toolkit import PromptSession
import prompt_toolkit
from prompt_toolkit.history import FileHistory
import sys
from handle_scripts import script_handler
from rc_handler import handle_rc
from colorama import init, Fore, Style

# translation dictionary
commands = {
    # File and Directory Management
    "عدد": "ls",
    "غير": "cd",
    "حالي": "pwd",
    "مجلد-جديد": "mkdir",
    "مجلد-مسح": "rmdir",
    "ملف-جديد": "touch",
    "نسخ": "cp",
    "تحرك": "mv",
    "مسح": "rm",
    "اقره": "cat",
    "لس": "less",
    "مور": "more",

    # Text Processing
    "يجد": "grep",
    "سيد": "sed",
    "اوك": "awk",
    "راس": "head",
    "ذيل": "tail",

    # System Information and Monitoring
    "عمل": "ps",
    "الأعمال": "top",
    "سعة-قرص": "df",
    "سعة-ملف": "du",
    "سعة-ذكره": "free",
    "معلومات": "uname",
    "تاريخ": "history",
    "من-أنا": "whoami", # Important sometimes

    # Permissions and Ownership
    "ملف-إذن": "chmod",
    "ملف-صاحب": "chown",
    "ملف-مجموعة": "chgrp",

    # Networking
    "بينغ": "ping",
    "كورل": "curl",
    "وغيت": "wget",
    "تحكم": "ssh",
    "شراك": "scp",

    # System management
    "نظام-تحكم": "systemctl",

    # Process Management
    "قف": "kill",
    "قف-اسم": "killall",
    "أمام": "fg",
    "خلف": "bg",

    # Other Essential Commands
    "صدى": "echo",
    "معنى": "man",
    "صعد": "sudo",
    "فساد": "alias",
    "واضح": "clear",

    # Package Managers and related (section added 17/10/25)
    # Arch
    "باكمان": "pacman",
    "مايك-بكج": "makepkg",
    "حزمة": "pkg", # FreeBSD
    "ياي": "yay",
    "بارو": "paru",
    # Debian
    "ابت": "apt",
    "د-بكج": "dpkg",
    "ابت-قت": "apt-get",
    # Fedora (the word "rpm" is shared between Fedora and openSUSE)
    "ربم": "rpm",
    "دنف": "dnf",
    # openSUSE
    "زيبر": "zypper",
    # Alpine
    "ابك": "apk",
    # Other package Managers
    "نبم": "npm", # Required, I don't know how it's still not there lol
    "برو": "brew",
    "بيب": "pip",

    # I have no idea where Git is supposed to go so im just gonna put it
    # here and figure it out later
    "قيت": "git",

    # Syntax of Logic (does not work yet)
    "لو": "if",
    "ثم": "then",
    "اخر": "else",
    "ول": "fi",
    "بينما": "while",
    "صحيح": "true",
    "خطا": "false",

    # Hyprland utils (Section added 20/10/25) ("I use MATE btw" -kma)
    # Friendly reminder that the prefix "-هايبر" should be used before every "hypr-" command
    "هايبر-تحكم": "hyprctl",
    "هايبر-خلفية": "hyprpaper",
    "هايبر-صور": "hyprshot"

    # "Ooh eeh ooh ah ah, ting tang wala wala bang bang!"
    #                                - Witch Doctor, 1998
}

# handle history and rc files
if not os.path.exists(os.path.expanduser("~/.config/.tabshhistory")):
    with open(os.path.expanduser("~/.config/.tabshhistory"), 'w') as f:
        f.close()

if not os.path.exists(".tabshrc"):
    with open(".tabshrc", 'w') as f:
        f.write("clear")
        f.close()

init(True)

# For directory tracking
global curr_dir
curr_dir = ""

# handle_scripts.py
script_handler(curr_dir, sys.argv)

safe_history_file = os.path.expanduser("~/.config/.tabshhistory")

try:
    history = FileHistory(safe_history_file)
except PermissionError:
    from prompt_toolkit.history import InMemoryHistory
    history = InMemoryHistory()

# command history and cycling
session = PromptSession(history=history, editing_mode=prompt_toolkit.enums.EditingMode.VI)

# to be written to .tabshhistory
command_history = []



r = open(os.path.expanduser("~/.config/.tabshhistory"), 'a')

# rc_handler.py
curr_dir, alias = handle_rc(curr_dir)

while True:
    try:
        cmd = session.prompt(f"{curr_dir.replace(os.path.expanduser('~'), '~', 1)} $$ ").strip() # Clean prompt
        command_history.append(cmd) # add to command history
    except (KeyboardInterrupt, EOFError): # Safe end
        continue # now to exit only use 'exit'


    if not cmd: # prevent empty commands
        continue
    if cmd == "خروج" or cmd == "quit" or cmd == "exit":  # exit
        r.write(utils.format_list(command_history))
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

r.close()
PYTHON

# gonna work on this more later but its not a very high priority
# momo if you can pls fix some of this stuff
