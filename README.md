# 洗衣精販售機IoT-Client
> 於洗衣精販售機中加入嵌入式系統，監控硬體系統，並回傳至雲端分析，提供供應商決策參考。
> 
## 安裝
0. 啟用Serial Port
1. 安裝xscreensaver：
    ```sh
    sudo apt-get install xscreensaver
    ```
2. 安裝相關套件：
    ```sh
    pip3 install -r requirements.txt
    sudo apt install python3-opencv
    ```
3. 啟動Service
## 選用
### Linux 手動回收 已經被 Cache 的記憶體

```sh
/sbin/sysctl -w vm.drop_caches=1
```
加入root排程中 crontab
```sh
10 1   *   *   *    /sbin/sysctl -w vm.drop_caches=1
```
>每天1:10AM執行

### 設定GPU MEM 大小
 /boot/config.txt 加入 gpu_mem=256

### 重啟各項服務
```sh
10 1   *   *   *    /sbin/sysctl -w vm.drop_caches=1
11 1   *   *   *    /bin/systemctl restart SSH_Tunnel.service
12 1   *   *   *    /bin/systemctl restart player.service
13 1   *   *   *    /bin/systemctl restart monitor.py
13 1   *   *   *    /bin/echo "" > /opt/ngrok/ngrok.log
0 */2   *   *   *    /bin/systemctl restart Ngrok.service #每二小時
15 1   *   *   *    /bin/systemctl restart Ngrok_Monitor.service
16 1   *   *   *    /bin/systemctl restart system_info.service

#0 1   *   *   *    /sbin/shutdown -r 0
```
