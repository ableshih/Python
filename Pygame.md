
# Pygame 教學
https://codingtube.tech/1641743920/Pygame-Tutorial-for-Beginners-Python-Game-Development-Course

https://www.youtube.com/playlist?list=PLJPiff845eg-rrjjTsHZIs1k6xTn-p-ij

https://www.pygame.org/

https://blog.techbridge.cc/2019/10/19/how-to-build-up-game-with-pygame-tutorial/

Day27-安裝使用PyGame套件
https://ithelp.ithome.com.tw/articles/10209243

Python遊戲教學
https://pygame.hackersir.org/

PythonTutorials
https://github.com/HackerSir/PygameTutorials

Python — 用pygame玩數獨
https://cde566.medium.com/python-%E7%94%A8pygame%E7%8E%A9%E6%95%B8%E7%8D%A8-ac1e0df6077e


https://www.pygame.org/contribute.html
https://www.pygame.org/project/5596/8108


https://clay-atlas.com/blog/2021/09/07/pygame-cn-download-install-hello-world/

下載並執行 Hello World 程式






簡單的按鈕點擊事件
https://clay-atlas.com/blog/2021/09/13/pygame-cn-button-click-event/

繪製矩形的 Rect 簡單介紹
https://clay-atlas.com/blog/2021/09/10/pygame-cn-rect/

簡單的文字輸入框製作筆記
https://clay-atlas.com/blog/2021/09/09/pygame-cn-input-box/

在視窗中添加背景圖片
https://clay-atlas.com/blog/2021/10/10/pygame-cn-add-background-image-window/

















python -m pip install --upgrade pip
python -m pip install pygame
假如它跳出'python'不是內部或外部命令、可執行的程式或批次檔。的訊息，那可能就是環境變數的部分沒有設定好。在cmd中打上:


## 使用 Python 和 PyGame 遊戲製作入門教學
https://blog.techbridge.cc/2019/10/19/how-to-build-up-game-with-pygame-tutorial/

$ pip install pygame

在開始 PyGame Hello World 之前我們先來認識 PyGame 幾大核心元素：

1. pygame.Surface：Surface 資料型別，代表一個矩形的影像，用來繪製在螢幕上
2. pygame.Rect：Rect 資料型別，用來定位矩形空間的位置和可以用來偵測物件是否碰撞的
3. pygame.event：事件模組，用來處理使用者觸發事件，包含自定義事件
4. pygame.font：文字模組，用來顯示文字，可用來顯示儀表板資料
5. pygame.draw：繪圖模組，可以畫出多邊形圖形，可當作背景物件
6. pygame.image：圖片模組，用來處理載入圖片等相關操作，可當作角色精靈（sprite）
7. pygame.time：時間模組，包含控制遊戲迴圈迭代速率，確保反饋不會太快消逝

## 安裝 Pygame 套件
我們可以直接通過 pip 來安裝

pip install setuptools requests -U
python -m buildconfig
python setup.py install

## 什麼是 pip?
pip 就是 python 內建的 “套件安裝跟管理的工具”
想要使用這個工具 我們只要在 “小黑”(命令提示字元) 打上 pip 就可以了
因為我們今天是要 安裝套件
所以我們可以打

pip install pygame

以此類推 假如我們今天 要裝其他 python 的套件
打上 pip install XXX就可以了

## 做遊戲之前必須具備的觀念
* 遊戲的畫面是由 “渲染” 來的

所謂的 渲染 就是將圖片經由電腦計算 再呈現給我們看的這個過程 至於他要計算能計算什麼 有很多~ 例如光影/透明度和再移動時的呈現 亦或是我們常接觸到的 文字轉圖片 都是需要計算的喔!

* 遊戲的畫面是由 一張一張圖片 快速串連起來的

你可以把她想成是動畫這樣 動畫也可以想成很多張照片快速撥放形成
在這邊我們介紹一個常用專有名詞
< 幀數 FPS(Frame per second) >
表示每秒有幾張圖片串起來 舉個例子 假如是10幀 就代表說每秒
有10張照片 以此可知 越高的幀數會讓畫面看起來越流暢 但相對的需要付出更多的時間計算
也回到我們跟剛剛所說的 需要花更多時間 “渲染”

* 遊戲的畫面是由 一層一層疊上去的

遊戲的渲染跟畫畫不一樣 通常我們在畫畫 會把我們要的主角先畫出來 在把旁邊的地方填上背景 這代表什麼!? 主角後面是沒有背景ㄉ 但是不管事在影片還是遊戲的畫面設計上 我們都是把東西 一層一層疊上去的 先有背景 在把人物疊上去 可以把他想成 Photoshop 的圖層 遊戲中每個元件都是獨立 而且有自己的圖層



* 有了這些觀念之後 我們就可以把 遊戲設計的流程簡化為
思考遊戲規則 > 主畫面設計 > 每個元件的功能設計 > 各個元件的互動 > 遊戲整體優化

## 第三步 - 認識 Pygame 的初始化
我們都知道 pygame 就是拿來寫遊戲的
因此在我們開始寫所謂的 “遊戲內容” 時 當然要先知道怎麼設定一些初始化的東西 像是

*視窗大小啊
*遊戲標題啊
*跟一些物件的呈現
*諸如此類等等
*首先 透過下面語法啟動套件

pygame.init()
接下來 要設定遊戲視窗的大小和視窗標題

screen = pygame.display.set_mode(800*600)
pygame.display.set_caption("這是視窗標題")
## Pygame 中的重要模組
* 方法類
* pygame.display

有關主視窗的 也可以說是最基本ㄉ 遊戲沒有主視窗怎麼跑

常用功能:

.setmode() 設定大小
.display.update()
.set_caption() 設定標題
* pygame.Surface

就是我們前面說的 “圖層” 的概念 這裡面有很多跟圖層有關的方法

* ygame.rect

用來偵測碰撞的

* pygame.draw

用來在 Surface 上畫畫的

* pygame.image

用來管理圖片 例如 圖片ㄉ載入等等

* pygame.font

跟字體有關的
常用功能:

render(文字,平滑值,文字顏色,背景顏色)
pygame.time / pygame.mixer / pygame.sound / pygame.transform

## 物件類
* Surface 物件

其實就是圖層 很多功能都是在圖層上操作 或是會返回一個圖層給你
例如 pygame.display.set_mode() 這個設定主視窗的功能 就會 return 一個 Surface

常用功能:

.blit(畫布變數,繪製位置)
.get_size()
* pygame.sprite.Sprite

這是pygame裡面幫腳色寫好的一個類別 如果要建立腳色 都會需要繼承這個類別
如果不知道什麼是 “類別” 和 “繼承” 的 你可以想成下面這樣
有一個樣板 裡面寫好了很多東西 如果你想要你的創建的物件也使用裡面的東西
就可以透過 “繼承”

因此 pygame.sprite.Sprite 這個類別裡 就幫我們寫好了像是 腳色圖片
腳色碰撞,顯示,群組等等 我們要使用的時候 只要把我們準備好的東西 “代入進去” 就好了

## Pygame - Hello_World!
```python=

import sys

import pygame
from pygame.locals import QUIT

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
window_surface = pygame.display.set_mode((800, 600))
# 設置視窗標題為 Hello World:)
pygame.display.set_caption('Hello World:)')
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Hello World!', True, (0, 0, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (10, 10))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


```
