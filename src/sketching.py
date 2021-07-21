list = [1,2,0,0,0,0]

# print(list)

# print ([i for i, e in enumerate(list) if e != 0])
# print([item for item in list if item != 0])


# print(list)

import datetime

now = datetime.datetime.now()
hour = now.hour
minutes = now.minute

print(minutes)

print("Pump controller started")

if (hour == 23 and minutes == 31):
    print(now.hour)

DataIntervalSec = 60

TempLast24h = [0]*(int(1*900/DataIntervalSec))

print(TempLast24h)


import PumpController

import HelperFunctions

for i in range(0,5):
    HelperFunctions.CalcAverage(TempLast24h, 5)
    print(TempLast24h)
    # print(list[len(list)-1]

test = [1.233, 1.456, 3.45, 3.44, 1.4445, 9.009]

print(test)

for idx, val in enumerate(test):
    if (idx) == 0:
        print(val)

import logger


meas = -2.3

print(format(meas, "0.2f"))
