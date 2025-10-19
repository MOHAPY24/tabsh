#!/usr/bin/env python3
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

    # I have no idea where Git is supposed to go so im just gonna put it
    # here and figure it out later
    "قيت": "git"
}
