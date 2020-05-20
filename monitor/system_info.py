from gpiozero import CPUTemperature
import psutil
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
from time import sleep
from dotenv import load_dotenv
load_dotenv()
# --------------------------------------
from Mqtt_Controller import Mqtt_Controller

cpu = CPUTemperature()
m = Mqtt_Controller()
m.set_TOPIC("system_info")
m.set_TOPIC_2("system_info","write")
sleep_time = 5
count = 60
while True:
    temp = cpu.temperature
    mem = psutil.virtual_memory()
    cpu_load = psutil.cpu_percent()
    disk = psutil.disk_usage('/').free / (2**30)
    now = datetime.now()
    now = now.strftime("%m/%d/%Y,%H:%M:%S")
    m.publish(m.get_TOPIC(), now, f'{temp}, {mem.free/1024/1024}, {cpu_load}, {disk}', "system_info")
    print(f'{temp}, {mem.free/1024/1024}, {cpu_load}, {disk}')
    if count > 120/sleep_time:
        print("send write signal")
        m.publish(m.get_TOPIC_2(), now, f'{temp}, {mem.free/1024/1024}, {cpu_load}, {disk}', "system_info")
        count = 0
    else:
        count+=1
    sleep(sleep_time)