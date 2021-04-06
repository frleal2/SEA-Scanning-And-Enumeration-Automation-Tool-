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

file_path = ""

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

        # DETAILED VIEW BUTTON TAKES YOU TO THE DETAILED VIEW PAGE
        self.ui.detailed_view_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.detailed_view))

        #SAVE TOOL INPUT INTO TOOL TABLE AT DATABASE
        self.ui.save_tool_button.clicked.connect(self.saveToolInput)
        self.ui.save_tool_button.clicked.connect(self.populateTable)
        self.ui.save_tool_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

        #POPULATE TABLE 
        self.populateTable()

        #BROWSE BUTTONS
        self.ui.browse_path_button_3.clicked.connect(self.open)
        

        self.ui.browse_path_button.clicked.connect(self.open1)
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ### METHOD TO SAVE TOOL INPUT INTO DATABASE ###
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

        
    ### METHOD TO POPULATE TABLE FROM DATABASE ###
    def populateTable(self):
        tooldata = db.importData()
        name_column = list(tooldata['name'])
        description_column = list(tooldata['description'])
        items = len(name_column)

        for x in range(items):
            self.ui.tool_list_table.setItem(x, 0, QTableWidgetItem(name_column[x]))
            self.ui.tool_list_table.setItem(x, 1, QTableWidgetItem(description_column[x]))
    
    ### METHODS FOR THE BROWSE BUTTONS ###
    def open(self):
        path=QFileDialog.getOpenFileName(self,r'Open a file',r'/home/hiram/Documents/Tool_Specification/',r'All files(*.*)')
        if path != ('',''):
            print("File path:"+path[0])
            self.ui.lineEdit_5.setText(path[0])
        

    def open1(self):
        path=QFileDialog.getOpenFileName(self,r'Open a file',r'/usr/bin/nmap',r'All files(*.*)')
        if path != ('',''):
            print("File path:"+path[0])   
            self.ui.tool_path_input.setText(path[0]) 
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())