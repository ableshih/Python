
# Get WiFi Passwords With Python
https://nitratine.net/blog/post/get-wifi-passwords-with-python/

輸入 'netsh wlan show profiles'，將看到存儲的 wifi 配置。

隨後鍵入 'netsh wlan show profile {Profile Name} key=clear'，輸出含網絡密鑰，即 WiFi 密碼。
```
Microsoft Windows [版本 10.0.22000.376]
(c) Microsoft Corporation. 著作權所有，並保留一切權利。


C:\Users\able_\Desktop\PY>netsh wlan show profiles

介面 Wi-Fi 上的設定檔:

群組原則設定檔 (唯讀)
---------------------------------
    <無>

使用者設定檔
-------------
    所有使用者設定檔 : TP-Link_Extender
    所有使用者設定檔 : S8278-5G
    所有使用者設定檔 : S8278    


C:\Users\able_\Desktop\PY>netsh wlan show profiles S8278-5G

介面 Wi-Fi 上的設定檔 S8278-5G:
=======================================================================

已套用: 所有使用者設定檔

設定檔資訊
-------------------
    版本                   : 1
    類型                   : 無線區域網路
    名稱                   : S8278-5G
    控制選項        :
        連線模式           : 自動連線
        網路廣播           : 只有此網路正在廣播時才連線
        AutoSwitch         :不切換到其他網路
        MAC 隨機化         ：已停用

連線設定
---------------------
    SSID 數目              : 1
    SSID 名稱              : "S8278-5G"
    網路類型               : 基礎結構
    無線電波類型           : [ 任何無線電波類型 ]
    廠商擴充                  : 不存在

安全性設定
-----------------
    驗證                   : WPA2-Personal
    加密方式               : CCMP
    驗證                   : WPA2-Personal
    加密方式               : GCMP
    安全性金鑰             : 現在

成本設定
-------------
    成本                   : 不受限制
    壅塞                   ：否
    接近資料限制           ：否
    超過資料限制           ：否
    漫遊                   ：否
    成本來源               ：預設值


C:\Users\able_\Desktop\PY>netsh wlan show profiles S8278-5G key=clear

介面 Wi-Fi 上的設定檔 S8278-5G:
=======================================================================

已套用: 所有使用者設定檔

設定檔資訊
-------------------
    版本                   : 1
    類型                   : 無線區域網路
    名稱                   : S8278-5G
    控制選項        :
        連線模式           : 自動連線
        網路廣播           : 只有此網路正在廣播時才連線
        AutoSwitch         :不切換到其他網路
        MAC 隨機化         ：已停用

連線設定
---------------------
    SSID 數目              : 1
    SSID 名稱              : "S8278-5G"
    網路類型               : 基礎結構
    無線電波類型           : [ 任何無線電波類型 ]
    廠商擴充                  : 不存在

安全性設定
-----------------
    驗證                   : WPA2-Personal
    加密方式               : CCMP
    驗證                   : WPA2-Personal
    加密方式               : GCMP
    安全性金鑰             : 現在
    金鑰內容               : 12345678

成本設定
-------------
    成本                   : 不受限制
    壅塞                   ：否
    接近資料限制           ：否
    超過資料限制           ：否
    漫遊                   ：否
    成本來源               ：預設值


C:\Users\able_\Desktop\PY>python wifi-get-pw.py
Traceback (most recent call last):
  File "C:\Users\able_\Desktop\PY\wifi-get-pw.py", line 3, in <module>
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 2: invalid start byte

```

沒成功 編碼錯誤
```python=
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")
```

```
PS C:\Users\able_\Desktop\PY> & C:/Python39/python.exe c:/Users/able_/Desktop/PY/h.py
Traceback (most recent call last):  
  File "c:\Users\able_\Desktop\PY\h.py", line 3, in <module>    
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 2: invalid start byte

PS C:\Users\able_\Desktop\PY> 

```

沒成功 無顯示任何訊息
```python=
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")
```

沒成功 無顯示任何訊息
加了 # -*- coding: utf-8 -*-
改了 decode('cp950')
```python=
# -*- coding: utf-8 -*-

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp950').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp950').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")
```
