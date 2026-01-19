#!/usr/bin/env python3

# Standard Library
from time import sleep

# 3rd Party Libraries
from nicegui import ui

# Internal Libraries

class GUI:

    buttons = ['On', 'Off']

    def __init__(self):
        self.isFanOn = False
        self.fanRunDurationInSeconds = 7
        self.ledBrightnessPercentage = 100

        # Button element references
        self.on_button = None
        self.off_button = None

    def update_fan_config(self, duration):
        self.fanRunDurationInSeconds = duration
        print(f"Fan Duration updated to {duration} seconds")

    def update_led_config(self, brightness):
        self.ledBrightnessPercentage = brightness
        print(f"LED Brightness updated to {brightness}%")

    def update_button_colors(self):
        """Set button classes according to current `isFanOn` state."""
        if self.on_button is None or self.off_button is None:
            return

        if self.isFanOn:
            # On is active -> make it green, restore Off to its base red
            self.on_button.classes('!bg-green-600 w-1/4')
            self.off_button.classes('!bg-red-900 w-1/4')
        else:
            # Off is active -> make it green, restore On to its base blue
            self.off_button.classes('!bg-green-600 w-1/4')
            self.on_button.classes('!bg-blue-900 w-1/4')


    def button_pressed(self, key):
        print(f"{key} Button clicked")
        if key == 'On':
            self.isFanOn = True
        elif key == 'Off':
            self.isFanOn = False

        self.update_button_colors()

    def layout(self, gui):

        with ui.column().classes('w-full gap-8'):
            with ui.row().classes('w-full items-center'):
                ui.label('Fan Duration (seconds):').classes('w-1/4 text-lg')
                ui.select([1, 5, 10], value=1, on_change=lambda e: gui.update_fan_config(e.value))

            with ui.row().classes('w-full items-center'):
                ui.label('White LED Brightness:').classes('w-1/4 text-lg')
                ui.slider(min=0, max=100, value=100).classes('w-1/4').on('update:model-value', lambda e: gui.update_led_config(e.args), throttle=1.0)

            with ui.row().classes('w-full items-center'):
                 self.on_button = ui.button('Turn On Fans', on_click=lambda: gui.button_pressed('On')).classes('!bg-blue-900 w-1/4')
                 self.off_button = ui.button('Turn Off Fans', on_click=lambda: gui.button_pressed('Off')).classes('!bg-red-900 w-1/4')


    def start(self):
        ui.run(native=False, dark=True, title='Komodo Ole Runners Club Project', window_size=(940, 640))

if __name__ in {"__main__", "__mp_main__"}:
    gui = GUI()
    gui.layout(gui)
    gui.start()
