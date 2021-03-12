#!/bin/bash

#i2cdetect needed, otherwise I2C connection is not detected by driver
i2cdetect -y 1


output=$(python /home/pi/IrrigationSystem2/drivers/bme280_read.py)

