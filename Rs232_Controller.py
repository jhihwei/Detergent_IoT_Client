# Dot ENV 預載模組-----------------------
from dotenv import load_dotenv
import os
load_dotenv()
# --------------------------------------
import paho.mqtt.client as mqtt
from datetime import datetime
from struct import *
import random
import json
from time import sleep
class Mqtt_Controller:
    def __init__(self):
        # *********************************************************************
        # Global
        self.flag_connected = True
        # MQTT Config
        self.data_channel_ID = str(os.getenv('CLIENT_ID'))
        self.MQTT_SERVER = "139.162.104.10"
        self.MQTT_PORT = 1883
        self.MQTT_ALIVE = 60
        self.MQTT_TOPIC_1 = "Sensor/" + self.data_channel_ID + "/Room1"
        # *********************************************************************
        self.mqtt_client = mqtt.Client(
            self.data_channel_ID, clean_session=False)
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.connect(
            self.MQTT_SERVER, self.MQTT_PORT, self.MQTT_ALIVE)

    def start_loop(self):
        print('Start Loop...')
        while True:
            t0 = random.randint(0, 30)
            payload = {
                "data_channel_ID": f'{self.data_channel_ID}_{random.randint(1, 1000)}', "value": t0}
            if self.flag_connected == 1:
                now = datetime.now()
                now = now.strftime("%m/%d/%Y,%H:%M:%S")
                self.publish(now, f'sensor : {t0}')
            sleep(1)

    def publish(self, datetime: str, msg: str):
        # self.mqtt_client.connect(
        #     self.MQTT_SERVER, self.MQTT_PORT, self.MQTT_ALIVE)
        print("flag:", self.flag_connected)
        if self.flag_connected == 1:
            payload = {"time": datetime, 'value': msg}
            print(f'Received and Send:{datetime},{msg}')
            self.mqtt_client.publish(self.MQTT_TOPIC_1, json.dumps(payload), 1)

    def on_disconnect(self, client, userdata, rc):
        self.flag_connected = False
        print("MQTT is Disconnect")
        while self.flag_connected:
            time.sleep(3)
            try:
                print("Try to Connect...", self.flag_connected)
                self.mqtt_client.connect(
                    self.MQTT_SERVER, self.MQTT_PORT, self.MQTT_ALIVE)
                self.flag_connected = True
                with open('mqtt_log.txt', 'a+') as fd:
                    fd.write("Try to Connect to MQTT")
            except:
                self.flag_connected = False
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
