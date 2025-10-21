#!/bin/bash

# Made by kma 21/10/2025.
# This script was thankfully sponsored by Jeffery Epstein's third ex-wife!

printf "\n"
printf "|-----------------------------------|\n"
printf "|  Welcome to the TABSH installer!  |\n"
printf "|  !مرحبًا بك في برنامج التثبيت طبش  |\n"
printf "|-----------------------------------|\n"
printf "        Beta version 0.1\n"
printf "\n"

printf "TABSHInstaller: What language would you like to continue in?\n"
printf "TASHInstaller: ما هي اللغة التي ترغب في الاستمرار بها؟\n"
read -p "(english/عربي): " lang

if [[ "$lang" == "english" ]]; then
	printf "TABSHInstaller: Pip that shit!\n"
	pip install colorama prompt-toolkit &&
	printf "TABSHInstaller: Downloading TABSH from Testicles GitHub\n"
	git clone https://github.com/MOHAPY24/tabsh.git &&
	printf "TABSHInstaller: Making shell executable\n"
	chmod +x ~/tabsh/tabsh.sh &&
	if [[ "$SHELL" == "/bin/zsh" ]]; then
		rc="~/.zshrc"
	elif [[ "$SHELL" == "/bin/bash" ]]; then
		rc="~/.bashrc"
	else
		printf "TABSHInstaller: Invalid shell! Exiting...\n"
		exit 1
	fi
	printf "TABSHInstaller: Modifying $rc to automatically start TABSH\n"
	echo "source ~/tabsh/tabsh.sh\n" >> $rc &&
	printf "Successfully installed!"
elif [[ "$lang" == "عربي" ]]; then
        printf "TABSHInstaller: تثبيت التبعيات\n"
        pip install colorama prompt-toolkit &&
        printf "TABSHInstaller: تنزيل طبش\n"   
        git clone https://github.com/MOHAPY24/tabsh.git &&
        printf "TABSHInstaller: جعل الصدفة قابلاً للتنفيذ\n"
        chmod +x ~/tabsh/tabsh.sh &&
        if [[ "$SHELL" == "/bin/zsh" ]]; then
                rc="~/.zshrc"
        elif [[ "$SHELL" == "/bin/bash" ]]; then  
                rc="~/.bashrc"
        else    
                printf "TABSHInstaller: ... صدفة غير صالح! جاري الخروج\n"
                exit 1
        fi
	echo "source ~/tabsh/tabsh.sh\n" >> $rc &&
        printf "Successfully installed!\n"
else
	printf "TABSHInstaller: invalid option\n"
fi
