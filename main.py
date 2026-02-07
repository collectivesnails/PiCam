# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "gpiozero"
# ]
# ///
"""PiCam"""
from api import button
from api import camera
from api import display
from api import send_file
import constants
import os

PINS = constants.PINS


lcd = display.Display()
cam = camera.Camera()

###############################################

#Available Classes and Methods
def _activate_display():
    lcd = display.Display()
    #lcd.toggle_backlight()
    #lcd.message(text,line,duration)
    return lcd

def _activate_buttons():
    buttons = list()
    for pin in PINS:
        current_pin = button.Button_Handler(pin)
        buttons.append(current_pin)
    #buttons.when_pressed()
    return buttons

def _activate_camera():
    cam = camera.Camera()
    #image = cam.picture()
    #picam2, video_file = cam.start_video()
    #picam2 = cam.stop_video()
    return cam

    file = None # ToDo: Set file variable based on Camera usage.
    file_share = send_file.Immich.send_file(file=file)

def _boot():
    lcd = _activate_display()
    lcd.message(text='Starting PiCam',line=1,duration=3)
    path = os.getcwd()
    info = os.statvfs(path)
    MB_free = round((info.f_bavail * info.f_frsize)/1000000,1)
    lcd.message(text=f'{MB_free}MB available',line=2,duration=3)
    return None

def main():
    # Initialize
    try:
        lcd = _activate_display()
        buttons = _activate_buttons()
        cam = _activate_camera()
        
        # Boot message
        lcd.message(text='Initializing PiCam',line=1,duration=3)
        path = os.getcwd()
        info = os.statvfs(path)
        MB_free = round((info.f_bavail * info.f_frsize)/1000000,1)
        lcd.message(text=f'{MB_free}MB available',line=2,duration=3)
        lcd.clear()
        lcd.message(text='Starting Video',line=1,duration=3)

        # Start Camera
        video = cam.start_video()
        lcd.clear()
        
        # Menu
        lcd.message(text=' 1   2   3   4  ',line=1,duration=5)
    except Exception:
        lcd.clear()


main()
