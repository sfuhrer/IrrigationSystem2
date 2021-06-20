import time
import logger as logger
from datetime import datetime
from bme280_read import bme280_get_states
from ina226 import INA226

now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H_%M_%S")

log_file_name = "log_" + current_time + ".txt"
log_file_path = "/home/pi/IrrigationSystem2/log/" + log_file_name
print("created " + log_file_name)

while True:
    # get measurements
    x = bme280_get_states() #hum, temp, pres
    
    sensor = INA226(False)
    voltage = sensor.get_voltage()
    current = sensor.get_current()
    power = sensor.get_power()

    x.append(voltage)
    x.append(current)

    # log data
    #f = open("../log/" + log_file_name, 'a')
    f = open(log_file_path, 'a')
    logger.log_state(f, x)
    f.close()
    
    # sleep for 1min
    time.sleep(60)
