#################################
#주식 기본 정보 출력
#################################
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

from PyQt5.QtCore import *
#################################


class MyWindow(QMainWindow):
    login_stat = 141
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pystock")
        self.setGeometry(300, 300, 300, 500)
        
        
      
        btn1 = QPushButton("로그인", self)
        btn1.move(190, 60)
        btn1.clicked.connect(self.login)
        
        #조회 결과 출력 공간
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 100, 280, 80)
        self.text_edit.setEnabled(False)
        
        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_login_clicked)
            
        label = QLabel("종목코드: ", self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
            
        #종목코드 조회 입력 창에 디폴트 입력값
        self.code_edit.setText("039490")   
        QMessageBox.about(self, "message", f"__init__{self.login_stat}")
        
        
        
    #카움증권 로그인    
    def login(self):
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("commConnect()")
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        
    
    def event_connect(self, err_code):
        if err_code == 0:
            self.login_stat = err_code
            print(self.login_stat)
            QMessageBox.about(self, "message", f"로그인 성공{self.login_stat}")
            self.text_edit.append(f"로그인 성공{self.login_stat}")
            account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
            self.text_edit.append("계좌번호: " + account_num.rstrip(';'))
        QMessageBox.about(self, "message", f"at event_connect {self.login_stat}")
        
    #조회 버튼 클릭 시
    def btn1_login_clicked(self):
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)
        
        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString", "종목코드", code)
        
        # CommRqData
        # sRQName-사용자구분 명
        # sTrCode-Tran명 입력
        # nPrevNext-0조회, 2연속
        # sScreenNo-4자리 회원번호
        #ex) CommRqData("RQ_1", "OPT00001", 0, "0101"
        self.kiwoom.dynamicCall("CommRqData(QString, Qstring, int, QString)", "opt10001_req", "opt10001", 0, "0101")
        
    #  ScrNo-화면번호
    # RQName-사용자자구분 명
    # TrCode-Tran 명
    # RecordName-Record 명
    # PreNext-연속조회 유무
    
    # 나머지는 1.0.0.1 버전 이후 사용하지 않음(data_len, err_code, msg1, msg2)    
    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            
            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량" + volume.strip())






####################################
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()   
