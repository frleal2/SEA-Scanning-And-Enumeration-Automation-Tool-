from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DB.db import databaseHandler
from PyQt5 import QtWidgets
import pymongo
import nmap
import pandas as pd
import sys

# GUI FILE
from SEA_main_page import Ui_MainWindow
from Confirmation_Dialog import Ui_Dialog

db = databaseHandler()
db.build()

file_path = ""
string_of_args = "" # THIS WILL BE USED TO GET THE FULL STRING OF ARGS

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

            # DETAILED VIEW BUTTON TAKES YOU TO THE DETAILED VIEW PAGE
        self.ui.detailed_view_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.detailed_view))

        # ADD TOOL PAGE
        self.ui.btn_add_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool_specification))

            # PRESSED CANCEL BUTTON ON ADD TOOL PAGE GOES BACK TO TOOL PAGE
        self.ui.cancel_tool.clicked.connect(self.clearInputBoxes)
        self.ui.cancel_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

            #SAVE TOOL INPUT INTO TOOL TABLE AT DATABASE
        self.ui.save_tool_button.clicked.connect(self.saveToolInput)
        self.ui.save_tool_button.clicked.connect(self.populateTable)

        # This is what I am working on - SEAN
        self.ui.browse_path_button_2.clicked.connect(self.stringOfArgs)


        #POPULATE TABLE
        self.populateTable()

        #BROWSE BUTTONS
        self.ui.browse_path_button_3.clicked.connect(self.open)
        self.ui.browse_path_button.clicked.connect(self.open1)
        self.ui.browse_path_button_4.clicked.connect(self.open2)
        self.ui.browse_path_button_6.clicked.connect(self.open3)

        # BROWSE BUTTONS OF CONFIGURATION FILE
        self.ui.add_configuration_file_run.clicked.connect(self.open2)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    
    def confirmation_dialog(self, row):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()

        rsp == QtWidgets.QDialog.accepted

        if rsp == 1:
            self.onClickedRemove(row)

    ### METHOD FOR ADDING THE STRING OF ARGS TO DISPLAY WITHIN THE  ###
    def stringOfArgs(self):
        args = self.ui.option_arg_input_2.text()
        string_of_args = self.ui.option_arg_input.text()
        final = string_of_args + " " + args
        self.ui.option_arg_input.setText(final)

    ### METHOD TO CHECK TOOL INPUT AND SAVE TOOL INPUT INTO DATABASE ###
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

        if toolName == "":
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("Missing Tool Name")

        elif toolDesc == "":
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("Missing Tool Description")

        elif toolPath == "":
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("Missing Tool Path")

        elif toolOutputDataSpec == "":
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("Missing Tool Output Data Specification")

        elif optionArg == "":
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("Missing Tool Options and Arguments")

        else:
            self.ui.Announcer.setStyleSheet("color: red")
            self.ui.Announcer.setText("")
            db.insertIntoTool(toolName, toolDesc, toolPath, toolOutputDataSpec, optionArg)
            self.clearInputBoxes()
            self.ui.stackedWidget.setCurrentWidget(self.ui.tool)

    ### METHOD TO CLEAR ALL INPUT BOXES AFTER SAVE BUTTON IS CLICKED
    def clearInputBoxes(self):
        self.ui.tool_name_input.setText("")
        self.ui.tool_description_input.setText("")
        self.ui.tool_path_input.setText("")
        self.ui.output_data_input.setText("")
        self.ui.option_arg_input.setText("")

    ### METHOD TO POPULATE TOOL LIST TABLE FROM DATABASE ###
    def populateTable(self):
        tooldata = db.importData()
        name_column = list(tooldata['name'])
        description_column = list(tooldata['description'])
        items = len(name_column)

        for x in range(items):
            remove_btn = QPushButton("Remove")         #CREATES A REMOVE BUTTON
            remove_btn.clicked.connect(lambda *args, row=x: self.confirmation_dialog(row)) #GIVES THE ROW OF THE BUTTON
            remove_btn.setStyleSheet("QPushButton {\n" #STYLES THE BUTTON
                                        "    color: black;\n"
                                        "    background-color: rgb(235,235,235);\n"
                                        "    border: 0px solid;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")    

            update_btn = QPushButton("Update/Edit")         #CREATES AN UPDATE BUTTON
            update_btn.clicked.connect(lambda *args, row=x: self.onClickedUpdate(row))
            update_btn.setStyleSheet("QPushButton {\n" #STYLES THE BUTTON
                                        "    color: black;\n"
                                        "    background-color: rgb(235,235,235);\n"
                                        "    border: 0px solid;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")   
            self.ui.tool_list_table.setItem(x, 0, QTableWidgetItem(name_column[x]))
            self.ui.tool_list_table.setItem(x, 1, QTableWidgetItem(description_column[x]))
            self.ui.tool_list_table.setCellWidget(x, 2, remove_btn) #ADDS A REMOVE BUTTON IN EVERY ROW OF THE COLUMN
            self.ui.tool_list_table.setCellWidget(x, 3, update_btn) #ADDS AN UPDATE BUTTON IN EVERY ROW OF THE COLUMN
    
    ### METHOD FOR UPDATE BUTTON IN TOOL LIST TABLE
    def onClickedUpdate(self,row):
        name = self.ui.tool_list_table.item(row,0).text()

        self.ui.stackedWidget.setCurrentWidget(self.ui.tool_update)

        tooldata = db.importData()
        #print(tooldata)
        name_column = list(tooldata['name'])
        description_column = list(tooldata['description'])
        path_column = list(tooldata['path'])
        outputDataSpec_column = list(tooldata['outputDataSpec'])
        optionAndArgument_column = list(tooldata['ouptionAndArgument'])

        self.ui.tool_name_input_2.setText(name_column[row])
        self.ui.tool_name_input_2.textChanged.connect(self.onChanged1)

        self.ui.tool_description_input_2.setText(description_column[row])
        self.ui.tool_description_input_2.textChanged.connect(self.onChanged2)

        #self.ui.tool_path_input_2.setText(path_column[row])
        #self.ui.tool_path_input_2.textChanged.connect(self.onChanged3)

        self.ui.output_data_input_2.setText(outputDataSpec_column[row])
        self.ui.output_data_input_2.textChanged.connect(self.onChanged4)

        self.ui.option_arg_input_3.setText(optionAndArgument_column[row])
        self.ui.option_arg_input_3.textChanged.connect(self.onChanged5)

        #THIS BUTTON UPDATES THE ALREADY SAVED TOOL
        self.ui.save_tool_button_2.clicked.connect(lambda *args, name=name: self.updateTool(name))

        #THIS BUTTON CANCELS THE UPDATING FORM 
        self.ui.cancel_tool_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))
    
    def onChanged1(self,text):
        self.ui.tool_name_input_2.setText(text)
        print(text)

    def onChanged2(self,text):
        self.ui.tool_description_input_2.setText(text)

    def onChanged3(self,text):
        self.ui.tool_path_input_2.setText(text)
    
    def onChanged4(self,text):
        self.ui.output_data_input_2.setText(text)

    def onChanged5(self,text):
        self.ui.option_arg_input_3.setText(text)
    
    ###METHOD TO GET UPDATED STRINGS FROM UPDATE OF TOOL
    def updateTool(self,name):
        toolName = self.ui.tool_name_input_2.text()
        toolDesc = self.ui.tool_description_input_2.text()
        toolPath = self.ui.tool_path_input_2.text()
        toolOutputDataSpec = self.ui.output_data_input_2.text()
        optionArg = self.ui.option_arg_input_3.text()

        print(toolName, toolDesc, toolPath, toolOutputDataSpec, optionArg)
        db.updateAtTool(name,toolName,toolDesc,toolPath,toolOutputDataSpec,optionArg)
        self.populateTable()
        self.ui.stackedWidget.setCurrentWidget(self.ui.tool)
        
    ### METHOD FOR REMOVE BUTTON IN TOOL LIST TABLE
    def onClickedRemove(self,row):
        name = self.ui.tool_list_table.item(row,0).text() #GETTING THE NAME OF THE TOOL
        print(name)
        db.deleteFromTool(name)                           #DELETING DOCUMENT FROM CLUSTER
        self.ui.tool_list_table.removeRow(row)            #DELETING ROW FROM TABLE
    
    ### METHODS FOR THE BROWSE BUTTONS ###
    def open(self):
        path = QFileDialog.getOpenFileName()
        print("File path:" + path[0])
        self.ui.lineEdit_5.setText(path[0])
        file = path[0]

        with open(file, "r") as f:
            print(f.readline())

    ### BROWSE BUTTON FOR THE TOOL PATH ###
    def open1(self):
        path = QFileDialog.getOpenFileName()
        print("File path:"+path[0])
        self.ui.tool_path_input.setText(path[0])
        # file = path[0]
        #
        # with open(file, "r") as f:
        #     print(f.readline())

    def open2(self):
        path = QFileDialog.getOpenFileName()
        print("File path:" + path[0])
        self.ui.tool_path_input_2.setText("HIIIII")
        file = path[0]

        with open(file, "r") as f:
            print(f.readline())
    
    def open3(self):
        path = QFileDialog.getOpenFileName()
        print("File path:" + path[0])
        self.ui.lineEdit_6.setText(path[0])
        file = path[0]

        with open(file, "r") as f:
            print(f.readline())

    ### METHOD FOR ADDINGING THE PATH OF CONFIGURATION FILE ###
    def open2(self):
        path = QFileDialog.getOpenFileName()
        print("File path:" + path[0])
        self.ui.configuration_file_selected_run_path.setText(path[0])
        file = path[0]

        with open(file, "r") as f:
            print(f.readline())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())