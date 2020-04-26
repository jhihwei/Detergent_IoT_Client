# 增加系統路徑---------------------------
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
sys.path.insert(0, libs_dir_path)
# --------------------------------------
# Dot ENV 預載模組-----------------------
from struct import *
from datetime import datetime
from dotenv import load_dotenv
# load_dotenv()
load_dotenv(dotenv_path="/home/pi/Detergent_IoT_Client/.env")
# --------------------------------------
import subprocess
import cv2
import base64
from Mqtt_Controller import Mqtt_Controller
class Monitor:
    def __init__(self):
        pass

    def take_screenshot(self):
        subprocess.run(["raspi2png"])
        img = cv2.imread("snapshot.png")
        h, w, channels = img.shape
        # resize img and save it
        ratio = 320
        h_ratio = h/ratio
        h = int(h/h_ratio)
        w = int(w/h_ratio)
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('output.jpg', img)

    def convert_img_to_base64(self, image_path:str):
        with open(f'{image_path}', "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read())
            return img_base64.decode('utf-8')

if __name__ == "__main__":
    monitor = Monitor()
    monitor.take_screenshot()
    img_base64 = monitor.convert_img_to_base64('output.jpg')
    m = Mqtt_Controller()
    m.set_TOPIC('screenshot')
    now = datetime.now()
    now = now.strftime("%m/%d/%Y,%H:%M:%S")
    m.publish(now, "no")
    print(m.get_TOPIC())
