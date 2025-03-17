#!/bin/bash
good='\e[0;32m'
bad='\e[0;31m'

name="gpt-cli"

error=0
if [[ $error == 0 ]]
then
	cp $name.py /bin/$name
	sudo chmod o+x /bin/$name
	echo -e "\e[0;36m $name$good is installed."
else
	echo -e "$bad $name is not installed."
fi
echo ""
