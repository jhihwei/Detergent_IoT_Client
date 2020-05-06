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
while True:
    temp = cpu.temperature
    mem = psutil.virtual_memory()
    now = datetime.now()
    now = now.strftime("%m/%d/%Y,%H:%M:%S")
    m.publish(now, f'{temp},{mem.free}', "system_info")
    print(cpu.temperature)
    sleep(15)