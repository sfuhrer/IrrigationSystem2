import time 
import smbus2
import bme280
import sys

#out_string = str(temperature) + "-" + str(humidity) + "-" + str(pressure)


def bme280_get_states():
    # BME280 settings 
    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    bme280data = bme280.sample(bus, address, calibration_params)
    x = [bme280data.humidity, bme280data.temperature,  100 *bme280data.pressure]
    return x