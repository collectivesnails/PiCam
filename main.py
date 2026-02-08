# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "gpiozero"
# ]
# ///
"""PiCam"""

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from api import button
from api import display
from api import send_file
import constants
import os

PINS = constants.PINS


lcd = display.Display()


# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "picamera2",
# ]
# ///


class Camera:

    def __init__(self
                ):
        self = self
        picamera2 = Picamera2()
        self.picamera2 = picamera2

    def picture(self):
        picamera2 = self.picamera2 #Picamera2()
        camera_config = picamera2.create_preview_configuration({"size":(320,180)})
        picamera2.configure(camera_config)
        picamera2.start()
        today = constants.today
        image_file = picamera2.capture_file(f'image.{today}.jpg')
        return image_file

    def start_video(self):
        picamera2 = self.picamera2 #Picamera2()
        video_config = picamera2.create_video_configuration() #ToDo: Attribute not found
        picamera2.configure(video_config)
        encoder = H264Encoder()
        today = constants.today
        video_file = picamera2.start_recording(encoder, f'video.{today}', quality=Quality.HIGH)
        return picamera2, video_file

    def stop_video(self):
        picamera2 = self.picamera2
        picamera2.stop_recording()
        return picamera2
    












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
        cam = Camera()
        
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
