# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DetailedViewOfSelectedTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 399)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 651, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 50, 251, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(320, 80, 21, 21))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 80, 251, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(10, 140, 251, 21))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 140, 61, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 110, 251, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 110, 61, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 220, 361, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 100, 56, 17))
        self.pushButton_8.setObjectName("pushButton_8")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(10, 120, 251, 21))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(210, 40, 51, 21))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 40, 61, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 40, 71, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 350, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 350, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Tool Specification"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Tool Name"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "Tool Description"))
        self.pushButton_3.setText(_translate("Dialog", "Tool Path"))
        self.plainTextEdit_5.setPlainText(_translate("Dialog", "OR"))
        self.pushButton_5.setText(_translate("Dialog", "Tool Specification File"))
        self.plainTextEdit_4.setPlainText(_translate("Dialog", "Output Data Specification"))
        self.pushButton_6.setText(_translate("Dialog", "Add"))
        self.plainTextEdit_3.setPlainText(_translate("Dialog", "Option and Argument"))
        self.pushButton_4.setText(_translate("Dialog", "Add"))
        self.groupBox_4.setTitle(_translate("Dialog", "Tool Dependency"))
        self.pushButton_8.setText(_translate("Dialog", "Add"))
        self.plainTextEdit_8.setPlainText(_translate("Dialog", "Dependency Expression"))
        self.plainTextEdit_6.setPlainText(_translate("Dialog", "    Value"))
        self.pushButton_7.setText(_translate("Dialog", "Remove"))
        self.label.setText(_translate("Dialog", "Dependent Data"))
        self.label_2.setText(_translate("Dialog", "Operator"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
