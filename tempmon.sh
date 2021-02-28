#!/bin/bash

timestamp=$(date +%Y_%m_%d_%H_%M_%S)

filename="/home/pi/IrrigationSystem2/log/"$timestamp".txt"
#filename="test"

touch $filename
echo  "Created file: "$filename

#printf "%-15s%5s\n" "Timestamp Temperature[°C]"
#printf "%20s\n" "------------------"

i2cdetect -y 1

i_max=1440 #max iterations
dt=60 #time step, seconds
i=1
while [ $i -le $i_max ]
do  	
	output=$(python /home/pi/IrrigationSystem2/drivers/bme280_read.py)

	IFS='-' #setting - as delimiter
	read -a strarr <<<"$output" #reading str as an array as tokens separated by IFS  
	temp=${strarr[0]}
	hum=${strarr[1]}
	pres=${strarr[2]}

	temp_pi=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
	timestamp_meas=$(date +%Y_%m_%d_%H_%M_%S)

	echo "$timestamp_meas $temp_pi $temp $hum $pres"
	echo "$timestamp_meas $temp_pi $temp $hum $pres" >> $filename

	i=$(( $i + 1 ))
	sleep $dt
done
