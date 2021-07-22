#dsfds

import PumpDriver


def Start(TempFilt24):
    
    if (TempFilt24 > 30):
        PumpDuration = 200
    else:
        PumpDuration = 100

    feedbackString = "Pump controller started, average temp last 24h: " + format(TempFilt24, ".1f") + " deg " + "Duration: " + str(PumpDuration) + "s"
    print(feedbackString)
    PumpDriver.RunPump(PumpDuration)
    return feedbackString
