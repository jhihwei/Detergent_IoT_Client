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
from Data_Format import Data_Format
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
        self.income = 0
        self.m = Mqtt_Controller()
        self.m.set_TOPIC_2('Sensor', 'write')
        print(self.m.get_TOPIC_2)
        print(self.m.get_TOPIC)
        # self.m.subscribe('rs232')
        # self.m.mqtt_client.on_message = self.get_data
        # self.m.mqtt_client.loop_forever()

    def get_data(client, userdata, message):
        message = str(message.payload.decode("utf-8"))
        print(message)

    def start(self):
        data = ''
        d_format = Data_Format()
        while 1:
            ox = self.ser.read()
            x = ox.hex()
            # 完整的訊息含逗號，長度為84
            if x == 'fa' and len(data) > 83:
                d = data.split(',')
                # 最後一個為[]，倒數第二個為chksum，。如果serial讀取有誤chksum為ff
                chksum = d[-2] if len(d[-2]) > 0 else 'ff'
                # 由0至倒數第三個(不含第三個)為資料
                d = d[:-3]
                try:
                    if int(chksum, 16) == int(self.checksum(d), 16):
                        _,_,_,income,_ = d_format.extract_data(d)
                        now = datetime.now()
                        now = now.strftime("%m/%d/%Y,%H:%M:%S")
                        self.m.publish(self.m.get_TOPIC(), now, data)
                        data = 'fa,'

                        if self.check_income(income):
                            print('send write signal')
                            self.income = income
                            self.m.publish('Sensor/detergent_client_002/write', now, data)
                    else:
                        print('checksum error.')
                        data = 'fa,'
                except:
                    data = 'fa,'
            else:
                #如果serial讀取有誤，填入00
                if len(x) < 1:
                    x = '00'
                data = data + f'{x},'

    def check_income(self, income):
        if self.income != income:
            return True
        else:
            return False

    def checksum(self, data):
        ans = 0
        try:
            for i in data:
                ans += int(i, 16)
            ans = (ans ^ 0x55) & 0x7F
            return hex(ans).lstrip("0x")
        except:
            return "xx"


if __name__ == '__main__':
    if str(os.getenv('CLIENT_TYPE')) == 'local' :
        r = Recevier()
        r.start()
    else:
        m = Mqtt_Controller()
        m.start_loop()
