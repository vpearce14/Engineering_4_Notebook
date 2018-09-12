#!/bin/bash
gpio mode 0 out
i=1
until [ $i == 11 ]
do
	gpio write 0 1
	sleep 1
	gpio write 0 0
	sleep 1
	i=$((i + 1))
done
