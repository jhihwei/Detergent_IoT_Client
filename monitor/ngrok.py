# Dot ENV 預載模組-----------------------
from struct import *
from datetime import datetime
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
load_dotenv()
# --------------------------------------
# 增加系統路徑---------------------------
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
sys.path.insert(0, libs_dir_path)
# --------------------------------------
from Mqtt_Controller import Mqtt_Controller
import time

while True:
    with open('ngrok.log', 'r', encoding="utf-8") as f:
        sleep(10)
        rs = f.readlines()
        for r in rs:
            print(r)