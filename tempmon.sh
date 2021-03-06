#!/bin/bash

#i2cdetect needed, otherwise I2C connection is not detected by driver
i2cdetect -y 1

i_max=144000 #max iterations
dt=60 #time step, seconds
i=1
date_prev="0"

filename="test"

while [ $i -le $i_max ]
do  	
	#check if new day, and open new file if so
	timestamp_file=$(date +%Y_%m_%d_%H_%M_%S)
	data_curr=${timestamp_file:0:10}

	if [ "$date_curr" != "$data_prev" ];
	then	
		filename="/home/pi/IrrigationSystem2/log/"$timestamp_file".txt"
		#filename="test"

		touch $filename
		echo  "Created file: "$filename
	fi

	output=$(python /home/pi/IrrigationSystem2/drivers/bme280_read.py)

	#measurement data is separated by -
	IFS='-' #setting - as delimiter
	read -a strarr <<<"$output" #reading str as an array as tokens separated by IFS  
	temp=${strarr[0]}
	hum=${strarr[1]}
	pres=${strarr[2]}

	temp_pi=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')
	timestamp_meas=$(date +%Y-%m-%d_%H:%M:%S)

	echo "$timestamp_meas $temp_pi $temp $hum $pres"
	echo "$timestamp_meas $temp_pi $temp $hum $pres" >> $filename

	i=$(( $i + 1 ))
	sleep $dt
done
