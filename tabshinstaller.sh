#!/bin/bash

# Made by kma 21/10/2025.
# This script was thankfully sponsored by Jeffery Epstein's third ex-wife!

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

printf "\n"
printf "|-----------------------------------|\n"
printf "|  Welcome to the TABSH installer!  |\n"
printf "|  !مرحبًا بك في برنامج التثبيت طبش  |\n"
printf "|-----------------------------------|\n"
printf "        Beta version 0.2\n"
printf "\n"

printf "TABSHInstaller: What language would you like to continue in?\n"
printf "TABSHInstaller: ما هي اللغة التي ترغب في الاستمرار بها؟\n"
read -p '(english/عربي): ' lang

if [[ "$lang" == "english" ]]; then
	printf "TABSHInstaller: Installing Pip\n"
	pip3 install colorama prompt-toolkit &&
	printf "TABSHInstaller: Downloading TABSH\n"
	git clone https://github.com/MOHAPY24/tabsh.git &&
	printf "TABSHInstaller: Making shell executable\n"
	chmod +x ~/tabsh/tabsh.sh &&
	if [[ "$SHELL" == "/bin/zsh" ]]; then
		rc="$HOME/.zshrc"
	elif [[ "$SHELL" == "/bin/bash" ]]; then
		rc="$HOME/.bashrc"
	else
		printf "TABSHInstaller: Invalid shell! Exiting...\n"
		exit 1
	fi
	printf "TABSHInstaller: Modifying $rc to automatically start TABSH\n"
	printf "source ~/tabsh/tabsh.sh\n" >> $rc &&
	printf "Successfully installed!"
elif [[ "$lang" == "عربي" ]]; then
        printf "TABSHInstaller: تثبيت التبعيات\n"
        pip3 install colorama prompt-toolkit &&
        printf "TABSHInstaller: تنزيل طبش\n"   
        git clone https://github.com/MOHAPY24/tabsh.git &&
        printf "TABSHInstaller: جعل الصدفة قابلاً للتنفيذ\n"
        chmod +x ~/tabsh/tabsh.sh &&
        if [[ "$SHELL" == "/bin/zsh" ]]; then
                rc="$HOME/.zshrc"
        elif [[ "$SHELL" == "/bin/bash" ]]; then  
                rc="$HOME/.bashrc"
        else    
                printf "TABSHInstaller: ... صدفة غير صالح! جاري الخروج\n"
                exit 1
        fi
	printf "source ~/tabsh/tabsh.sh\n" >> "$rc" &&
        printf "Successfully installed!\n"
else
	printf "TABSHInstaller: invalid option\n"
fi
