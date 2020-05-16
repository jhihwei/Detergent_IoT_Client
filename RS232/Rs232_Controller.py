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
        # self.m.mqtt_client.on_message = self.get_data
        # self.m.mqtt_client.loop_forever()

    def get_data(client, userdata, message):
        message = str(message.payload.decode("utf-8"))
        print(message)

    def start(self):
        data = ''
        while 1:
            ox = self.ser.read()
            x = ox.hex()
            # 完整的訊息含逗號，長度為84
            if ox == b'\xfa' and len(data) == 84:
                d = data.split(',')
                # 最後一個為[]，倒數第二個為chksum
                chksum = d[-2]
                # 由0至倒數第三個(不含第三個)為資料
                d = d[:-3]
                if chksum == self.checksum(d):
                    now = datetime.now()
                    now = now.strftime("%m/%d/%Y,%H:%M:%S")
                    self.m.publish(now, data)
                    data = ''
                    data = f'{x},'
            else:
                data = data + f'{x},'

    def checksum(self, data):
        ans = 0
        for i in data:
            ans += int(i, 16)
        ans = (ans ^ 0x55) & 0x7F
        return hex(ans).lstrip("0x")


if __name__ == '__main__':
    if str(os.getenv('CLIENT_TYPE')) == 'local' :
        r = Recevier()
        r.start()
    else:
        m = Mqtt_Controller()
        m.start_loop()
