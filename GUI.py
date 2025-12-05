#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
from nicegui import ui

# Internal Libraries

class GUI:

    def __init__(self):
        self.fanRunDurationInSeconds = 7
        self.ledBrightnessPercentage = 1.0


    def layout(self):

        with ui.row():
            ui.label('Fan Duration:')
            ui.select([1, 5, 10], value=1)
        with ui.row():
            ui.label('LED Brightness:')
            ui.slider(min=0, max=100, value=100)

    def start(self):
        ui.run(dark=True, title='Komodo Ole Runners Club Project', window_size=(1920, 1080))

if __name__ in {"__main__", "__mp_main__"}:
    gui = GUI()
    gui.layout()
    gui.start()
