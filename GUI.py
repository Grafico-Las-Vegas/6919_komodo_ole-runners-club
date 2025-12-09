#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
from nicegui import ui

# Internal Libraries

class GUI:

    def __init__(self):
        self.isFanOn = False
        self.fanRunDurationInSeconds = 7
        self.ledBrightnessPercentage = 100

    def update_fan_config(duration):
        self.fanRunDurationInSeconds = duration

    def update_led_config(self, brightness):
        self.ledBrightnessPercentage = brightness
        print(f"LED Brightness updated to {brightness}%")



    def layout(self, gui):

        with ui.row().classes('w-full items-center'):
            ui.label('Fan Duration (seconds):').classes('w-1/8 text-lg')
            ui.select([1, 5, 10], value=1, on_change=lambda e: update_fan_config(e.value))
            ui.label('LED Brightness:').classes('w-1/10 text-lg')
            ui.slider(min=0, max=100, value=100).classes('w-1/8').on('update:model-value', lambda e: gui.update_led_config(e.args), throttle=1.0)
            ui.button('Turn on Fans', on_click=lambda: print('Turning')).classes('w-1/8')
            ui.button('Turn off Fans', on_click=lambda: print('Turning')).classes('w-1/8')

    def start(self):
        ui.run(native=True, dark=True, title='Komodo Ole Runners Club Project', window_size=(1920, 1080))

if __name__ in {"__main__", "__mp_main__"}:
    gui = GUI()
    gui.layout(gui)
    gui.start()
