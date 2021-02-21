import time 
import smbus2
import bme280
 
# --------- User Settings ---------
SECONDS_BETWEEN_READS = 1
# ---------------------------------

# BME280 settings 
port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

while True:
        bme280data = bme280.sample(bus, address, calibration_params)
        humidity = format(bme280data.humidity, ".1f")
        temperature = bme280data.temperature
        pressure = format(bme280data.pressure * 100, ".1f")
        
        
        print("Temperature(C)", temperature)
        print("Humidity(%)", humidity)
        print("Pressure(Pa)", pressure)

        time.sleep(SECONDS_BETWEEN_READS)