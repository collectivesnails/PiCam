#! /usr/bin/env python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "time",
# ]
# ///
from lcd import drivers
from time import sleep

class Display:

    def __init__(
            self
            ):
        self
        display = drivers.Lcd()
        self.display = display

    def toggle_backlight(self):
        self.display.lcd_backlight()
        return None

    def clear(self):
        self.display.lcd_clear()
        return None

    def message(self,
                text:str, #16 char max
                line:str, # 1|2
                duration:int #Int
                ):
            display = self.display
            print("Writing to display")
            display.lcd_display_string(f"{text}", line)
            sleep(duration)