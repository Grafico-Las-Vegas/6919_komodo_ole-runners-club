
# https://gpiozero.readthedocs.io/en/stable/
from gpiozero import Button
from time import sleep


MAX_DURATION = 10
MIN_DURATION = 1

# Board numbering https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
leftLED = PWMLED("BOARD13")
rightLED = PWMLED("BOARD15")
leftActionButton = Button("BOARD7")
rightActionButton = Button("BOARD11")
leftFan = Fan("BOARD16")
rightFan = Fan("BOARD18")


def turn_on_fan(duration=7):
    if duration > MAX_DURATION:
        duration = MAX_DURATION
    elif duration < 0:
        duration = MIN_DURATION

    leftFan.on()
    rightFan.on()
    sleep(duration)
    leftFan.off()
    rightFan.off()


if __name__ == "__main__":
    gui = GUI()
    gui.start()


    while True:
        leftActionButton.when_pressed = lambda: turn_on_fan()
        rightActionButton.when_pressed = lambda: turn_on_fan()
        sleep(1)
