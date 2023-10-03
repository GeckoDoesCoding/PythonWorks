import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtGui
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Test Run 1"
        self.setGeometry(300, 300, 550, 550)
        self.icon = 'C:/users/shoukulk/Desktop/work/pics/MagnaLogo.png'
        self.createUI()
        self.show()
        
    def createUI(self):
        self.setGeometry(300, 300, 550, 550)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setStyleSheet("""""")
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.drawItems()
        
    def drawItems(self):
        self.imageLogo = QPixmap('C:/users/shoukulk/Desktop/work/pics/MagnaLogo.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.imageLogo)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)


App = QApplication(sys.argv)
window = Windows()
sys.exit(App.exec())