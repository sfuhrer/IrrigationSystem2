#dsfds

import PumpDriver


def Start(TempFilt24):
    
    if (TempFilt24 > 30):
        PumpDuration = 200
    else:
        PumpDuration = 100

    print("Pump controller started, average temperature over last 24h: ", TempFilt24,  "Duration: ", PumpDuration)
    PumpDriver.RunPump(PumpDuration)
    return 0
