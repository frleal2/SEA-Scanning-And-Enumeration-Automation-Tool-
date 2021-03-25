from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 420, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 390, 151, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 50, 761, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 120, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 120, 251, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(30, 220, 251, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 220, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(30, 170, 251, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 170, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(30, 20, 251, 31))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(370, 130, 61, 20))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(30, 70, 251, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 390, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 390, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 390, 111, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 370, 561, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(30, 120, 251, 31))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(350, 20, 91, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 20, 71, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 80, 71, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 470, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tool Specification"))
        self.pushButton_3.setText(_translate("MainWindow", "Tool Path"))
        self.pushButton_5.setText(_translate("MainWindow", "Tool Specification File"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Output Data Specification"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Option and Argument"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.plainTextEdit_7.setPlainText(_translate("MainWindow", "Tool Name"))
        self.label_3.setText(_translate("MainWindow", "OR"))
        self.plainTextEdit_5.setPlainText(_translate("MainWindow", "Tool Description"))
        self.label.setText(_translate("MainWindow", "Dependent Data"))
        self.label_2.setText(_translate("MainWindow", "Operator"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Tool Dependency"))
        self.plainTextEdit_8.setPlainText(_translate("MainWindow", "Dependency Expression"))
        self.plainTextEdit_6.setPlainText(_translate("MainWindow", "Value"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove"))
        self.pushButton_8.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())