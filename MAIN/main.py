from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 

# GUI FILE
from sea_main_page import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #DEFAULT PAGE 
        self.ui.stackedWidget.setCurrentWidget(self.ui.tool)

        # PAGE 1
        self.ui.btn_tool.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tool))

        # PAGE 2
        self.ui.btn_run_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.run))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())