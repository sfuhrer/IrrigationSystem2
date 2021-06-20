#!/usr/bin/python

import smbus

# ===========================================================================
# Adafruit_I2C Class
# ===========================================================================

class Adafruit_I2C(object):

    def readU16(self, reg, little_endian=True):
        "Reads an unsigned 16-bit value from the I2C device"
        try:
            result = self.bus.read_word_data(self.address,reg)
            # Swap bytes if using big endian because read_word_data assumes little
            # endian on ARM (little endian) systems.
            if not little_endian:
                result = ((result << 8) & 0xFF00) + (result >> 8)
            return result
        except:
            print("error")
        
    def __init__(self, address, busnum=-1, debug=False):
        self.address = address
        # By default, the correct I2C bus is auto-detected using /proc/cpuinfo
        # Alternatively, you can hard-code the bus version below:
        #self.bus = smbus.SMBus(0); # Force I2C0 (early 256MB Pi's)
        self.bus = smbus.SMBus(1); # Force I2C1 (512MB Pi's)
        # self.bus = smbus.SMBus(busnum if busnum >= 0 else Adafruit_I2C.getPiI2CBusNumber())
        self.debug = debug

    def writeList(self, reg, list):
        "Writes an array of bytes using I2C format"
        try:
            if self.debug:
                print ("I2C: Writing list to register 0x%02X:" % reg)
                print (list)
            self.bus.write_i2c_block_data(self.address, reg, list)
        except:
            r#eturn print("error")


if __name__ == '__main__':
    try:
        bus = Adafruit_I2C(address=0)
        print ("Default I2C bus is accessible")
    except:
        print ("Error accessing default I2C bus")
