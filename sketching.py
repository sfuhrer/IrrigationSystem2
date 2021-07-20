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

if (hour == 23 and minutes == 31):
    print(now.hour)

DataIntervalSec = 60

TempLast24h = [0]*(int(1*3600/DataIntervalSec))

print(TempLast24h)


import HelperFunctions

for i in range(0,5):
    HelperFunctions.CalcAverage(list, 5)
    print(list)
    # print(list[len(list)-1]