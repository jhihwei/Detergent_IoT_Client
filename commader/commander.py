import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
libs_dir_path = parent_dir_path+'/libs'
# sys.path.insert(0, libs_dir_path)
from Mqtt_Controller  import Mqtt_Controller

print(dir_path)
print(parent_dir_path)
print(libs_dir_path)

m = Mqtt_Controller()