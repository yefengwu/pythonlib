from PySide6 import QtWidgets, QtGui, QtCore
from ui import uiWindow
import sys

class MainPageWindow(uiWindow):
    def __init__(self):
        super(MainPageWindow, self).__init__()
        self.initUi()
        
    def initUi(self):
        self.setLayout(self.mainLayout)
        items = ['Items 1', 'Items 2']
        self.funcWidget.addItems(items)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainPageWindow()
    mainWindow.show()
    sys.exit(app.exec())