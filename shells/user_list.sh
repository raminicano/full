#!/bin/bash

input="/etc/passwd"
count=1
while IFS=':' read -r username uid gid home shell
do
	let count+=1
	echo "$count : $username $uid $gid $home $shell"
done < $input

