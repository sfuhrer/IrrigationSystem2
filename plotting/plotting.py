import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates

with open('../log/2021_03_06_09_59_33.txt') as f:
    lines = f.readlines()

    timestamp_full = [line.split()[0] for line in lines]
    time_datetime = [datetime.strptime(d, '%Y-%m-%d_%H:%M:%S') for d in timestamp_full]
    # Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in I020]
    # Time1 = [mdates.date2num(line) for line in Time]
    temp_int = [float(line.split()[1]) for line in lines]
    temp_ext = [float(line.split()[2]) for line in lines]
    hum = [float(line.split()[3]) for line in lines]
    pres = [float(line.split()[4]) for line in lines]


def timestamp_to_sec(timestamp):
    length = len(timestamp)
    hrs = int(timestamp[length - 8: length - 6])
    hrs = int(timestamp[length - 8: length - 6])
    minutes = int(timestamp[length - 5: length - 3])
    sec = int(timestamp[length - 2:])
    return hrs * 3600 + minutes * 60 + sec


xs = matplotlib.dates.date2num(time_datetime)
# hfmt = matplotlib.dates.DateFormatter('%Y-%m-%d\n%H:%M:%S')
hfmt = mdates.DateFormatter('%H:%M:%S')

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.patch.set_facecolor('lightgrey')
ax1.xaxis.set_major_formatter(hfmt)
ax1.set_xlabel('Time')
ax1.set_ylabel('Temp [°]')
plt.setp(ax1.get_xticklabels(), size=8)
ax1.plot(xs, temp_ext, linewidth=2)
ax1.xaxis.set_major_formatter(hfmt)
plt.grid()

# add a subplot that shares the x-axis with ax1
ax2 = plt.subplot(212, sharex=ax1)
ax2.patch.set_facecolor('lightgrey')
ax2.xaxis.set_major_formatter(hfmt)
ax2.set_xlabel('Time')
ax2.set_ylabel('Humidity [%]')
plt.setp(ax2.get_xticklabels(), size=8)
ax2.plot(xs, hum, linewidth=2)
ax2.xaxis.set_major_formatter(hfmt)

plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.grid()
plt.show()