; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CDlg_t1857
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "xingapi_sample_esearch.h"
LastPage=0

ClassCount=15
Class1=CChildFrame
Class2=CChildView
Class3=CDlg_t1101
Class4=CDlg_t1857
Class5=CDlgBase
Class6=CDlgExcludeItem
Class7=CDlgLogin
Class8=CDlgTRBar
Class9=CMainFrame
Class10=CSizingControlBarG
Class11=CSizingControlBar
Class12=CSCBMiniDockFrameWnd
Class13=CTRBar
Class14=CXingAPI_Sample_eSearchApp
Class15=CAboutDlg

ResourceCount=7
Resource1=IDD_t1857
Resource2=IDD_TR_BAR
Resource3=IDR_XINGAPTYPE
Resource4=IDR_MAINFRAME
Resource5=IDD_ABOUTBOX
Resource6=IDD_LOGIN
Resource7=IDD_t1866

[CLS:CChildFrame]
Type=0
BaseClass=CMDIChildWnd
HeaderFile=ChildFrm.h
ImplementationFile=ChildFrm.cpp

[CLS:CChildView]
Type=0
BaseClass=CWnd
HeaderFile=ChildView.h
ImplementationFile=ChildView.cpp

[CLS:CDlg_t1101]
Type=0
BaseClass=CDialog
HeaderFile=Dlg_t1101.h
ImplementationFile=Dlg_t1101.cpp

[CLS:CDlg_t1857]
Type=0
BaseClass=CDialog
HeaderFile=Dlg_t1857.h
ImplementationFile=Dlg_t1857.cpp
Filter=D
VirtualFilter=dWC
LastObject=IDC_COMBO1

[CLS:CDlgBase]
Type=0
BaseClass=CDialog
HeaderFile=DlgBase.h
ImplementationFile=DlgBase.cpp

[CLS:CDlgExcludeItem]
Type=0
BaseClass=CDialog
HeaderFile=DlgExcludeItem.h
ImplementationFile=DlgExcludeItem.cpp

[CLS:CDlgLogin]
Type=0
BaseClass=CDialog
HeaderFile=DlgLogin.h
ImplementationFile=DlgLogin.cpp

[CLS:CDlgTRBar]
Type=0
BaseClass=CDialog
HeaderFile=DlgTRBar.h
ImplementationFile=DlgTRBar.cpp

[CLS:CMainFrame]
Type=0
BaseClass=CMDIFrameWnd
HeaderFile=MainFrm.h
ImplementationFile=MainFrm.cpp

[CLS:CSizingControlBarG]
Type=0
BaseClass=baseCSizingControlBarG
HeaderFile=scbarg.h
ImplementationFile=scbarg.cpp

[CLS:CSizingControlBar]
Type=0
BaseClass=baseCSizingControlBar
HeaderFile=sizecbar.h
ImplementationFile=sizecbar.cpp

[CLS:CSCBMiniDockFrameWnd]
Type=0
BaseClass=baseCSCBMiniDockFrameWnd
HeaderFile=sizecbar.h
ImplementationFile=sizecbar.cpp

[CLS:CTRBar]
Type=0
BaseClass=CSizingControlBarG
HeaderFile=TRBar.h
ImplementationFile=TRBar.cpp

[CLS:CXingAPI_Sample_eSearchApp]
Type=0
BaseClass=CWinApp
HeaderFile=XingAPI_Sample_eSearch.h
ImplementationFile=XingAPI_Sample_eSearch.cpp

[CLS:CAboutDlg]
Type=0
BaseClass=CDialog
HeaderFile=XingAPI_Sample_eSearch.cpp
ImplementationFile=XingAPI_Sample_eSearch.cpp

[DLG:IDD_t1857]
Type=1
Class=CDlg_t1857
ControlCount=14
Control1=IDC_STATIC,static,1342308864
Control2=IDC_INBLOCK_REALKEY,edit,1350631552
Control3=IDC_BUTTON_REQUEST4,button,1342242816
Control4=IDC_INBLOCK_INDEX1857,edit,1350631552
Control5=IDC_BUTTON_REQUEST,button,1342242816
Control6=IDC_STATIC,static,1342308352
Control7=IDC_OUTBLOCK1,SysListView32,1350631425
Control8=IDC_STATIC,static,1342308864
Control9=IDC_STATIC,static,1342308352
Control10=IDC_KEYLIST,SysListView32,1350631425
Control11=IDC_STATIC,static,1342308864
Control12=IDC_STATIC,static,1342308352
Control13=IDC_COMBO_FLAG,combobox,1344340226
Control14=IDC_COMBO_REAL,combobox,1344340226

