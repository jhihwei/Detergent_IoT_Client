sudo apt install -y libatlas-base-dev
sudo apt install -y libjasper-dev
sudo apt install -y libqtgui4
sudo apt install -y python3-pyqt5
sudo apt install -y libqt4-test
sudo apt install -y python3-opencv
sudo apt install -y libgstreamer1.0-0
sudo apt install -y --reinstall python3-pip
sudo apt install -y autossh
pip3 install --upgrade pip
curl -sL https://raw.githubusercontent.com/AndrewFromMelbourne/raspi2png/master/installer.sh | bash -

git clone https://github.com/jhihwei/Detergent_IoT_Client.git

mkdir ~/Detergent_IoT_Client/player/test_videos

cd ~/Detergent_IoT_Client

pip3 install -r requirements.txt