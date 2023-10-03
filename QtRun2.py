import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QApplication, QMainWindow, QWidget

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(30, 40, 200, 30)
        #slider.valueChanged[int].connect(self.changeValue)
        
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("Checkbox Example")
        self.setWindowIcon(QtGui.QIcon('C:/users/shoukulk/Desktop/work/pics/MagnaLogo.png'))
        self.show()
        
        def changeValue(self, value):
            value = value+2
            print(value)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        




