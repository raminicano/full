#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "Input : "
	read a

	if [ $a != "0" ]; then
		for ((i=1;i<10;i++)) do
			echo "$a * $i = `expr $a \* $i`"
		done
	fi
done
echo Exit

