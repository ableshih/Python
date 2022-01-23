

# Flask

## 範例
https://www.youtube.com/watch?v=AiUzsr5JZgQ

https://gamma-ray-studio.blogspot.com/2021/09/python-flask.html

https://gitlab.com/GammaRayStudio/DevDoc/-/blob/master/Python/002.PythonFlask.md

https://hiskio.com/lives/1151/about

1. Python 3.4 up
2. python -V (Python 3.9.6)
3. pip install -U Flask
4. 建立 app.py (檔名要一致不可改變)
```
    from flask import Flask
    app = Flask(__name__)
    @app.route("/")
    def hello():
        return "Hello, World!"
```
5. 終端機指令執行 (要注意 flask.exe 的路徑)
    $ flask run 
```
PS C:\Users\LC55-14C\Desktop\py> C:\Users\LC55-14C\AppData\Roaming\Python\Python39\Scripts\flask.exe run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
6. 開打瀏覽器 http://127.0.0.1:5000/

7. Ctrl + c 停止

## 問題
```
PS C:\Users\LC55-14C\Desktop\py> flask
flask : 無法辨識 'flask' 詞彙是否為 Cmdlet、函數、指令檔或可執行程式的名稱。請檢查名稱拼字是否正確，如果包含路徑的話，請確認路徑是否正確，然後再
試一次。
位於 線路:1 字元:1
+ flask
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (flask:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

:w
:q

【 Python Flask 入門指南 】
Python Flask 是一種輕量級的網頁框架，只要五行程式碼，就可以架設網頁伺服器 :

步驟一 : 安裝 Flask 套件
$ pip install Flask

步驟二 : 將以下代碼存檔為 app.py

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"

步驟三 : 終端機指令執行 
$ flask run 

出現「Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)」的文字
並且瀏覽器訪問 127.0.0.1:5000，出現 Hello World ，代表架設完成 !

在 Flask 的官網，對於 「micro」 有這樣的定義 :
「輕量並不代表缺少功能，而是在保持核心簡單的情況下，留有擴展空間。
做法就是不為你事先做出決定，只會包含『你需要的一切，而沒有你不需要的』」。

除了說明上述五行程式碼代表的含義，還會延伸幾項後端開發常見的配置:
• URL 路由 - 註解註冊
• Html 回傳 - 網頁模版
• Web API - 資料交換

從 Flask 入門網站開發，可以帶你快速的了解，網頁框架通常會具備的功能，以及累積網站開發後端的知識。

對於後續要了解 Python 在網路領域，相關的技術與應用，例如: 爬蟲的原理或者資料庫的數據分析，都可以大幅提升學習的效率。

【時間軸】
00:00 五行程式碼
02:43 Hello World
04:45 網頁模版
09:24 資料交換
16:15 開發配置

• 源代碼，下載 :
https://gitlab.com/GammaRayStudio/DevelopmentGroup/Python/FlaskSE

• 部落格文章 : 
https://gamma-ray-studio.blogspot.com/2021/09/python-flask.html

• Gitlab 教程文件 :
https://gitlab.com/GammaRayStudio/DevDoc

• Python/002.PythonFlask.md
https://gitlab.com/GammaRayStudio/DevDoc/-/blob/master/Python/002.PythonFlask.md

• git 方式下載
https://youtu.be/QWVQF9UvsDo

• Markdown 檢視器
https://youtu.be/0WzOzNEu8ws

【參考資料】
• Flask 官網 : https://flask.palletsprojects.com/en/2.0.x/
• Tutorialspoint : https://www.tutorialspoint.com/flask/index.htm

