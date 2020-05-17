import serial
import os
# Dot ENV 預載模組-----------------------
from struct import *
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

ser = serial.Serial(
            port=str(os.getenv('SERIAL_PORT')),
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
while True:
    x = ser.read()
    print(x)