import paho.mqtt.client as mqtt
import os
from datetime import datetime
import time
import json
import random
from time import sleep

class Mqtt_Controller:
    def __init__(self):
        # *********************************************************************
        # Global
        self.flag_connected = False
        # Current Path
        self.system_path = os.path.dirname(os.path.abspath(__file__))
        # MQTT Config
        self.data_channel_ID = str(os.getenv('CLIENT_ID'))
        self.MQTT_SERVER = "139.162.104.10"
        self.MQTT_PORT = 1883
        self.MQTT_ALIVE = 60
        self.MQTT_TOPIC_1 = f"Sensor/{self.data_channel_ID}/Room1"
        # *********************************************************************
        self.mqtt_client = mqtt.Client(
            f'{self.data_channel_ID}_{random.randint(1, 1000)}', clean_session=False)
        self.mqtt_client.on_disconnect = self.on_disconnect
        try:
            self.mqtt_client.connect(
            self.MQTT_SERVER, self.MQTT_PORT, self.MQTT_ALIVE)
            self.flag_connected = True
            print('MQTT is connected')
        except Exception as e:
            self.mqtt_reconnect()
            
    def set_TOPIC(self, topic:str):
        self.MQTT_TOPIC_1 = f'{topic}/{self.data_channel_ID}'

    def on_disconnect(self, client, userdata, rc):
        self.flag_connected = False
        print("MQTT is Disconnect")
        self.mqtt_reconnect()

    def mqtt_reconnect(self):
        while not self.flag_connected:
            time.sleep(3)
            try:
                print("Try to Connect...")
                self.write_log('log/mqtt_connect_log.txt', '連線中斷並嘗試連線')
                self.mqtt_client.connect(
                    self.MQTT_SERVER, self.MQTT_PORT, self.MQTT_ALIVE)
                self.flag_connected = True
                print("MQTT is Connected")
                self.write_log('log/mqtt_connect_log.txt', '連線成功')
            except Exception as e:
                self.flag_connected = False
                self.write_log('log/mqtt_connect_except_log.txt', str(e))

    def write_log(self, path:str, log:str):
        with open(f'{self.system_path}/{path}','a+', encoding='utf-8') as f:
            now = datetime.now()
            now = now.strftime("%m/%d/%Y,%H:%M:%S")
            f.write(f'{now}:{log}\n')
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
        print("flag:", self.flag_connected)
        if self.flag_connected:
            payload = {"time": datetime, 'value': msg}
            print(f'Received and Send:{datetime},{msg}')
            print(json.dumps(payload))
            self.mqtt_client.publish(
                self.MQTT_TOPIC_1, json.dumps(payload), 0)