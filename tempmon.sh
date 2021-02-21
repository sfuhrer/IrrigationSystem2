#!/bin/bash

timestamp=`date +%Y-%m-%d_%H-%M-%S`

filename="log/"$timestamp".txt"

touch $filename
echo  "Created file: "$filename

#printf "%-15s%5s\n" "Timestamp Temperature[°C]"
#printf "%20s\n" "------------------"

while true
do
	python drivers/bme280_read.py | {
  		while IFS= read -r line
  		do
    			lastline="$line"
  		done

  		echo "Last measurements (temp-hum-pres): $lastline"
	}

	IFS='-' read -ra ADDR <<< "$lastline"
	echo "lastline again:" "asfd"
	for i in "${ADDR[@]}"; do
    		echo "$i"
	done

	temp_pi=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
	timestamp=`date +%Y-%m-%d_%H-%M-%S`
	echo "$temp_pi $timestamp"
	echo "$timestamp $temp_pi" >> $filename
	sleep 5
done
