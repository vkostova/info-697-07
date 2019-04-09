from microbit import *
import radio
radio.on()

# receiver will show the distance to the beacon
# the number of receivers should be easily adjustable
while True:
    message=radio.receive_full()
    # the stronger the signal the higher the number
    if message:
        strength = message[1]+100
        displaystrength = (int((strength/10)+1))
        display.show(str(displaystrength))
        sleep(200)
    # if beacon is too far, also usable as a sixth level of light intensity
    else:
        display.show(Image.NO)