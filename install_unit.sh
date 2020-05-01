
sudo echo -e "[Unit]
    Description=Video Player
    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/player2/player.py
    Type=simple
    Restart=always
    RestartSec=1min
    [Install]
    WantedBy=multi-user.target" >> /etc/systemd/system/player.service
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
    WantedBy=multi-user.target" >> /etc/systemd/system/RS232_Controller.service
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
  WantedBy=multi-user.target" >> /etc/systemd/system/Screen_Monitor.service
sudo systemctl enable Screen_Monitor.service
sudo systemctl restart Screen_Monitor.service

sudo echo -e "[Unit]
  Description=Auto Key
  [Service]
  User=root
  ExecStart=sudo /usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/keyboard.py
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >>   /etc/systemd/system/Auto_key.service
sudo systemctl enable Auto_key.service
sudo systemctl restart Auto_key.service

sudo echo -e "[Unit]
  Description=Ngrok
  [Service]
  User=root
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/
  ExecStart=/opt/ngrok/ngrok tcp 22 --log ngrok.log
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >>   /etc/systemd/system/Ngrok.service
sudo systemctl enable Ngrok.service
sudo systemctl restart Ngrok.service

sudo echo -e "[Unit]
  Description=Ngrok_Monitor
  After=Ngrok.service
  [Service]
  User=pi
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/
  ExecStart=/opt/ngrok/ngrok --log ngrok.log tcp 22
  Type=simple
  Restart=always
  RestartSec=1min
  [Install]
  WantedBy=multi-user.target" >>   /etc/systemd/system/Ngrok_Monitor.service
sudo systemctl enable Ngrok_Monitor.service
sudo systemctl restart Ngrok_Monitor.service