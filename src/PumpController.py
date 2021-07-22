#dsfds

import PumpDriver


def Start(TempFilt24):
    print("Pump controller started")
    PumpDriver.RunPump(20)
    return 0
