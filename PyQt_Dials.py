# importing libraries
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from openpyxl import load_workbook

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)   

class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("RP Adjust")
		self.setWindowIcon(QtGui.QIcon('C:/users/shoukulk/Desktop/work/pics/MagnaLogo.png'))
		# setting geometry
		self.setGeometry(300, 300, 550, 250)
		self.UiComponents()
		self.show()
  
	def UiComponents(self):

		dial = QDial(self)
		dial.setGeometry(50, 50, 150, 150)
		dial.setRange(0, 20)
		dial.setNotchesVisible(True)
		
		label = QLabel("Set Roll", self)
		label.setGeometry(100, 175, 75, 75)
		label.setWordWrap(True)
		dial.valueChanged.connect(lambda: label.setText("Roll is: \n" +str(dial.value())+" Deg"))
		#print(str(dial.value()))
  
		dial2 = QDial(self)
		dial2.setGeometry(350, 50, 150, 150)
		dial2.setRange(0, 20)
		dial2.setNotchesVisible(True)
        
		label2 = QLabel("Set Pitch", self)
		label2.setGeometry(400, 175, 75, 75)
		label2.setWordWrap(True)
		dial2.valueChanged.connect(lambda: label2.setText("Pitch is: \n" +str(dial2.value())+" Deg"))

       	
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
