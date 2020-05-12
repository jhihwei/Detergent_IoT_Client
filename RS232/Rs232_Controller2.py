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
load_dotenv()
# --------------------------------------
from Mqtt_Controller import Mqtt_Controller
import time
import serial
import pip._vendor.requests._internal_utils
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
        self.m.subscribe('rs232')
        self.recipt = 0
        # self.m.mqtt_client.on_message = self.get_data
        # self.m.mqtt_client.loop_forever()
    
    def line_notify(self, data):
        payload = {'message':f'光遠站發票存量：{data}'}  
        headers = {'Authorization': 'Bearer ' + 'Urqc2WCRhwd0Dc3LvyzkyIJsjh4FzRoEvRc4DRE26YL'} 
        requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)

    def get_data(client, userdata, message):
        message = str(message.payload.decode("utf-8"))
        print(message)

    def start(self):
        data = ''
        while 1:
            ox = self.ser.read()
            x = ox.hex()
            if ox == b'\xfa':
                now = datetime.now()
                now = now.strftime("%m/%d/%Y,%H:%M:%S")

                d = data.split(',')
                if len(d) > 10:
                    recipt = f'{d[25]}{d[24]}{d[23]}{d[22]}{d[21]}'
                    if self.recipt == 0:
                        self.recipt = recipt
                    if self.recipt != recipt:
                        self.line_notify(int(recipt))
                        self.recipt = recipt

                self.m.publish(now, data)
                data = f'{x},'
            else:
                data = data+f'{x},'


if __name__ == '__main__':
    if str(os.getenv('CLIENT_TYPE')) == 'local' :
        r = Recevier()
        r.start()
    else:
        m = Mqtt_Controller()
        m.start_loop()
