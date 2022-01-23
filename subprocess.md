
# 使用 subprocess 模块 (cmd)
https://docs.python.org/zh-tw/3.8/library/subprocess.html
subprocess 無法顯示訊息



```python=
# -*- coding: UTF8 -*-

import subprocess

r = subprocess.run(["ping", "google.com"], stdout=subprocess.PIPE)
print(r.stdout.decode('cp950'))
```
```

PS C:\Users\able_\Desktop\PY> & C:/Python39/python.exe c:/Users/able_/Desktop/PY/h.py

Ping google.com [142.251.43.14] (使用 32 位元組的資料):
回覆自 142.251.43.14: 位元組=32 時間=13ms TTL=113
回覆自 142.251.43.14: 位元組=32 時間=11ms TTL=113
回覆自 142.251.43.14: 位元組=32 時間=11ms TTL=113
回覆自 142.251.43.14: 位元組=32 時間=11ms TTL=113

142.251.43.14 的 Ping 統計資料:
    封包: 已傳送 = 4，已收到 = 4, 已遺失 = 0 (0% 遺失)，
大約的來回時間 (毫秒):
    最小值 = 11ms，最大值 = 13ms，平均 = 11ms

PS C:\Users\able_\Desktop\PY>
```


---


```python=
# -*- coding: UTF8 -*-

import subprocess

r = subprocess.run(["ping", "google.com"], stdout=subprocess.PIPE)
print(r)
```
```
PS C:\Users\able_\Desktop\PY> & C:/Python39/python.exe c:/Users/able_/Desktop/PY/h.py
CompletedProcess(args=['ping', 'google.com'], returncode=0, stdout=b'\r\nPing google.com [142.251.43.14] (\xa8\xcf\xa5\xce 32 \xa6\xec\xa4\xb8\xb2\xd5\xaa\xba\xb8\xea\xae\xc6):\r\n\xa6^\xc2\xd0\xa6\xdb 142.251.43.14: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1=16ms TTL=113\r\n\xa6^\xc2\xd0\xa6\xdb 142.251.43.14: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1=11ms TTL=113\r\n\xa6^\xc2\xd0\xa6\xdb 142.251.43.14: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1=11ms TTL=113\r\n\xa6^\xc2\xd0\xa6\xdb 142.251.43.14: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1=10ms TTL=113\r\n\r\n142.251.43.14 \xaa\xba Ping \xb2\xce\xadp\xb8\xea\xae\xc6:\r\n    \xab\xca\xa5]: \xa4w\xb6\xc7\xb0e = 4\xa1A\xa4w\xa6\xac\xa8\xec = 4, \xa4w\xbf\xf2\xa5\xa2 = 0 (0% \xbf\xf2\xa5\xa2)\xa1A\r\n\xa4j\xac\xf9\xaa\xba\xa8\xd3\xa6^\xae\xc9\xb6\xa1 (\xb2@\xac\xed):\r\n    \xb3\xcc\xa4p\xad\xc8 = 10ms\xa1A\xb3\xcc\xa4j\xad\xc8 = 16ms\xa1A\xa5\xad\xa7\xa1 = 12ms\r\n')
PS C:\Users\able_\Desktop\PY> 
```
