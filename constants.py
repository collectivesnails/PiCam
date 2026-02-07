# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datetime",
# ]
# ///
from datetime import date

today = date.today()

PINS = [21,20,16,26] #21:White 20:Black 16:Green 26:Blue
FUNCTION_MAP = {'21':{
                    '0':'CYCLE_THROUGH_RECENT_VIDEOS()',
                    '1':'DELETE_SELECTED_VIDEO()'
                    },
                '20':{
                    '0':'lcd.toggle_backlight()',
                    '1':'lcd.toggle_backlight()'
                    },
                '16':{
                    '0':'cam.stop_video()',
                    '1':'cam.stop_video()'
                    },
                '26':{
                    '0':'cam.start_video()',
                    '1':'cam.stop_video()'
                    }
                }
