#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "Input : "
	read a

	if [ $a -eq 0 ]; then
		break;
	elif [ $a -ge 2 -a $a -le 9 ]; then
		for ((i=1;i<10;i++)) do
			echo "$a * $i = `expr $a \* $i`"
		done
	else
		echo "The Number of inputs must be between 2 and 9."
	fi
done
echo Exit

