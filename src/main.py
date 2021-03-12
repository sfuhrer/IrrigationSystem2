import time
import logger as logger
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H_%M_%S")

log_file_name = "log_" + current_time + ".txt"
# log_file_name = "/home/pi/IrrigationSystem2/log/" + log_file_name + ".txt"

i = 1
while i < 10:
    print(i)
    i += 1
    x = [1, 2, 3]
    f = open("../log/" + log_file_name, 'a')
    logger.log_state(f, x)
    f.close()
    time.sleep(5)



#
# # i2cdetect needed, otherwise I2C connection is not detected by driver
# i2cdetect - y
# 1

# output =$(python / home / pi / IrrigationSystem2 / drivers / bme280_read.py)
#
