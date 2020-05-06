from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()

while True:
    sleep(5)
    temp = cpu.temperature
    write_temp(temp)