```

https://www.apachefriends.org/zh_tw/download.html

=============================================
PyQt5 Tutorial – How to Create MySQL Database in PyQt5
https://codeloop.org/pyqt5-tutorial-how-to-create-mysql-database-in-pyqt5/

開啟 MySQL Workbench

安裝
pip install mysql-connector-python
建立
Qt Designer
轉檔方法一
pyuic5 mydatabase.ui -o mydatabase.py -x
轉檔方法二
vscode 右鍵 PYQT:Compile

合 code
執行
回 MySQL Workbench
就可見卬增加資料庫
=============================================




PyQt5

MySQL in PyQt5

PyQt5教程–在PyQt5中使用MySQL進行簡單登錄
https://codeloop.org/pyqt5-tutorial-simple-login-with-mysql-in-pyqt5/

如何在PyQt5中創建MySQL數據庫
如何在PyQt5中將數據插入Mysql數據庫
在QTableWidget中從Mysql數據庫中選擇數據



如何在PyQt5中創建MySQL數據庫
https://codeloop.org/pyqt5-tutorial-how-to-create-mysql-database-in-pyqt5/


如何在PyQt5中將數據插入Mysql數據庫
https://codeloop.org/pyqt5-tutorial-how-to-insert-data-in-mysql-database/


在QTableWidget中從Mysql數據庫中選擇數據
https://codeloop.org/pyqt5-tutorial-retrieve-data-from-mysql-in-qtablewidget/



Python教程–在Python中使用MySQL數據庫
https://codeloop.org/python-tutorial-working-with-mysql-database-in-python/

如何在PyQt5中創建MySQL數據庫
如何在PyQt5中將數據插入Mysql數據庫

如何在PyQt5中創建MySQL數據庫
https://codeloop.org/pyqt5-tutorial-how-to-create-mysql-database-in-pyqt5/
如何在PyQt5中將數據插入Mysql數據庫
https://codeloop.org/pyqt5-tutorial-how-to-insert-data-in-mysql-database/




PyQt5教程–在QTableWidget中從MySQL檢索數據
https://codeloop.org/pyqt5-tutorial-retrieve-data-from-mysql-in-qtablewidget/


如何在PyQt5中創建MySQL數據庫
如何在PyQt5中將數據插入Mysql數據庫


PyQt5教程–如何在MySQL數據庫中插入數據
https://codeloop.org/pyqt5-tutorial-how-to-insert-data-in-mysql-database/


PyQt5教程–如何在PyQt5中創建MySQL數據庫
https://codeloop.org/pyqt5-tutorial-how-to-create-mysql-database-in-pyqt5/



PyQt5將數據插入到Mysql數據庫中
https://codeloop.org/pyqt5-inserting-mysql-database/



如何將PyQt5應用程序與Mysql數據庫連接
https://codeloop.org/connect-pyqt5-with-mysql-database/


PyQt5教程–使用Qt Designer創建日曆
https://codeloop.org/pyqt5-tutorial-creating-calendar-with-qt-designer/


在PyQt5中使用Qt Designer
使用Qt Designer在PyQt5中創建CheckBox
Qt Designer中的PyQt5單選按鈕 



在PyQt5中使用Qt Designer
https://codeloop.org/pyqt5-tutorial-working-with-qt-designer/
使用Qt Designer在PyQt5中創建CheckBox
https://codeloop.org/pyqt5-tutorial-create-checkbox-in-qt-designer/
Qt Designer中的PyQt5單選按鈕 
https://codeloop.org/pyqt5-tutorial-working-with-radiobutton/



PyQt5教程–使用RadioButton
https://codeloop.org/pyqt5-tutorial-working-with-radiobutton/

PyQt5教程–在Qt Designer中創建複選框
https://codeloop.org/pyqt5-tutorial-create-checkbox-in-qt-designer/


PyQt5教程–使用Qt Designer
https://codeloop.org/pyqt5-tutorial-working-with-qt-designer/



















A.py

from B import b2
def a1():
    print('a1')
    b2()
B.py

def b1():
   from A import a1
   print('b1')
   a1()

def b2():
   print('b2')
if __name__ == '__main__':
   b1() 
   
   
   
主檔名   
mydatabase.py

主檔內容
from SqlData import Ent ###
    def database_C(self):
        print('C')
        Ent.db_Create()
    def database_R(self):
        print('R')
        Ent.db_Read()
    def database_U(self):
        print('U')
        Ent.db_Update()
    def database_D(self):
        print('D')
        Ent.db_Delete()

子檔名
SqlData.py

子檔內容
class Ent:   
    def db_Create():
    def db_Read():
    def db_Update():
    
```
