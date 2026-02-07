# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "picamera2",
# ]
# ///
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
import constants

class Camera:

    def __init__(self
                ):
        self = self
    
    def _activate(self):
        picam2 = Picamera2()
        return picam2

    def picture(self):
        picam2 = self._activate
        camera_config = picam2.create_preview_configuration({"size":(320,180)})
        picam2.configure(camera_config)
        picam2.start()
        today = constants.today
        image_file = picam2.capture_file(f'image.{today}.jpg')
        return image_file

    def start_video(self):
        picam2 = self._activate
        video_config = picam2.create_video_configuration() #ToDo: Attribute not found
        picam2.configure(video_config)
        encoder = H264Encoder()
        today = constants.today
        video_file = picam2.start_recording(encoder, f'video.{today}', quality=Quality.HIGH)
        return picam2, video_file

    def stop_video(picam2):
        picam2.stop_recording()
        return picam2
    