# 洗衣精販售機IoT-Client
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
 /boot/config.txt 加入 gpu_mem=128
