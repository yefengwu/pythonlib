from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon


class uiWindow(QMainWindow):
    def __init__(self) -> None:
        super(uiWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(300,300,500,400)
        windowicon = QIcon()
        windowicon.addFile('icon.ico')
        self.setWindowIcon(windowicon)
        self.setWindowTitle('Managerment')

        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.funcWidget = QListWidget()
        self.infoWidget = QListWidget()
        
        self.mainLayout.addWidget(self.funcWidget, 1)
        self.mainLayout.addWidget(self.infoWidget, 2)

        self.setCentralWidget(self.mainWidget)