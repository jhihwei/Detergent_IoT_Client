# Dot ENV 預載模組-----------------------
from time import sleep
import sys
from struct import *
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
# --------------------------------------
# 增加系統路徑---------------------------
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
sys.path.insert(0, libs_dir_path)
from Mqtt_Controller import Mqtt_Controller
# --------------------------------------

while True:
    try:
        with open('ngrok.log', 'r', encoding="utf-8") as f:
            tunnel = ""
            sleep(3)
            rs = f.readlines()
            for r in rs:
                if(r.index("tunnel")):
                    tunnel = r
            print(tunnel)
    except FileNotFoundError:
        pass
