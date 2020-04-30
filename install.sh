sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libjasper-dev
sudo apt-get install -y libqtgui4
sudo apt-get install -y python3-pyqt5
sudo apt install -y libqt4-test
curl -sL https://raw.githubusercontent.com/AndrewFromMelbourne/raspi2png/master/installer.sh | bash -

mkdir ~/Detergent_IoT_Client

cd ~/Detergent_IoT_Client

git clone https://github.com/jhihwei/Detergent_IoT_Client.git

pip3 install -r requirements.txt

sudo echo -e 
"[Unit]
    Description=Video Player
    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/player2/player.py
    Type=simple
    RemainAfterExit=yes
    [Install]
    WantedBy=multi-user.target" >> /etc/systemd/system/player.service
sudo systemctl enable player.service
sudo systemctl restart player.service

sudo echo -e 
"[Unit]
    Description=RS232 Controller
    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/RS232/Rs232_Controller.py
    Type=simple
    RemainAfterExit=yes
    [Install]
    WantedBy=multi-user.target" >> /etc/systemd/system/RS232_Controller.service
sudo systemctl enable RS232_Controller.service
sudo systemctl restart RS232_Controller.service

sudo echo -e 
"[Unit]
  Description=Screen Monitor
  [Service]
  User=pi
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/
  ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/monitor.py
  Type=simple
  RemainAfterExit=yes
  [Install]
  WantedBy=multi-user.target" >> /etc/systemd/system/Screen_Monitor.service
sudo systemctl enable Screen_Monitor.service
sudo systemctl restart Screen_Monitor.service

sudo echo -e 
"[Unit]
  Description=Auto Key
  [Service]
  User=root
  ExecStart=sudo /usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/keyboard.py
  Type=simple
  RemainAfterExit=yes
  [Install]
  WantedBy=multi-user.target" >>   /etc/systemd/system/Auto_key.service
sudo systemctl enable Auto_key.service
sudo systemctl restart Auto_key.service