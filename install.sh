
#!/bin/bash
read -p "enter your ssh port:" "ssh_port"
sudo echo 'gpu_mem=256' >>  /boot/config.txt
sudo echo -e "[Unit]
    Description=Video Player
    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/player2/player.py
    Type=simple
    Restart=always
    RestartSec=1min
    [Install]
    WantedBy=multi-user.target" > /etc/systemd/system/player.service
sudo systemctl enable player.service
sudo systemctl restart player.service

sudo echo -e "[Unit]
    Description=RS232 Controller
    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/RS232/Rs232_Controller.py
    Type=simple
    Restart=always
    RestartSec=1min
    [Install]
    WantedBy=multi-user.target" > /etc/systemd/system/RS232_Controller.service
sudo systemctl enable RS232_Controller.service
sudo systemctl restart RS232_Controller.service

sudo echo -e "[Unit]
  Description=Screen Monitor
  [Service]
  User=pi
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/
  ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/monitor.py
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" > /etc/systemd/system/Screen_Monitor.service
sudo systemctl enable Screen_Monitor.service
sudo systemctl restart Screen_Monitor.service

# sudo echo -e "[Unit]
#   Description=Auto Key
#   [Service]
#   User=root
#   ExecStart=sudo /usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/keyboard.py
#   Type=simple
#   Restart=always
#   RestartSec=1min
#   [Install]
#   WantedBy=multi-user.target" >   /etc/systemd/system/Auto_key.service
# sudo systemctl enable Auto_key.service
# sudo systemctl restart Auto_key.service

sudo mkdir /opt/ngrok
cd /opt/ngrok
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
sudo unzip ngrok-stable-linux-arm.zip
sudo rm ngrok-stable-linux-arm.zip
sudo chmod +x ngrok
sudo chmod 777 ngrok.log

sudo echo -e "[Unit]
  Description=ngrok
  After=network.target
  [Service]
  ExecStart=/opt/ngrok/ngrok tcp 22 --log /opt/ngrok/ngrok.log
  ExecReload=/bin/kill -HUP $MAINPID
  KillMode=process
  IgnoreSIGPIPE=true
  Restart=always
  RestartSec=3
  Type=simple
  [Install]
  WantedBy=multi-user.target" >   /etc/systemd/system/Ngrok.service
sudo systemctl enable Ngrok.service
sudo systemctl restart Ngrok.service

sudo echo -e "[Unit]
  Description=Ngrok_Monitor
  After=Ngrok.service
  [Service]
  User=pi
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/
  ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/ngrok.py
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >   /etc/systemd/system/Ngrok_Monitor.service
sudo systemctl enable Ngrok_Monitor.service
sudo systemctl restart Ngrok_Monitor.service

sudo echo -e "[Unit]
  Description=AutoSSH Service
  After=Ngrok.service
  [Service]
  User=pi
  ExecStart=/usr/bin/autossh -CNR $ssh_port:localhost:22 user@139.162.104.10
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >   /etc/systemd/system/SSH_Tunnel.service
sudo systemctl enable SSH_Tunnel.service
sudo systemctl restart SSH_Tunnel.service

sudo echo -e "[Unit]
  Description=System Info
  After=Ngrok.service
  [Service]
  User=pi
  ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/system_info.py
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >   /etc/systemd/system/system_info.service
sudo systemctl enable system_info.service
sudo systemctl restart system_info.service