import paho.mqtt.client as mqtt
from datetime import datetime
from struct import *
import random
import json
from time import sleep
# Dot ENV 預載模組-----------------------
from dotenv import load_dotenv
import os
load_dotenv()
# --------------------------------------


class Mqtt_Controller:
    def __init__(self):
        # *********************************************************************
        # MQTT Config
        self.data_channel_ID = str(os.getenv('detergent_01'))
        MQTT_SERVER = "139.162.104.10"
        MQTT_PORT = 1883
        MQTT_ALIVE = 60
        self.MQTT_TOPIC_1 = "Sensor/" + self.data_channel_ID + "/Room1"
        # *********************************************************************
        self.mqtt_client = mqtt.Client(self.data_channel_ID, clean_session=False)
        self.mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

    def start_loop(self):
        while True:
            t0 = random.randint(0, 30)
            payload = {"data_channel_ID": f'{self.data_channel_ID}_{random.randint(1, 1000)}', "value": t0}
            print(f'sensor : {t0}')
            self.mqtt_client.publish(self.MQTT_TOPIC_1, json.dumps(payload), 0)
            sleep(0.7)
            
    def publish(self, datetime:str, msg: str):
        payload = { "time":datetime, 'value': msg}
        print(f'Received and Send:{datetime},{msg}')
        self.mqtt_client.publish(self.MQTT_TOPIC_1, json.dumps(payload), 1)


class Recevier():
    import time
    import serial
    ser = serial.Serial(
        port='/dev/ttyS0',
        # port='COM1',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    counter = 0
    m = Mqtt_Controller()
    data = ''
    while 1:
        ox = ser.read()
        x = ox.hex()
        # with open('record.txt','a+') as fd:
        if ox == b'\xfa':
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
            m.publish(date_time,data)
            data = ''
                #fd.write('\r\n')
            data = f'{x},'
                #fd.write(f'{date_time},{data}')
        else:
            data = data+f'{x},'
                #fd.write(f'{x},')

if __name__ == '__main__':
   Recevier()
