# 增加系統路徑---------------------------
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
sys.path.insert(0, libs_dir_path)
# --------------------------------------
# Dot ENV 預載模組-----------------------
from Mqtt_Controller import Mqtt_Controller
from time import sleep
import sys
from struct import *
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# --------------------------------------

m = Mqtt_Controller()
m.set_TOPIC('ngrok')
m.subscribe('ngrok')


def get_url(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    if(message == "get"):         
        try:
            with open('ngrok.log', 'r', encoding="utf-8") as f:
                tunnel = "keep move"
                sleep(3)
                rs = f.readlines()
                for r in rs:
                    if(r.find('started tunnel') > 0):
                        tunnel = r
                now = datetime.now()
                now = now.strftime("%m/%d/%Y,%H:%M:%S")
                m.publish(now, tunnel)
        except:
            print("keep move")

m.mqtt_client.on_message = get_url
m.mqtt_client.loop_forever()
