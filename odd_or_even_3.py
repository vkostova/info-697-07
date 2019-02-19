from microbit import *
import random

# introduction text
sleep(1000)
display.scroll("Hi! Is the Number Odd or Even?")
display.show(Image.ARROW_E)
sleep(2000)
display.scroll("Odd")
display.show(Image.ARROW_W)
sleep(2000)
display.scroll("Even")

# selecting modes
while True:
    display.scroll("Select Easy")
    display.show(Image.ARROW_W)
    sleep(1000)
    display.scroll("Or Hard")
    display.show(Image.ARROW_E)
    sleep(1000)
    if button_a.was_pressed():
        # easy mode and show how to start game
        display.show(Image.YES)
        sleep(1000)
        display.scroll("shake to start, turn down to stop", wait=False)
        # begin game
        while True:
            if accelerometer.was_gesture("shake"):
                # countdown
                display.show("321", delay=1000)
                display.clear()
                sleep(1000)
                while True:
                    # display random number for 2 seconds
                    numb = random.randint(1, 9)
                    display.show(numb)
                    sleep(2000)
                    # choose even
                    if button_a.was_pressed():
                        if numb % 2 == 0:
                            # correct asnwer
                            display.show(Image.YES)
                            sleep(1000)
                            display.scroll("shake")
                        else:
                            # wrong answer
                            display.show(Image.NO)
                            sleep(1000)
                            display.scroll("shake")
                        break
                    # choose odd
                    if button_b.was_pressed():
                        if numb % 2 == 0:
                            # wrong answer
                            display.show(Image.NO)
                            sleep(1000)
                            display.scroll("shake")
                        else:
                            # correct asnwer
                            display.show(Image.YES)
                            sleep(1000)
                            display.scroll("shake")
                        break
                    # time runs out
                    display.show(Image.NO)
                    sleep(1000)
                    display.scroll("Too slow. shake")
                    break
            # stop the game
            if accelerometer.was_gesture("face down"):
                display.scroll("stop")
                display.clear()
                break
    # hard mode and show how to start game
    if button_b.was_pressed():
        display.show(Image.YES)
        sleep(1000)
        display.scroll("shake to start, turn down to stop", wait=False)
        # begin game
        while True:
            if accelerometer.was_gesture("shake"):
                display.show("321", delay=1000)
                display.clear()
                sleep(1000)
                while True:
                    # display random number for .5 seconds
                    numb = random.randint(1, 9)
                    display.show(numb)
                    sleep(500)
                    # choose even
                    if button_a.was_pressed():
                        if numb % 2 == 0:
                            display.show(Image.YES)
                            sleep(1000)
                            display.scroll("shake")
                        else:
                            display.show(Image.NO)
                            sleep(1000)
                            display.scroll("shake")
                        break
                    # choose odd
                    if button_b.was_pressed():
                        if numb % 2 == 0:
                            display.show(Image.NO)
                            sleep(1000)
                            display.scroll("shake")
                        else:
                            display.show(Image.YES)
                            sleep(1000)
                            display.scroll("shake")
                        break
                    # time runs out
                    display.show(Image.NO)
                    sleep(1000)
                    display.scroll("Too slow. shake")
                    break
            # stop the game
            if accelerometer.was_gesture("face down"):
                break