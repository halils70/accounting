import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import test_17

class tab_widget(QTabWidget):
    def __init__(self, parent=None):
        super(tab_widget, self).__init__(parent)
        self.setGeometry(100,100,600,300)
        self.setStyleSheet("QTabBar{font: bold;}")
        self.setMovable(True)
        self.setTabsClosable(True)
        self.setTabShape(1)

        self.Tab1 = QTabWidget()

        self.Tab2 = QTabWidget()

        self.Tab3 = QTabWidget()
        self.Tab4 = QTabWidget()
        self.Tab5 = QTabWidget()

        self.addTab(self.Tab1,"Tab1")
        self.addTab(self.Tab2,"Tab2")
        self.addTab(self.Tab3,"Tab3")
        self.addTab(self.Tab4,"Tab4")
        self.addTab(self.Tab5,"Tab5")

        self.Tab_1_UI()
        self.Tab_2_UI()
        self.Tab_3_UI()
        self.Tab_4_UI()
        self.Tab_5_UI()


    def Tab_1_UI(self):
        layout = QFormLayout()
        label_picture = QLabel()
        label_picture.setScaledContents(True)
        picture_view = QPixmap("/home/hsa/PycharmProjects/writer/ozet_ana_ekran.png")
         #   .scaled(size,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        label_picture.setPixmap(picture_view)
        layout.addRow(label_picture)

        self.setTabText(0, "&İşletme Hesap Özet Göstergeleri")
        self.Tab1.setLayout(layout)


    def Tab_2_UI(self):

        cari_hes_no_label       = QLabel("Cari Hesap No")
        cari_hes_firma_label    = QLabel("Firma Adı")
        cari_hes_yetkili_label  = QLabel("Yetkili")
        cari_ver_daire_label    = QLabel("Vergi Dairesi")
        cari_ver_no_label       = QLabel("Vergi No")

        cari_hes_no = QLineEdit()
        cari_hes_no.setInputMask("NNN-NNNN")

        cari_hes_firma = QLineEdit()
        cari_hes_firma.setInputMask("NNNNNNNNNNNNNNNNNNNN")

        cari_hes_yetkili = QLineEdit()
        cari_hes_yetkili.setInputMask("NNNNNNNNNNNNNNNNNNNN")
        cari_hes_yetkili.setMaxLength(20)
        cari_hes_yetkili.setAlignment(Qt.AlignLeft)
        cari_hes_yetkili.home(True)
        cari_hes_yetkili.setCursorPosition(0)
        cari_hes_yetkili.setFrame(True)

        cari_ver_daire = QLineEdit()
        cari_ver_daire.setInputMask("NNNNNNNNNNNNNNNNNNNN")
        cari_ver_daire.setMaxLength(20)
        cari_ver_daire.setAlignment(Qt.AlignLeft)
        cari_ver_daire.home(True)
        cari_ver_daire.setCursorPosition(0)
        cari_ver_daire.setFrame(True)

        cari_ver_no = QLineEdit()
        cari_ver_no.setInputMask("9999999999")
        cari_ver_no.setMaxLength(20)
        cari_ver_no.setAlignment(Qt.AlignLeft)
        cari_ver_no.home(True)
        cari_ver_no.setCursorPosition(0)
        cari_ver_no.setFrame(True)

        self.frame_main_tab2 = QFrame(self.Tab2)
        self.frame_main_tab2.setGeometry(5,100,795,200)


        cari_hes_kategori = QGroupBox()
        cari_hes_kategori.setTitle("Müşteri Kategori")
        cari_hes_kategori.setFlat(True)
        cari_hes_kategori1 = QRadioButton(cari_hes_kategori)
        cari_hes_kategori1.setText("Müşteri")

        cari_hes_kategori2 = QRadioButton(cari_hes_kategori)
        cari_hes_kategori2.setText("Tedarikci")
        cari_hes_kategori1.setChecked(True)
        hbox = QGridLayout()
        hbox.addWidget(cari_hes_kategori1,0,0)
        hbox.addWidget(cari_hes_kategori2,0,1)
        cari_hes_kategori.setLayout(hbox)

        layout=QFormLayout()
        layout.addRow(cari_hes_kategori)
        layout.addRow(cari_hes_no_label,cari_hes_no)
        layout.addRow(cari_hes_firma_label,cari_hes_firma)
        layout.addRow(cari_hes_yetkili_label,cari_hes_yetkili)
        layout.addRow(cari_ver_daire_label,cari_ver_daire)
        layout.addRow(cari_ver_no_label,cari_ver_no)
        self.setLayout(layout)

        tabtext1 = "&Cari Hesap Kartları"
        self.setTabText(1,tabtext1)
        self.Tab2.setLayout(layout)

    def Tab_3_UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))

        self.setTabText(2,"&Kasa Banka Kartları")
        self.Tab3.setLayout(layout)

    def Tab_4_UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.setTabText(3,"&Stok Envanter Kartları")
        self.Tab4.setLayout(layout)

    def Tab_5_UI(self):
        layout = QFormLayout()
        self.btn=QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)
        self.le=QLineEdit()
        layout.addRow(self.btn,self.le)

        self.btn1=QPushButton("get name")
        self.btn1.clicked.connect(self.gettext)
        self.le1=QLineEdit()
        layout.addRow(self.btn1,self.le1)

        self.btn2=QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)
        self.le2=QLineEdit()
        layout.addRow(self.btn2,self.le2)

        self.setTabText(4, "&Çalışan Hesap Hareketleri")
        self.Tab5.setLayout(layout)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages",
                                        items, 0, False)
        if ok and item:
            self.le.setText(item)
    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
        if ok:
            self.le1.setText(str(text))

    def getint(self):
        num,ok=QInputDialog.getInt(self,"integer input dualog","enter a number")
        if ok:
            self.le2.setText(str(num))
def main():
    app = QApplication(sys.argv)
    ex = tab_widget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
