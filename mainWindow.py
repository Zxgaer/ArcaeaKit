from ctypes import alignment
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from bindUi import bindWidget
class MainWidget(QtWidgets.QWidget):
    def openBindWeidgt(self):
        WbindWidget = bindWidget()
        WbindWidget.exec()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArcaeaKit")   #标题ArcaeaKit
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))  #设置icon

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Exo-Light.ttf")
        self.title = QtWidgets.QLabel("\tArcaeaKit",alignment=QtCore.Qt.AlignTop)
        self.title.setFont(QtGui.QFont("Exo",18))

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Kazesawa-Light.ttf")
        self.nickNameText = QtWidgets.QLabel(" 游客 ",alignment=QtCore.Qt.AlignTop)
        self.nickNameText.setFont(QtGui.QFont("Kazesawa Light",18))
        
        self.getUserInfoButton = QtWidgets.QPushButton(text="用户信息")

        self.getSongsInfoButton = QtWidgets.QPushButton(text="曲目信息")

        self.pttCalculatorButton = QtWidgets.QPushButton(text="PTT计算")

        self.settingsButton = QtWidgets.QPushButton(text="设置")
        
        self.best30Button = QtWidgets.QPushButton(text="Best30查询")

        self.bindButton = QtWidgets.QPushButton(text="绑定Arcaea账号")
        self.bindButton.clicked.connect(self.openBindWeidgt)

        self.topBar = QtWidgets.QWidget()
        self.topBar.setObjectName("topBar")
        self.topBar.setStyleSheet("#topBar{border-image: url(./assets/top_bar_bg.png);}")
        
        self.topBox = QtWidgets.QGridLayout(self.topBar)
        self.topBox.addWidget(self.title,0,0,1,1)
        self.topBox.addWidget(self.nickNameText,0,2,1,1)
        self.topBox.setContentsMargins(0,0,0,0)

        self.mainBoxWeidgt = QtWidgets.QWidget()
        self.mainBoxWeidgt.setObjectName("mainBoxWeidgt")
        self.mainBoxWeidgt.setStyleSheet("#mainBoxWeidgt{border-image: url(./assets/bg.jpg);}")
        self.mainBoxWeidgt.setContentsMargins(0,0,0,0)

        self.mainBox = QtWidgets.QGridLayout(self.mainBoxWeidgt)
        self.mainBox.addWidget(self.getUserInfoButton,0,0)
        self.mainBox.addWidget(self.pttCalculatorButton,1,0)
        self.mainBox.addWidget(self.getSongsInfoButton,0,3)
        self.mainBox.addWidget(self.settingsButton,1,3)
        self.mainBox.addWidget(self.best30Button,0,1,2,2)
        self.mainBox.addWidget(self.bindButton,2,0,1,4)
        self.mainBox.setContentsMargins(0,0,0,0)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.topBar,0,0,1,1)
        self.layout.addWidget(self.mainBoxWeidgt,1,0,18,1)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWidget()
    widget.resize(1280,810)
    widget.show()
    #widget.showMaximized()
    sys.exit(app.exec())