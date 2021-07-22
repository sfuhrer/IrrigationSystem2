import time
import logger as logger
from datetime import datetime
from bme280_read import bme280_get_states
from ina226 import INA226
import PumpController
import HelperFunctions

now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H_%M_%S")

log_file_name = "log_" + current_time + ".txt"
log_file_path = "/home/pi/IrrigationSystem2/log/" + log_file_name
print("created " + log_file_name)

DataIntervalSec = 30

TempLast24h = [0]*int((24*3600/DataIntervalSec))

while True:
    # get measurements
    x = bme280_get_states() #hum, temp, pres
    
    sensor = INA226(False)
    voltage = sensor.get_voltage()
    current = sensor.get_current()
    power = sensor.get_power()

    print(current)

    x.append(voltage)
    x.append(current)

    TempFilt24 = HelperFunctions.CalcAverage(TempLast24h, x[1])
    AverageTemp24 = TempFilt24[-1]
    x.append(AverageTemp24)

    f = open(log_file_path, 'a')

    now = datetime.now()
    # every day at 08.00 start Pump controller
    if (now.hour == 22 and now.minute == 1):
        #logger.log_message(f, "test")
        pumpResult = PumpController.Start(AverageTemp24)
        logger.log_message(f, pumpResult)
        #print(pumpResult)


    # log data
    #f = open("../log/" + log_file_name, 'a')
    
    logger.log_state(f, x)
    f.close()
    
    # sleep for 1min
    time.sleep(DataIntervalSec)
