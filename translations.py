#!/usr/bin/env python3
commands = {

    # Helpful reminders for all translation contributors:
    # 1. Arabic is a lingustically painful language to mix two words the same
    #    way English does for these commands. If you need to translate a command
    #    like "hyperctl" for example, don't hesitate to add a dash between the two
    #    words in Arabic (the prefix "هايبر" and the suffix "تحكم", making "هايبر-تحكم").

    # 2. It's fine if you want to translate a command verbosely, but please don't overdo it.
    #    TABSH is meant to be a way for Arabic beginners to experience Bash in a user
    #    friendly way, so if you don't capture the meaning of a command in one word, you can
    #    extend it to 2-3 words. But do NOT make it a chore to type in a single command, as
    #    most Arabic people (even I lol) feel like it is tiring to type in large amounts of
    #    text.

    # - Written by yours truly, KMA

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
