from ctypes import alignment
import sys
from PySide6 import QtCore, QtWidgets, QtGui
class bindWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArcaeaKit Login")   #标题ArcaeaKit
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))  #设置icon
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Exo-Light.ttf")
        self.title = QtWidgets.QLabel("  ArcaeaKit Login",alignment=QtCore.Qt.AlignTop)
        self.title.setFont(QtGui.QFont("Exo",18))

        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/Kazesawa-Light.ttf")
        self.fontA = QtGui.QFontDatabase.addApplicationFont("./assets/fonts/NotoSansCJKsc-Regular.otf")
        self.idEdit = QtWidgets.QLabel(" 用户ID(9位) ",alignment=QtCore.Qt.AlignCenter)
        self.idEdit.setFont(QtGui.QFont("Noto Sans CJK SC Regular",18))

        self.userIdEdit = QtWidgets.QLineEdit()
        self.userIdEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:2px solid;border-color: rgba(0,0,0,0);border-bottom-color: rgb(149, 139, 255);")
        self.userIdEdit.setFont(QtGui.QFont("Exo",18))
        self.userIdEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.userIdEdit.setPlaceholderText("用户ID(9位)")

        self.loginButton = QtWidgets.QPushButton(text="   绑定Arcaea账号   ")
        self.loginButton.setFont(QtGui.QFont("Noto Sans CJK SC Regular",15))
        self.loginButton.setStyleSheet("border-image: url(./assets/login_btn.png);color: rgb(255,255,255)")
        self.loginButton.setMinimumHeight(40)

        self.closeButton = QtWidgets.QPushButton(text="  取消绑定  ")
        self.closeButton.setFont(QtGui.QFont("Noto Sans CJK SC Regular",15))
        self.closeButton.setStyleSheet("border-image: url(./assets/login_btn.png);color: rgb(255,255,255)")
        self.closeButton.setMinimumHeight(40)
        self.closeButton.clicked.connect(self.close)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0,10,0,0)
        self.layout.addWidget(self.title,0,0)
        self.layout.addWidget(self.idEdit,1,0,1,5)
        self.layout.addWidget(self.userIdEdit,2,0,12,5)
        self.layout.addWidget(self.loginButton,14,1)
        self.layout.addWidget(self.closeButton,14,3)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = bindWidget()
    widget.resize(720,480)
    widget.show()
    #widget.showMaximized()
    sys.exit(app.exec())