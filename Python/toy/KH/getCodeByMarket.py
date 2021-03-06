import sys
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        self.setWindowTitle("종목 코드")
        self.setGeometry(300, 300, 300, 150)
        
        btn1 = QPushButton("종목코드 얻기", self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)
        
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 230, 130)
        
        
    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)",["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []
        
        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)",[x])
            kospi_code_name_list.append(x + " : " + name)
            
            
        self.listWidget.addItems(kospi_code_name_list)
        
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


####################################
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)
myWindow = MyWindow2()
myWindow.show()
app.exec_()   