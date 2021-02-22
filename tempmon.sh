#!/bin/bash

timestamp=`date +%Y-%m-%d_%H-%M-%S`

filename="log/"$timestamp".txt"
filename="test"

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

	IFS='-' #setting comma as delimiter
	read -a strarr <<<"$lastline" #reading str as an array as tokens separated by IFS  
	echo "Temp : ${strarr[0]} "  
	echo "Hum : ${strarr[1]} "  
	echo "Pres : ${strarr[2]}" 

	temp_pi=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
	timestamp=`date +%Y-%m-%d_%H-%M-%S`
	#echo "$temp_pi $timestamp"
	echo "$timestamp $temp_pi" >> $filename
	sleep 5
done
