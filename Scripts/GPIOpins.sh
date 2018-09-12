#!/bin/bash
gpio mode 0 out
gpio mode 1 out
i=1
until [ $i == 11 ]
do
	gpio write 0 1
	gpio write 1 1
	sleep 1
	gpio write 0 0
	gpio write 1 0
	sleep 1
	i=$((i + 1))
done
