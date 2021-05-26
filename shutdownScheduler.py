from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 775)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #2c3259;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font:bold;\n"
                                 "color:#26f2fc;\n"
                                 "font-size: 40px;")
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(150, 390, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(22)
        self.b1.setFont(font)
        self.b1.setStyleSheet("       background-color: #913d90;\n"
                              "    color:white;\n"
                              "    border-width: 2px;\n"
                              "")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(30, 580, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setStyleSheet("       background-color: #8010e3;\n"
                              "    color:white;\n"
                              "    border-width: 2px;\n"
                              "")
        self.b2.setObjectName("b2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 470, 71, 91))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font:bold;\n"
                                   "color:white;\n"
                                   "font-size: 40px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font:bold;\n"
                                   "color:white;\n"
                                   "font-size: 40px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 31, 21))
        self.label_4.setStyleSheet("color:white;\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 300, 41, 21))
        self.label_5.setStyleSheet("color:white;\n"
                                   "")
        self.label_5.setObjectName("label_5")

        self.txt1 = QtWidgets.QSpinBox(self.centralwidget)
        self.txt1.setGeometry(QtCore.QRect(60, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.txt1.setFont(font)
        self.txt1.setObjectName("txt1")

        self.txt2 = QtWidgets.QSpinBox(self.centralwidget)
        self.txt2.setGeometry(QtCore.QRect(330, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.txt2.setFont(font)
        self.txt2.setObjectName("txt2")

        self.label.raise_()
        self.b1.raise_()
        self.b2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.txt1.raise_()
        self.label_4.raise_()
        self.txt2.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Shutdown Scheduler"))
        self.b1.setText(_translate("MainWindow", "Activate"))
        self.b2.setText(_translate("MainWindow", "Cancel an already scheduled shutdown"))
        self.label_2.setText(_translate("MainWindow", "OR"))
        self.label_3.setText(_translate("MainWindow", "Schedule a Download:"))
        self.label_4.setText(_translate("MainWindow", "Hours"))
        self.label_5.setText(_translate("MainWindow", "Minutes"))

    def start_shutdown(self):
        self.hrs = self.txt1.value()
        self.minutes = self.txt2.value()
        total = self.hrs * 3600 + self.minutes * 60
        total_unix = self.hrs * 60 + self.minutes
        if os.name == 'nt':
            os.system(f'shutdown -s -t {total}')
        elif os.name == 'posix':
            os.system(f'shutdown -h +{total_unix}')

    def cancel_shutdown(self):
        if os.name == 'nt':
            os.system('shutdown -a')
        elif os.name == 'posix':
            os.system('shutdown - c')

    def on_click(self):
        self.b1.clicked.connect(self.start_shutdown)
        self.b2.clicked.connect(self.cancel_shutdown)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.on_click()
    MainWindow.show()
    sys.exit(app.exec_())