[DLG:IDD_EXCLUDE_ITEM]
Type=1
Class=CDlgExcludeItem

[DLG:IDD_LOGIN]
Type=1
Class=CDlgLogin
ControlCount=29
Control1=IDC_STATIC,button,1342177287
Control2=IDC_STATIC,static,1342308864
Control3=IDC_EDIT_ID,edit,1350631552
Control4=IDC_CHECK_SAVE_ID,button,1342177283
Control5=IDC_STATIC,static,1342308864
Control6=IDC_EDIT_PWD,edit,1350631584
Control7=IDC_STATIC,static,1342308864
Control8=IDC_EDIT_CERT_PWD,edit,1350631584
Control9=IDC_BUTTON_LOGIN,button,1342242816
Control10=IDC_CHECK_SHOW_CERT_ERR_DLG,button,1342242819
Control11=IDC_STATIC,button,1342177287
Control12=IDC_RADIO_REAL,button,1342246921
Control13=IDC_RADIO_SIMUL,button,1342181385
Control14=IDC_STATIC,static,1342308864
Control15=IDC_COMBO_SERVER_ADDR_TYPE,combobox,1344339971
Control16=IDC_STATIC,static,1342308864
Control17=IDC_EDIT_SERVER_IP,edit,1350631552
Control18=IDC_STATIC,static,1342308864
Control19=IDC_COMBO_SERVER_PORT,combobox,1344339971
Control20=IDC_CHECK_SEND_PACKET_SIZE,button,1342242819
Control21=IDC_COMBO_SEND_PACKET_SIZE,combobox,1344339970
Control22=IDC_STATIC,static,1342308864
Control23=IDC_CHECK_CONNECT_TIMEOUT,button,1342242819
Control24=IDC_EDIT_CONNECT_TIMEOUT,edit,1350631554
Control25=IDC_STATIC,static,1342308864
Control26=IDC_STATIC,button,1342177287
Control27=IDC_STATIC,static,1342308352
Control28=IDC_STATIC,static,1342308352
Control29=IDC_STATIC,static,1342308352

[DLG:IDD_TR_BAR]
Type=1
Class=CDlgTRBar
ControlCount=4
Control1=IDC_TREE_TR,SysTreeView32,1350631431
Control2=IDC_STATIC,static,1342308352
Control3=IDC_COMBO_TR,combobox,1344340226
Control4=IDC_BUTTON_SEARCH,button,1342242816

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[MNU:IDR_MAINFRAME]
Type=1
Class=?
Command1=ID_FILE_NEW
Command2=ID_APP_EXIT
Command3=ID_APP_ABOUT
CommandCount=3

[MNU:IDR_XINGAPTYPE]
Type=1
Class=?
Command1=ID_FILE_NEW
Command2=ID_FILE_CLOSE
Command3=ID_APP_EXIT
Command4=ID_EDIT_UNDO
Command5=ID_EDIT_CUT
Command6=ID_EDIT_COPY
Command7=ID_EDIT_PASTE
Command8=ID_WINDOW_CASCADE
Command9=ID_WINDOW_TILE_HORZ
Command10=ID_WINDOW_ARRANGE
Command11=ID_APP_ABOUT
CommandCount=11

[DLG:IDD_t1866]
Type=1
Class=CDlgBase
ControlCount=12
Control1=IDC_STATIC,static,1342308864
Control2=IDC_STATIC,static,1342308864
Control3=IDC_INBLOCK_ID,edit,1350631552
Control4=IDC_STATIC,static,1342308864
Control5=IDC_INBLOCK_CONT,edit,1350631552
Control6=IDC_STATIC,static,1342308864
Control7=IDC_INBLOCK_INDEX1866,edit,1350631552
Control8=IDC_BUTTON_REQUEST,button,1342242816
Control9=IDC_BUTTON_REQUEST1,button,1342242816
Control10=IDC_STATIC,static,1342308864
Control11=IDC_OUTBLOCK1,SysListView32,1350631425
Control12=IDC_OUTBLOCK,SysListView32,1350631425

