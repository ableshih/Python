# https://xiang1023.blogspot.com/2017/09/python-pyautogui.html
# https://codeloop.org/python-how-to-create-digital-clock-with-pyside2/

from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide2.QtCore import QTime, QTimer, SIGNAL
import sys
from PySide2.QtGui import QIcon
import pyautogui # get screen resolution
# pip install pyautogui
a=pyautogui.size() # get screen resolution

# print(a.width,a.height)

class DigitalClock(QLCDNumber):
    def __init__(self, parent = None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(1000)
        self.showTime()
        self.setWindowTitle("Digital Clock")
        # setting  the geometry of window 
        self.setGeometry(-1, -1, a.width, a.height) # get screen resolution position 0,0
        # self.resize(a.width, a.height) 
        # pyautogui.position(0,0)

        self.setIcon()


    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)



    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)



myapp = QApplication(sys.argv)
window = DigitalClock()
window.show()
myapp.exec_()
sys.exit()
