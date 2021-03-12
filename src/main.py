import time
import logger as logger
from datetime import datetime
from bme280_read import bme280_get_states

now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H_%M_%S")

log_file_name = "log_" + current_time + ".txt"
log_file_path = "/home/pi/IrrigationSystem2/log/" + log_file_name
print("created " + log_file_name)

i=1
while i < 100:
    x = bme280_get_states() #hum, temp, pres
    #f = open("../log/" + log_file_name, 'a')
    f = open(log_file_path, 'a')
    logger.log_state(f, x)
    f.close()
    i +=1
    time.sleep(5)
