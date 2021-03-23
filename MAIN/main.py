from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DB.db import databaseHandler
import pymongo
import pandas as pd
import sys 

# GUI FILE
from SEA_main_page import Ui_MainWindow

db = databaseHandler()
db.build()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #DEFAULT PAGE 
        self.ui.stackedWidget.setCurrentWidget(self.ui.tool)

        # TOOL PAGE 
        self.ui.btn_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

        # RUN PAGE
        self.ui.btn_run_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.run))

        # ADD TOOL PAGE
        self.ui.btn_add_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool_specification))

        # PRESSED CANCEL BUTTON ON ADD TOOL PAGE GOES BACK TO TOOL PAGE
        self.ui.cancel_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

        #SAVE TOOL INPUT INTO TOOL TABLE AT DATABASE
        self.ui.save_tool_button.clicked.connect(self.saveToolInput)
        self.ui.save_tool_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

        #TESTING PANDAS
        #db.Tool.find()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def saveToolInput(self):
        doc = QtGui.QTextDocument()

        toolName = self.ui.tool_name_input
        toolDesc = self.ui.tool_description_input
        toolPath = self.ui.tool_path_input
        toolOutputDataSpec = self.ui.output_data_input
        optionArg = self.ui.option_arg_input

        doc.setHtml(toolName.text())
        toolName = doc.toPlainText()

        doc.setHtml(toolDesc.text())
        toolDesc = doc.toPlainText()

        doc.setHtml(toolPath.text())
        toolPath = doc.toPlainText()

        doc.setHtml(toolOutputDataSpec.text())
        toolOutputDataSpec = doc.toPlainText()

        doc.setHtml(optionArg.text())
        optionArg = doc.toPlainText()

        db.insertIntoTool(toolName, toolDesc, toolPath, toolOutputDataSpec, optionArg)

    
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())