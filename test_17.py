from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tabbed_widget import *
import sys

class anaPencere(QMainWindow):
    def __init__(self):
        super (anaPencere,self).__init__()
        #self.setStyleSheet("background-color: ; margin:5px; border:1px solid rgb(0, 255, 0); ")
        self.initUI()

    def initUI(self):

        self.setGeometry(100,100,800,600)
        self.setWindowTitle("İşletme Cari Hesap Otomasyonu")
        self.statusBar()

        #textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

        main_frame = QFrame(self)
        main_frame.setFrameStyle(QFrame.Box)
        main_frame.setLineWidth(2)
        self.setCentralWidget(main_frame)

        main_frame.resize(800,200)
        self.create_menuBar()
        self.create_toolBar()

        #frame.setGeometry(5,100,795,200)
        #frame.setStyleSheet("background-color: gray;")
        #border: 5px solid black
        #frame.setFrameShape(QFrame.StyledPanel)
        main_frame.setFrameShadow(QFrame.Sunken)
        #frame.setFrameShape(QFrame.HLine)
        tabbed_win = tab_widget(self)
        self.setCentralWidget(tabbed_win)

        self.create_horizantalGroupBox()
        self.create_gridGroupBox()
        self.create_formGroupBox()

    def create_menuBar(self):
        new_action = QAction(QIcon('/home/hsa/PycharmProjects/writer/icons/new.png'),'&New',self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Yeni ')
        new_action.triggered.connect(self.new_func)

        open_action = QAction(QIcon('/home/hsa/PycharmProjects/writer/icons/open2.png'),'&Open',self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Dosya Aç ')
        open_action.triggered.connect(self.open_func)

        delete_action = QAction(QIcon('/home/hsa/PycharmProjects/writer/icons/cut.png'),'&Delete',self)
        delete_action.setShortcut('Ctrl+D')
        delete_action.setStatusTip('Sil')
        delete_action.triggered.connect(self.delete_func)

        exit_action = QAction(QIcon('/home/hsa/PycharmProjects/writer/icons/close.png'),'&Exit',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Çıkış ')
        exit_action.triggered.connect(QApplication.quit)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&Dosya')
        filemenu.addAction(new_action)
        filemenu.addAction(open_action)
        filemenu.addAction(delete_action)
        filemenu.addAction(exit_action)

        editMenu =  menubar.addMenu('&Düzelt')
        viewMenu =  menubar.addMenu('&Göster')
        searchMenu =menubar.addMenu('&Ara')
        toolsMenu = menubar.addMenu('&Araçlar')
        helpMenu =  menubar.addMenu('&Yardım')

        help_action = QAction(QIcon('/home/hsa/PycharmProjects/writer/icons/preview.png'),'&Yardım',self)
        help_action.setShortcut('Ctrl+H')
        help_action.setStatusTip('Yardım')
        help_action.triggered.connect(self.help_func)

        helpMenu.addAction(help_action)


    def help_func(self):
        dialog_win = QDialog(self)
        dialog_win.setModal(False)
        dialog_win.setWindowOpacity(0.88)
        #self.dialog_win.setSizeGripEnabled()

        text_edit = QTextEdit()
        text=open('/home/hsa/Documents/Help_test.html').read()
        text_edit.setHtml(text)
        dialog_win.setWindowTitle("Yardım Penceresi")

        layout = QGridLayout(dialog_win)

        layout.addWidget(text_edit)

        dialog_win.show()

    def new_func(self):
        pass

    def open_func(self):
        pass

    def delete_func(self):
        pass

    def create_toolBar(self):

        account_tlb_action = QAction(QIcon("/home/hsa/PycharmProjects/writer/cc/black/png/contact_icon&32.png"),"Cari Hesap İşlemleri Yönetimi",self)
        account_tlb_action.setStatusTip("Cari Hesap Hareketleri giriş/düzeltme/silme işlemleri")
        account_tlb_action.setShortcut("Ctrl+Shift+A")
        account_tlb_action.triggered.connect(self.win_account)

        collection_tlb_action = QAction(QIcon("/home/hsa/PycharmProjects/writer/cc/black/png/checkbox_checked_icon&32.png"),"Kasa Hesabı Yönetimi",self)
        collection_tlb_action.setStatusTip("Kasa Hareketleri giriş/düzeltme/silme işlemleri")
        collection_tlb_action.setShortcut("Ctrl+Shift+C")
        collection_tlb_action.triggered.connect(self.win_collection)

        stock_tlb_action = QAction(QIcon("/home/hsa/PycharmProjects/writer/cc/black/png/layers_1_icon&32.png"),"Stok Envanter Yönetimi",self)
        stock_tlb_action.setStatusTip("Stok Envanter Hareketleri giriş/düzeltme/silme işlemleri")
        stock_tlb_action.setShortcut("Ctrl+Shift+I")
        stock_tlb_action.triggered.connect(self.win_stock)

        employee_tlb_action = QAction(QIcon("/home/hsa/PycharmProjects/writer/cc/black/png/emotion_smile_icon&32.png"),"Çalışan İşlemleri Yönetimi",self)
        employee_tlb_action.setStatusTip("Çalışan Hareketleri giriş/düzeltme/silme işlemleri")
        employee_tlb_action.setShortcut("Ctrl+Shift+C")
        employee_tlb_action.triggered.connect(self.win_employee)

        reporting_tlb_action = QAction(QIcon("/home/hsa/PycharmProjects/writer/cc/black/png/db_icon&32.png"),"Raporlama Yönetimi",self)
        reporting_tlb_action.setStatusTip("Rapor geliştirme/düzenleme/yazıcı çıktısı")
        reporting_tlb_action.setShortcut("Ctrl+Shift+R")
        reporting_tlb_action.triggered.connect(self.win_reporting)

        tool_bar = self.addToolBar("Araçlar")

        tool_bar.addAction(account_tlb_action)
        tool_bar.addAction(collection_tlb_action)
        tool_bar.addAction(stock_tlb_action)
        tool_bar.addAction(employee_tlb_action)
        tool_bar.addSeparator()
        tool_bar.addAction(reporting_tlb_action)

        self.addToolBarBreak()

    def win_account(self):
        pass

    def win_collection(self):
        pass

    def win_stock(self):
        pass

    def win_employee(self):
        pass

    def win_reporting(self):
        pass

    def create_horizantalGroupBox(self):
        pass

    def create_gridGroupBox(self):
        pass

    def create_formGroupBox(self):
        pass

def main():
    app = QApplication(sys.argv)
    run_app = anaPencere()
    run_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



