import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArcaeaKit")   #标题ArcaeaKit
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))  #设置icon

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Exo-Light.ttf")
        self.title = QtWidgets.QLabel("\tArcaeaKit",alignment=QtCore.Qt.AlignTop)
        self.title.setFont(QtGui.QFont("Exo",18))

        self.fontB = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Kazesawa-Light.ttf")
        self.nickNameText = QtWidgets.QLabel(" 游客 ",alignment=QtCore.Qt.AlignTop)
        self.nickNameText.setFont(QtGui.QFont("Kazesawa Light",18))

        self.fragText = QtWidgets.QLabel("残片",alignment=QtCore.Qt.AlignTop)
        self.fragText.setFont(QtGui.QFont("Kazesawa Light",18))
        
        self.nbutton = QtWidgets.QPushButton(text="Click me!")

        self.topBar = QtWidgets.QWidget()
        self.topBar.setObjectName("topBar")
        self.topBar.setStyleSheet("#topBar{border-image: url(./assets/top_bar_bg.png);}")
        
        self.topBox = QtWidgets.QGridLayout(self.topBar)
        self.topBox.addWidget(self.title,0,0,1,2)
        self.topBox.addWidget(self.nickNameText,0,2,1,1)
        self.topBox.addWidget(self.fragText,0,4,1,1)
        self.topBox.setContentsMargins(0,0,0,0)

        self.mainBox = QtWidgets.QGridLayout()
        self.mainBox.addWidget(self.nbutton,0,0)
        self.mainBox.setContentsMargins(0,0,0,0)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.topBar,0,0,1,1)
        self.layout.addLayout(self.mainBox,1,0,18,1)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1280,810)
    widget.show()
    #widget.showMaximized()
    sys.exit(app.exec())