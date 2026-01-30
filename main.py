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




# Do I need to do the function heavy methodology, or can I just write top to bottom? 
# The function method allows everything to be declared in advance, but it seems like the classes are already doing that.
# This feels needlessly complicated and it isn't just ... getting tested already.

buttons = button.Button_Handler(PINS)
buttons.when_pressed()
lcd.message(text='Starting PiCam',line=1,duration=3)
path = os.getcwd()
info = os.statvfs(path)
MB_free = round((info.f_bavail * info.f_frsize)/1000000,1)
lcd.message(text=f'{MB_free}MB available',line=2,duration=3)











###############################################
"""
#Available Classes and Methods
def _activate_display():
    lcd = display.Display()
    #lcd.toggle_backlight()
    #lcd.message(text,line,duration)
    return lcd

def _activate_buttons():
    buttons = button.Button_Handler(PINS)
    #buttons.when_pressed()

def _activate_camera():
    cam = camera.Camera()
    #image = cam.picture()
    #picam2, video_file = cam.start_video()
    #picam2 = cam.stop_video()

    file = None #ToDo: Set file variable based on Camera usage.
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
    
    _boot()
    #ToDO: 
    
    message = ' 1   2   3   4  ' # 16 char
    row = 1 # 1| 2
    display_time = 3 # Int
    lcd.message(text=message,line=row,duration=display_time)
    


main()
"""