# 洗衣精販售機IoT-Client
## Install
0. 啟用Serial Port
1. 安裝xscreensaver：
    ```sh
    sudo apt-get install xscreensaver
    ```
2. 安裝相關套件：
    ```sh
    pip3 install -r requirements.txt
    ```
3. 建立Unit File：
* player
    ```sh
    /etc/systemd/system/player.service
    ```
    ```sh
    [Unit]
    Description=Video Player

    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/player/player.py
    Type=simple
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target
    ```
* RS232_Controller
    ```sh
    /etc/systemd/system/RS232_Controller.service
    ```
    ```sh
    [Unit]
    Description=RS232 Controller

    [Service]
    User=pi
    ExecStart=/usr/bin/python3 /home/pi/Detergent_IoT_Client/RS232/Rs232_Controller.py
    Type=simple
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target
    ```
4. 啟動Service
