import matplotlib.pyplot as plt

with open('2021-01-17_18-54-58.txt') as f:
    lines = f.readlines()

    timestamp_full = [line.split()[0] for line in lines]
    temp = [line.split()[1] for line in lines]


def timestamp_to_sec(timestamp):
    length = len(timestamp)
    hrs = int(timestamp[length - 8: length - 6])
    hrs = int(timestamp[length - 8: length - 6])
    minutes = int(timestamp[length - 5: length - 3])
    sec = int(timestamp[length - 2:])
    return hrs * 3600 + minutes * 60 + sec


timestamp_s = []
for i in timestamp_full:
    timestamp_s.append(timestamp_to_sec(i))

plt.subplot(2, 1, 1)
plt.plot(timestamp_s, temp, 'o-')
plt.title('Some logging')
plt.ylabel('Temp [°C]')

plt.subplot(2, 1, 2)
plt.plot(timestamp_s, temp, '.-')
plt.xlabel('Time [s]')
plt.ylabel('Temp 2')

plt.show()