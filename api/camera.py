from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
import constants

class Camera:

    def __init__(self,
                mode # still | video
                ):
        self.mode = mode
    
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
        picam2.configure(picam2.create_video_configuration())
        encoder = H264Encoder()
        today = constants.today
        video_file = picam2.start_recording(encoder, f'video.{today}', quality=Quality.HIGH)
        return picam2, video_file

    def stop_video(picam2):
        picam2.stop_recording()
        return picam2
    