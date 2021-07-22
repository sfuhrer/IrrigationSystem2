#dsfds

import PumpDriver


def Start(TempFilt24):
    
    if (TempFilt24 > 30):
        PumpDuration = 200
    else:
        PumpDuration = 100

    string = "Pump controller started, average temp last 24h: " + str(TempFilt24) + " deg " + "Duration: " + str(PumpDuration) + "s"
    print(str)
    PumpDriver.RunPump(PumpDuration)
    return str
