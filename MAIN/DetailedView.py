# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailedView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DB.db import databaseHandler

db = databaseHandler()
db.build()

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 801, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ToolSpecification = QtWidgets.QGroupBox(self.frame)
        self.ToolSpecification.setAlignment(QtCore.Qt.AlignCenter)
        self.ToolSpecification.setObjectName("ToolSpecification")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ToolSpecification)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QFrame(self.ToolSpecification)
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        
        self.tool_name = QtWidgets.QPlainTextEdit(self.left)
        self.tool_name.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.tool_name.setObjectName("tool_name")

        
        self.tool_description = QtWidgets.QPlainTextEdit(self.left)
        self.tool_description.setGeometry(QtCore.QRect(10, 50, 211, 31))
        self.tool_description.setObjectName("tool_description")
       

        self.tool_path = QtWidgets.QPlainTextEdit(self.left)
        self.tool_path.setGeometry(QtCore.QRect(10, 90, 211, 31))
        self.tool_path.setObjectName("tool_path")
        

        self.option_argument = QtWidgets.QPlainTextEdit(self.left)
        self.option_argument.setGeometry(QtCore.QRect(10, 130, 211, 31))
        self.option_argument.setObjectName("option_argument")
       

        self.Output_data_spec = QtWidgets.QPlainTextEdit(self.left)
        self.Output_data_spec.setGeometry(QtCore.QRect(10, 170, 211, 31))
        self.Output_data_spec.setObjectName("Output_data_spec")
       

        self.browse_path_button = QtWidgets.QPushButton(self.left)
        self.browse_path_button.setGeometry(QtCore.QRect(220, 90, 111, 31))
        self.browse_path_button.setObjectName("browse_path_button")


        self.add_option_argument = QtWidgets.QPushButton(self.left)
        self.add_option_argument.setGeometry(QtCore.QRect(220, 130, 111, 31))
        self.add_option_argument.setObjectName("add_option_argument")


        self.horizontalLayout.addWidget(self.left)
        self.label_3 = QtWidgets.QLabel(self.ToolSpecification)
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.right = QtWidgets.QFrame(self.ToolSpecification)
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.tool_path_2 = QtWidgets.QPlainTextEdit(self.right)
        self.tool_path_2.setGeometry(QtCore.QRect(60, 80, 261, 31))
        self.tool_path_2.setObjectName("tool_path_2")
        self.browse_path_button_2 = QtWidgets.QPushButton(self.right)
        self.browse_path_button_2.setGeometry(QtCore.QRect(130, 120, 111, 31))
        self.browse_path_button_2.setObjectName("browse_path_button_2")
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout.addWidget(self.ToolSpecification)
        self.ToolDependency = QtWidgets.QGroupBox(self.frame)
        self.ToolDependency.setAlignment(QtCore.Qt.AlignCenter)
        self.ToolDependency.setObjectName("ToolDependency")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ToolDependency)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.ToolDependency)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 35, 141, 31))
        self.comboBox_2.setStyleSheet("font: 13pt \".AppleSystemUIFont\";\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.frame_4)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(430, 40, 171, 21))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(230, 35, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(655, 35, 91, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 70, 71, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.frame_5)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(20, 30, 751, 31))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.ToolDependency)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 10, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ToolSpecification.setTitle(_translate("MainWindow", "Tool Specification"))
        self.tool_name.setPlainText(_translate("MainWindow", "Tool Name"))
        self.tool_description.setPlainText(_translate("MainWindow", "Tool Description"))
        self.tool_path.setPlainText(_translate("MainWindow", "Tool Path\n"
""))
        self.option_argument.setPlainText(_translate("MainWindow", "Option and Argument\n"
""))
        self.Output_data_spec.setPlainText(_translate("MainWindow", "Output Data Specification\n"
""))
        self.browse_path_button.setText(_translate("MainWindow", "Browse"))
        self.add_option_argument.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "OR"))
        self.tool_path_2.setPlainText(_translate("MainWindow", "Tool Specification File\n"
""))
        self.browse_path_button_2.setText(_translate("MainWindow", "Browse"))
        self.ToolDependency.setTitle(_translate("MainWindow", "Tool Dependency"))
        self.plainTextEdit_6.setPlainText(_translate("MainWindow", "Value"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove"))
        self.label.setText(_translate("MainWindow", "Dependent Data"))
        self.label_2.setText(_translate("MainWindow", "Operator"))
        self.pushButton_8.setText(_translate("MainWindow", "Add"))
        self.plainTextEdit_8.setPlainText(_translate("MainWindow", "Dependency Expression"))
        
        
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton.clicked.connect( self.saveinput )
        
        
        
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    
    
    
    def saveinput(self):
            toolName = self.tool_name.toPlainText()
            toolDescription = self.tool_description.toPlainText()
            toolPath = self.tool_path.toPlainText()
            optionArgument = self.option_argument.toPlainText()
            dataSpec = self.Output_data_spec.toPlainText()
            db.insertIntoTool(toolName, toolDescription, toolPath, optionArgument, optionArgument, dataSpec)
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

