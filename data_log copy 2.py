from microbit import *

# intro
display.scroll("press A to start logging")

while True:
    # start logging by pressing button A
    if button_a.is_pressed():
        display.show(Image.YES)
        sleep(1000)
        while True:
            # print data in csv file=(comp, temp) and view in data_capture
            print((compass.heading()), ",", (temperature()))
            # show reading & start calibrating process
            display.scroll(compass.heading(), wait=True)
            sleep(20)
            display.scroll(temperature())
            # time interval of 5 seconds
            sleep(5000)
            # stop logging by pressing button B
            if button_b.was_pressed():
                display.show(Image.NO)
                sleep(1000)
                # clear the screen
                display.clear()
                break