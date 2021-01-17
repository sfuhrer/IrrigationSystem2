#!/bin/bash

timestamp=`date +%Y-%m-%d_%H-%M-%S`

filename=$timestamp".txt"
#filename="test.txt"

touch $filename
echo  "Created file: "$filename

printf "%-15s%5s\n" "Timestamp Temperature[°C]"
printf "%20s\n" "------------------"

while true
do
	temperature=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
	timestamp=`date +%Y-%m-%d_%H-%M-%S`
	echo "$temperature $timestamp"
	echo "$timestamp $temperature" >> $filename
	sleep 60
done
