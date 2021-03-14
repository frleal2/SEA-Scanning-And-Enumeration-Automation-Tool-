from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DB.db import databaseHandler
import sys 

# GUI FILE
from sea_main_page import Ui_MainWindow

#db = databaseHandler()
#db.build()

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

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())