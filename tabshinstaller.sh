#!/bin/bash

# Made by kma 21/10/2025.
# This script is 100% gluten free. Probably.

if command -v python3 >/dev/null 2>&1; then
  version=$(python3 -V 2>&1 | awk '{print $2}')
  printf "TABSHInstaller: Python3 version $version detected.\n"
  if command -v pip3 >/dev/null 2>&1; then
    pipver=$(pip3 -V 2>&1 | awk '{print $2}')
    printf "TABSHInstaller: Pip3 version $pipver detected.\n"
  else
    printf "TABSHInstaller: Pip3 is NOT installed! Please install Pip3 and try again.\n"
    exit 1
  fi
else
    printf "TABSHInstaller: Python3 is NOT installed! Please install Python3 and try again.\n"
    exit 1
fi

if [[ "$SHELL" == "/bin/zsh" ]]; then
	rc="$HOME/.zshrc"
elif [[ "$SHELL" == "/bin/bash" ]]; then
	rc="$HOME/.bashrc"
else
	printf "TABSHInstaller: This shell is NOT supported! Use Bash or ZSh and try again.\n"
	exit 1
fi

printf "\n"
printf "|-----------------------------------|\n"
printf "|  Welcome to the TABSH installer!  |\n"
printf "|  !مرحبًا بك في برنامج التثبيت طبش  |\n"
printf "|-----------------------------------|\n"
printf "        Beta version 0.3\n"
printf "\n"

printf "TABSHInstaller: What language would you like to continue in?\n"
printf "TABSHInstaller: ما هي اللغة التي ترغب في الاستمرار بها؟\n"
read -p '(english/عربي): ' lang

if [[ "$lang" == "english" ]]; then
	printf "TABSHInstaller: Installing dependencies from Pip\n"
	pip3 install colorama prompt-toolkit &&
	printf "TABSHInstaller: Downloading TABSH\n" &&
	sudo git clone https://github.com/MOHAPY24/tabsh.git /usr/local/bin/tabsh &&
	printf "TABSHInstaller: Making shell executable\n" &&
	chmod +x /usr/local/bin/tabsh/tabsh.sh &&
	printf "TABSHInstaller: Modifying $rc to automatically start TABSH\n" &&
	printf "cd /usr/local/bin/tabsh && ./tabsh.sh" >> $rc &&
	printf "Successfully installed! Starting...\n"
	source $rc
elif [[ "$lang" == "عربي" ]]; then
        printf "TABSHInstaller: تثبيت التبعيات\n" &&
        pip3 install colorama prompt-toolkit &&
        printf "TABSHInstaller: تنزيل طبش\n" &&
        git clone https://github.com/MOHAPY24/tabsh.git /usr/local/bin &&
        printf "TABSHInstaller: جعل الصدفة قابلاً للتنفيذ\n" &&
        chmod +x ~/tabsh/tabsh.sh &&
	echo "cd /usr/local/bin/tabsh && ./tabsh.sh" >> "$rc" &&
        printf "Successfully installed! Starting...\n"
	source $rc
else
	printf "TABSHInstaller: invalid option\n"
fi
