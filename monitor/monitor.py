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
class Monitor:
    def __init__(self):
        pass
    def take_screenshot(self):
        subprocess.run(["raspi2png "])
        img = cv2.imread("snapshot.png")
        h, w, channels = img.shape
        ratio = h/400
        img = cv2.resize(img, (400, int(w/ratio)), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('output.jpg', img)
if __name__ == "__main__":
    monitor = Monitor()
    monitor.take_screenshot()