from lib.ina226 import INA226


if __name__ == '__main__':
    sensor = INA226(False)
    volrage = sensor.get_voltage()
    current = sensor.get_current()
    power = sensor.get_power()