#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
from gpiozero import PWMLED, Button, Device, Fan, MockFactory

# Internal Libraries
import GUI

# Global Objects
# Board numbering https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
overheadWhiteLED = PWMLED("BOARD13")
leftButtonLED = PWMLED("BOARD13")
rightButtonLED = PWMLED("BOARD15")
leftButtonAction = Button("BOARD7")
rightButtonAction = Button("BOARD11")
fan0 = Fan("BOARD16")  # or PWMLED() maybe
fan1 = Fan("BOARD18")  # or PWMLED() maybe

# Global Variables
isDoorReady = False  # Door is open, not ready for fan blowing
currentFanState = False
currentFanDuration = GUI.DEFAULT_DURATION
currentFanPercentage = GUI.MAX_DURATION
currentButtonLedBrightness = GUI.MAX_BRIGHTNESS
currentOverheadBrightness = GUI.MAX_BRIGHTNESS

# Button Array Indicies
BRIGHTNESS = 0
ACTION = 1


def turn_on_fans(fans):
    if currentFanDuration > GUI.MAX_DURATION:
        currentFanDuration = GUI.MAX_DURATION
    if currentFanDuration <= 0:
        currentFanDuration = GUI.MIN_DURATION

    for fan in fans:
        fan.on()

    sleep(currentFanDuration)

    for fan in fans:
        fan.off()


def update_button_brightness(buttons, percentage=GUI.MAX_BRIGHTNESS):
    if percentage > GUI.MAX_BRIGHTNESS:
        percentage = GUI.MAX_BRIGHTNESS
    if percentage < 0:
        percentage = GUI.MIN_BRIGHTNESS

    for button in buttons:
        button[BRIGHTNESS].pwm(percentage)


def update_overhead_brightness(percentage=GUI.MAX_BRIGHTNESS):
    if percentage > GUI.MAX_BRIGHTNESS:
        percentage = GUI.MAX_BRIGHTNESS
    if percentage < 0:
        percentage = GUI.MIN_BRIGHTNESS

    overheadWhiteLED.pwm(percentage)


if __name__ == "__main__":
    Device.pin_factory = MockFactory()

    gui = GUI()
    gui.start()

    currentFanState = gui.isFanOn
    currentFanDuration = gui.fanRunDurationInSeconds
    currentFanPercentage = gui.fanSpeedInPercentage
    currentOverheadBrightness = gui.whiteLedBrightnessInPercentage
    currentButtonLedBrightness = gui.redLedBrightnessInPercentage

    # Button element references
    self.on_button = None
    self.off_button = None

    fans = [fan0, fan1]
    leftButton = [leftButtonLED, leftButtonAction]
    rightButton = [rightButtonLED, rightButtonAction]

    while True:
        if isDoorReady:
            leftButtonAction.when_pressed = lambda: turn_on_fans(
                fans, currentFanDuration
            )
            rightButtonAction.when_pressed = lambda: turn_on_fans(
                fans, currentFanDuration
            )
            sleep(0.100)

        update_button_brightness(currentButtonLedBrightness)
        update_overhead_brightness(currentOverheadBrightness)
