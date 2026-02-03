#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
import pigpio

# Internal Libraries
import GUI

# Global Objects
# Board numbering https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
#overheadWhiteLED = PWMLED("BOARD13")
leftButtonPWMLED = 23   # GPIO23 & Physical/Board pin 16
rightButtonPWMLED = 24  # GPIO24 & Physical/Board pin 18
leftButtonAction = 5    # GPIO5  & Physical/Board pin 29
rightButtonAction = 6   # GPIO5  & Physical/Board pin 31
fan0PWM = 12            # GPIO12 & Physical/Board pin 32
fan1PWM = 13            # GPIO13 & Physical/Board pin 33
#  https://youtu.be/kluuL5dU2_Q?si=rZGEUGjZx0oBzIgy

# Global Variables
isDoorReady = False  # Door is open, not ready for fan blowing
currentFanState = False
currentFanDuration = GUI.DEFAULT_DURATION
currentFanPercentage = GUI.MAX_PERCENTAGE
currentButtonLedBrightness = GUI.MAX_BRIGHTNESS
currentOverheadBrightness = GUI.MAX_BRIGHTNESS

# Button Array Indicies
BRIGHTNESS = 0
ACTION = 1

PWM_FREQ = 10000  # 10KHz

# Function to change the PWM Duty Cycle
def set_PWM_duty_cycle(piInstance, PWM_FREQ_VALUE, GPIO_NUM, DutyCycle):
    correctedDutyCycle = DutyCycle*10000 # pigpio lib requires Duty Cycle to be in Mega
    piInstance.hardware_PWM(PWM_PIN_OUT, PWM_FREQ_VALUE, correctedDutyCycle)
    print('PWM Duty Cycle Set to = ', DutyCycle)

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

    pi = pigpio.pi()

    gui = GUI()
    gui.start()

    currentFanState = gui.isFanOn
    currentFanDuration = gui.fanRunDurationInSeconds
    currentFanPercentage = gui.fanSpeedInPercentage
    currentOverheadBrightness = gui.whiteLedBrightnessInPercentage
    currentButtonLedBrightness = gui.redLedBrightnessInPercentage

    fans = [fan0PWM, fan1PWM]
    leftButton = [leftButtonLED, leftButtonAction]
    rightButton = [rightButtonLED, rightButtonAction]

    while True:
        sleep(0.100) # Sleep to keep CPU below 80%

        if isDoorReady:
            leftButtonAction.when_pressed = lambda: turn_on_fans(fans)
            rightButtonAction.when_pressed = lambda: turn_on_fans(fans)

        update_button_brightness(currentButtonLedBrightness)
        # update_overhead_brightness(currentOverheadBrightness) - Control with physical button or remote control
