import sys
from PySide6 import QtCore, QtWidgets, QtGui
from bindUi import bindWidget
class B30Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Best30查询")   
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))  #设置icon

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Exo-Light.ttf")
        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Kazesawa-Light.ttf")
        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/NotoSansCJKsc-Regular.otf")

        self.title = QtWidgets.QLabel("\tBest30查询",alignment=QtCore.Qt.AlignTop)
        self.title.setFont(QtGui.QFont("Exo",18))

        self.nickNameText = QtWidgets.QLabel(" 游客 ",alignment=QtCore.Qt.AlignTop)
        self.nickNameText.setFont(QtGui.QFont("Kazesawa Light",18))
        
        self.getB30Button = QtWidgets.QPushButton(text="查询Best30/Recent10")
        self.getB30Button.setFont(QtGui.QFont("Exo",16))

        self.nowLabel = QtWidgets.QLabel("\t\t当前状态：")
        self.nowLabel.setFont(QtGui.QFont("Noto Sans CJK SC Regular",16))

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
        self.mainBox.addWidget(self.getB30Button,0,0,1,1)
        self.mainBox.addWidget(self.nowLabel,0,1,1,3)
        self.mainBox.setContentsMargins(0,0,0,0)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.topBar,0,0,1,1)
        self.layout.addWidget(self.mainBoxWeidgt,1,0,18,1)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = B30Widget()
    widget.resize(1280,810)
    widget.show()
    #widget.showMaximized()
    sys.exit(app.exec())