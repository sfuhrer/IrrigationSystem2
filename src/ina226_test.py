from ina226 import INA226


if __name__ == '__main__':
    sensor = INA226(False)
    voltage = sensor.get_voltage()
    current = sensor.get_current()
    power = sensor.get_power()

    print("volage:")
    print(voltage)

