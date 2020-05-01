# 增加系統路徑---------------------------
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
sys.path.insert(0, libs_dir_path)
# --------------------------------------
# Dot ENV 預載模組-----------------------
from struct import *
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
# --------------------------------------
from Mqtt_Controller import Mqtt_Controller
import time
import serial
class Recevier():
    def __init__(self):
        self.ser = serial.Serial(
            port=str(os.getenv('SERIAL_PORT')),
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.m = Mqtt_Controller()
    def start(self):
        data = ''
        while 1:
            ox = self.ser.read()
            x = ox.hex()
            # with open('record.txt','a+') as fd:
            if ox == b'\xfa':
                now = datetime.now()
                now = now.strftime("%m/%d/%Y,%H:%M:%S")
                self.m.publish(now, data)
                data = ''
                # fd.write('\r\n')
                data = f'{x},'
                # fd.write(f'{now},{data}')
            else:
                data = data+f'{x},'
                # fd.write(f'{x},')


if __name__ == '__main__':
    if str(os.getenv('CLIENT_TYPE')) == 'local' :
        r = Recevier()
        r.start()
    else:
        m = Mqtt_Controller()
        m.start_loop()
