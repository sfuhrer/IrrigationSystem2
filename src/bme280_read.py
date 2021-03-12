import time 
import smbus2
import bme280
import sys

# BME280 settings 
port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)


bme280data = bme280.sample(bus, address, calibration_params)
humidity = format(bme280data.humidity, ".1f")
temperature = format(bme280data.temperature, "0.1f")
pressure = format(bme280data.pressure * 100, ".1f")
        
#print("Temperature(C)", temperature)
#print("Humidity(%)", humidity)
#print("Pressure(Pa)", pressure)

out_string = str(temperature) + "-" + str(humidity) + "-" + str(pressure)
#print(out_string)

sys.stdout.write(out_string)
sys.stdout.flush()
sys.exit(0)