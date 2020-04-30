# sudo apt-get install -y libatlas-base-dev
# sudo apt-get install -y libjasper-dev
# sudo apt-get install -y libqtgui4
# sudo apt-get install -y python3-pyqt5
# sudo apt install -y libqt4-test
# curl -sL https://raw.githubusercontent.com/AndrewFromMelbourne/raspi2png/master/installer.sh | bash -
sudo echo -e "[Unit]
  Description=Screen Monitor \n
  [Service] \n
  User=pi \n
  WorkingDirectory=/home/pi/Detergent_IoT_Client/monitor/ \n
  ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/monitor/monitor.py \n
  Type=simple \n
  RemainAfterExit=yes \n
  [Install] \n
  WantedBy=multi-user.target" >> /etc/systemd/system/test.service 
sudo systemctl enable test.service
sudo systemctl restart test.service