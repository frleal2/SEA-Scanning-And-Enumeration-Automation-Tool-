# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SEA_main_pageFIXED.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ToolListArea import *
from RunArea import *
from DB.db import databaseHandler

db = databaseHandler()
db.build()
#db.insertIntoTool("name", "description", "path", "Path", "Path", "Path")


class Ui_MainWindow(object):

    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowRun(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindowRun()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.main_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_text_bar = QtWidgets.QFrame(self.main_header)
        self.title_text_bar.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.title_text_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_text_bar.setObjectName("title_text_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.title_text_bar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle = QtWidgets.QFrame(self.title_text_bar)
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(100, 50))
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_menu_pushButton = QtWidgets.QPushButton(self.left_menu_toggle)
        self.main_menu_pushButton.setMaximumSize(QtCore.QSize(100, 50))
        self.main_menu_pushButton.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.main_menu_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_menu_pushButton.setIcon(icon)
        self.main_menu_pushButton.setIconSize(QtCore.QSize(24, 24))
        self.main_menu_pushButton.setObjectName("main_menu_pushButton")
        self.horizontalLayout_3.addWidget(self.main_menu_pushButton)
        self.horizontalLayout_4.addWidget(self.left_menu_toggle)
        self.TITLE = QtWidgets.QFrame(self.title_text_bar)
        self.TITLE.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TITLE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TITLE.setObjectName("TITLE")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.TITLE)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.TITLE)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_4.addWidget(self.TITLE)
        self.righ_support_frame = QtWidgets.QFrame(self.title_text_bar)
        self.righ_support_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.righ_support_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.righ_support_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.righ_support_frame.setObjectName("righ_support_frame")
        self.horizontalLayout_4.addWidget(self.righ_support_frame)
        self.horizontalLayout_2.addWidget(self.title_text_bar)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftSide_menu = QtWidgets.QFrame(self.main_body)
        self.leftSide_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leftSide_menu.setStyleSheet("QFrame{\n"
"    background-color: rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(128, 128, 128);\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton: hover{\n"
"    background-color: rgb(204, 204, 204);\n"
"}")
        self.leftSide_menu.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftSide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftSide_menu.setObjectName("leftSide_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftSide_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.leftSide_menu)
        self.left_menu_top_buttons.setMaximumSize(QtCore.QSize(100, 16777215))
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.tool_page_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.tool_page_button.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tool_page_button.setStyleSheet("")
        self.tool_page_button.setAutoDefault(False)
        self.tool_page_button.setObjectName("tool_page_button")

        self.tool_page_button.clicked.connect(self.openWindow)


        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tool_page_button)
        self.scan_page_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.scan_page_button.setMaximumSize(QtCore.QSize(16777215, 150))
        self.scan_page_button.setStyleSheet("")
        self.scan_page_button.setObjectName("scan_page_button")

        self.scan_page_button.clicked.connect(self.openWindowRun)


        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.scan_page_button)
        self.scan_page_button.raise_()
        self.tool_page_button.raise_()
        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)
        self.horizontalLayout.addWidget(self.leftSide_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_footer.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.main_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">SEA TOOL</span></p></body></html>"))
        self.tool_page_button.setText(_translate("MainWindow", "TOOL"))
        self.scan_page_button.setText(_translate("MainWindow", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
