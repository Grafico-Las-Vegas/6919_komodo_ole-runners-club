#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
from nicegui import ui

class GUI:

    MAX_PERCENTAGE = 100
    MAX_DURATION = 6
    DEFAULT_DURATION = 3
    MIN_DURATION = 1
    OFF = 0

    MAX_BRIGHTNESS = 100
    MIN_BRIGHTNESS = 0

    powerButtonState = ["On", "Off"]

    def __init__(self):
        self.isFanOn = False
        self.fanRunDurationInSeconds = GUI.DEFAULT_DURATION
        self.fanSpeedInPercentage = GUI.MAX_PERCENTAGE
        self.whiteLedBrightnessInPercentage = GUI.MAX_PERCENTAGE
        self.redLedBrightnessInPercentage = GUI.MAX_PERCENTAGE

        # Button element references
        self.on_button = None
        self.off_button = None

    def update_fan_config(self, duration, speed):
        self.fanRunDurationInSeconds = duration
        self.fanSpeedInPercentage = speed
        print(f"Fan Duration updated to {duration} seconds, at speed of {speed}")

    def update_led_config(self, color="white", brightness=100):
        if color == "white":
            self.whiteLedBrightnessInPercentage = brightness
            print(f"White Overhead LED Brightness updated to {brightness}%")
        elif color == "red":
            self.redLedBrightnessInPercentage = brightness
            print(f"Red Button LED Brightness updated to {brightness}%")
        else:
            print("Warning: LED Brightness not updated!")

    def update_gui_button_colors(self):
        """Set button classes according to current `isFanOn` state."""
        if self.on_button is None or self.off_button is None:
            return

        if self.isFanOn:
            # On is active -> make it green, restore Off to its base red
            self.on_button.classes("!bg-green-600 w-1/4")
            self.off_button.classes("!bg-red-900 w-1/4")
        else:
            # Off is active -> make it green, restore On to its base blue
            self.off_button.classes("!bg-green-600 w-1/4")
            self.on_button.classes("!bg-blue-900 w-1/4")

    def button_pressed(self, key):
        print(f"{key} Button clicked")
        if key == "On":
            self.isFanOn = True
        elif key == "Off":
            self.isFanOn = False

        self.update_gui_button_colors()

    def layout(self):
        with ui.column().classes("w-full gap-8"):
            with ui.row().classes("w-full items-center"):
                ui.label("Fan Duration (seconds):").classes("w-1/4 text-lg")
                ui.select(
                    [1, GUI.DEFAULT_DURATION, 2*GUI.DEFAULT_DURATION],
                    value=GUI.DEFAULT_DURATION,
                    on_change=lambda e: GUI.update_fan_config(
                        e.value, self.fanSpeedInPercentage
                    ),
                )

            with ui.row().classes("w-full items-center"):
                ui.label("Fan Speed (%):").classes("w-1/4 text-lg")
                ui.select(
                    [GUI.OFF, 33, 66, GUI.MAX_PERCENTAGE],
                    value=GUI.MAX_PERCENTAGE,
                    on_change=lambda e: GUI.update_fan_config(
                        self.fanRunDurationInSeconds, e.value
                    ),
                )

            #with ui.row().classes("w-full items-center"):
            #    ui.label("White LED Brightness:").classes("w-1/4 text-lg")
            #    ui.slider(min=0, max=MAX_PERCENTAGE, value=MAX_PERCENTAGE).classes("w-1/4").on(
            #        "update:model-value",
            #        lambda e: gui.update_led_config(e.args),
            #        throttle=1.0,
            #    )

            with ui.row().classes("w-full items-center"):
                ui.label("Red Button LED Brightness:").classes("w-1/4 text-lg")
                ui.slider(min=0, max=GUI.MAX_PERCENTAGE, value=GUI.MAX_PERCENTAGE).classes("w-1/4").on(
                    "update:model-value",
                    lambda e: self.update_led_config(e.args),
                    throttle=1.0,
                )

            with ui.row().classes("w-full items-center"):
                self.on_button = ui.button(
                    "Turn On Fans", on_click=lambda: gui.button_pressed("On")
                ).classes("!bg-blue-900 w-1/4")
                self.off_button = ui.button(
                    "Turn Off Fans", on_click=lambda: gui.button_pressed("Off")
                ).classes("!bg-red-900 w-1/4")

    def start(self):
        # TODO: Make full screen on display selected
        ui.run(
            native=False,
            dark=True,
            title="Komodo Ole Runners Club Project",
            window_size=(940, 640),
        )


if __name__ in {"__main__", "__mp_main__"}:
    gui = GUI()
    gui.layout()
    gui.start()
