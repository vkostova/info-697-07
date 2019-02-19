from microbit import *

# intro
display.scroll("press A to start logging")

while True:
    # start logging by pressing button A
    if button_a.is_pressed():
        display.show(Image.YES)
        sleep(1000)
        while True:
            with open('data.csv', 'w') as csvfile:
                temp = temperature()
                comp = compass.heading()
                data = (str(comp) + ',' + str(temp))
                csvfile.write(data)
                # show reading & start calibrating process
                display.scroll(data)
                # time interval of 5 seconds
                sleep(5000)
                # stop logging by pressing button B
                if button_b.was_pressed():
                    display.show(Image.NO)
                    sleep(1000)
                    # clear the screen
                    display.clear()
                    break
