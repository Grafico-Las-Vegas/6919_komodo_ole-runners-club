#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
# TODO: Remove unused import "Device"
from gpiozero import Device
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero.pins.mock import MockFactory
from gpiozero import Button, PWMOutputDevice, DigitalOutputDevice

# Internal Libraries
from GUI import *

# Global Variables
isDoorReady = False  # Door is open, not ready for fan blowing
currentFanState = False
#currentFanDuration = GUI.DEFAULT_DURATION
currentFanPercentage = GUI.MAX_PERCENTAGE

# Global Constants
PWM_FREQ = 10000  # 10KHz

# Global Objects
# Board Numbering: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
# Button / Sensor: https://gpiozero.readthedocs.io/en/stable/recipes.html#button
# PWM Control:     https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice
Device.pin_factory = LGPIOFactory()
#Device.pin_factory = MockFactory()
activationButton = Button(4, pull_up=True)    # GPIO4  & Physical/Board pin 7
topDoorSensor = Button(17, pull_up=True)         # GPIO17 & Physical/Board pin 11
bottomDoorSensor = Button(27, pull_up=True)      # GPIO27 & Physical/Board pin 13
fan0PWM = PWMOutputDevice(23, active_high=True, frequency=PWM_FREQ)            # GPIO23 & Physical/Board pin 16
fan1PWM = PWMOutputDevice(24, active_high=True, frequency=PWM_FREQ)            # GPIO24 & Physical/Board pin 18
chiller1Power = DigitalOutputDevice(6, active_high=True)                       # GPIO6 & Physical/Board pin 31  First Stage Unit A
chiller2Power = DigitalOutputDevice(13, active_high=True)                      # GPIO13 & Physical/Board pin 33 Second Stage Unit A
chiller3Power = DigitalOutputDevice(19, active_high=True)                      # GPIO19 & Physical/Board pin 35 First Stage Unit B
chiller4Power = DigitalOutputDevice(26, active_high=True)                      # GPIO26 & Physical/Board pin 37 Second Stage Unit B


def turn_on_fans(fans):
    """ Turn on fans for a GUI specified duration.
        https://youtu.be/kluuL5dU2_Q?si=rZGEUGjZx0oBzIgy

    Args:
        fans (list): List of fans to turn on.
    """
    if currentFanDuration > GUI.MAX_DURATION:
        currentFanDuration = GUI.MAX_DURATION
    if currentFanDuration <= 0:
        currentFanDuration = GUI.MIN_DURATION

    for fan in fans:
        fan.value = currentFanPercentage / 100
        fan.on()

    print(f"Turning on fans for {currentFanDuration} seconds")
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


if __name__ == "__main__":

    gui = GUI()
    gui.start()

    fans = [fan0PWM, fan1PWM]

    while True:
        currentFanState = gui.isFanOn
        currentFanDuration = gui.fanRunDurationInSeconds
        currentFanPercentage = gui.fanSpeedInPercentage

        sleep(0.100) # Sleep to keep CPU below 80%

        if topDoorSensor.is_pressed or bottomDoorSensor.is_pressed:
            isDoorReady = True
        else:
            isDoorReady = False

        if isDoorReady:
            activationButton.when_pressed = turn_on_fans(fans)
