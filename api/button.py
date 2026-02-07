# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "gpiozero",
# ]
# ///
from gpiozero import Button
import constants

class Button_Handler():
    def __init__(
            self,
            pins
            ):
        self,
        self.pins = pins
        activated_pins = Button(pins)
        self.activated_pins = activated_pins
            
    def _get_function(self,pin):
        #get function from library of constants
        function_map = constants.FUNCTION_MAP
        button_map = function_map.get(pin)
        buttons = self.activated_pins
        button = buttons[pin]
        state_check = getattr(button,'is_active')
        state = state_check()
        action = button_map.get(state)
        return action

    def when_pressed(self):
        button = self.activated_pins
        action = self._get_function(button)
        button.when_activated = action      
        return button.when_activated
