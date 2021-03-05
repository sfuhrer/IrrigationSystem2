import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

with open('../log/2021_03_01_09_17_13.txt') as f:
    lines = f.readlines()

    timestamp_full = [line.split()[0] for line in lines]
    # Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in I020]
    # Time1 = [mdates.date2num(line) for line in Time]
    temp = [float(line.split()[1]) for line in lines]
    temp_ext = [float(line.split()[2]) for line in lines]
    hum = [float(line.split()[3]) for line in lines]
    pres = [float(line.split()[4]) for line in lines]

    temp_np=np.asarray(temp)


def timestamp_to_sec(timestamp):
    length = len(timestamp)
    hrs = int(timestamp[length - 8: length - 6])
    hrs = int(timestamp[length - 8: length - 6])
    minutes = int(timestamp[length - 5: length - 3])
    sec = int(timestamp[length - 2:])
    return hrs * 3600 + minutes * 60 + sec

x_orig = ['2015-12-29 15:01:25', '2015-12-29 15:04:18']
x_orig = ['2021_03_03_07_17_19 ', '2021_03_03_08_17_20 ']
x = [datetime.strptime(d, '%Y-%m-%d-%H:%M:%S') for d in x_orig]
y = ['7.1', '7.4', '9.4', '10.2']

xs = matplotlib.dates.date2num(x)
hfmt = matplotlib.dates.DateFormatter('%Y-%m-%d\n%H:%M:%S')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.patch.set_facecolor('lightgrey')
ax.xaxis.set_major_formatter(hfmt)
ax.set_title('Titel des Reports')
ax.set_xlabel('datum')
ax.set_ylabel('2MTemperatur')
plt.setp(ax.get_xticklabels(), size=8)
ax.plot(xs, y, linewidth=2)
ax.scatter(xs, y)
plt.grid()
plt.show()


timestamp_s = []
for i in timestamp_full:
    timestamp_s.append(timestamp_to_sec(i))

plt.subplot(2, 2, 1)
plt.plot(timestamp_s, temp, 'o-')
plt.title('Some logging')
plt.ylabel('Temp [°C]')

plt.tight_layout()

plt.subplot(2, 2, 2)
plt.plot(temp_ext, '.-')
plt.xlabel('Time [s]')
plt.ylabel('Temp ext')

plt.subplot(2, 2, 3)
plt.plot(timestamp_s, hum, '.-')
plt.xlabel('Time [s]')
plt.ylabel('Hum 2')

plt.subplot(2, 2, 4)
plt.plot(timestamp_s, pres, '.-')
plt.xlabel('Time [s]')
plt.ylabel('pres 2')

plt.show()