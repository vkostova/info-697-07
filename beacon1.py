from microbit import *
import radio
id = "1"
display.show(id)
# low power so the other receiver has to get close
radio.config(power=0)
radio.on()

while True:
    radio.send(id)