#!/bin/bash
good='\e[0;32m'
bad='\e[0;31m'

pkgm0="apt"
pkgm1="dnf"
pkgm2="dpkg"

exec0="python"
exec1="pip"

pip0="argparse"
pip1="g4f"

name="gpt-cli"

error=0

if command -v $exec0 2>&1 >/dev/null
then
	echo -e " Dependency satisfied: $exec0 is installed."
else
	if command -v $exec0 2>&1 >/dev/null
	then
		$pkgm0 install $exec0
	else
		if command -v $pkgm1 2>&1 >/dev/null
		then
			$pkgm1 install $exec0
		else
			if command -v $pkgm2 2>&1 >/dev/null
			then
				$pkgm2 install $exec0
			else
				echo -e "$bad Dependency is not satisfied: $exec0 is not installed."
				error=1
			fi
		fi
	fi
fi

if command -v $exec1 2>&1 >/dev/null
then
	echo -e " Dependency satisfied: $exec1 is installed."
else
	if command -v $pkgm0 2>&1 >/dev/null
	then
		$pkgm0 install $exec1
	else
		if command -v $pkgm1 2>&1 >/dev/null
		then
			$pkgm1 install $exec1
		else
			if command -v $pkgm2 2>&1 >/dev/null
			then
				$pkgm2 install $exec1
			else
				echo -e "$bad Dependency is not satisfied: $exec1 is not installed."
				error=1
			fi
		fi
	fi
fi

mod0=$(eval "pip show $pip0 | grep Name")
mod1=$(eval "pip show $pip1 | grep Name")

if [[ "$mod0" == *"$pip0"* ]];
then
	echo -e " Dependency satisfied: $pip0 is installed."
else
	$exec1 install $pip0
fi

if [[ "$mod1" == *"$pip1"* ]];
then
	echo -e " Dependency satisfied: $pip1 is installed."
else
	$exec1 install $pip1
fi

if [[ $error == 0 ]]
then
	cp $name.py /bin/$name
	chmod o+x /bin/$name
	echo -e "\e[0;36m $name$good is installed."
else
	echo -e "$bad $name is not installed."
fi
echo ""
