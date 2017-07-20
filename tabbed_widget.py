import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
        #cari_hes_no.setMaxLength(8)
        #cari_hes_no.setAlignment(Qt.AlignLeft)
        #cari_hes_no.home(True)
        #cari_hes_no.setCursorPosition(0)
        #cari_hes_no.setFrame(True)

        cari_hes_firma = QLineEdit()
        cari_hes_firma.setInputMask("NNNNNNNNNNNNNNNNNNNN")
        #cari_hes_firma.setMaxLength(20)
        #cari_hes_firma.setAlignment(Qt.AlignLeft)
        #cari_hes_firma.home(True)
        #cari_hes_firma.setCursorPosition(0)
        #cari_hes_firma.setFrame(True)

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


        layout=QGridLayout()
        #layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        cari_hes_kategori = QGroupBox("Müşteri Kategori")
        cari_hes_kategori1 = QRadioButton("Müşteri")
        cari_hes_kategori2 = QRadioButton("Tedarikci")
        cari_hes_kategori1.setChecked(True)
        hbox = QHBoxLayout()
        hbox.addWidget(cari_hes_kategori1)
        hbox.addWidget(cari_hes_kategori2)
        #hbox.addStretch(1)
        cari_hes_kategori.setLayout(hbox)

        layout.addWidget(cari_hes_kategori,0,0,1,1)

        #layout.addWidget(cari_hes_kategori1,0,0)
        #layout.addWidget(cari_hes_kategori2,0,1)
        layout.addWidget(cari_hes_no_label,1,0)
        layout.addWidget(cari_hes_no,1,1)
        layout.addWidget(cari_hes_firma_label,2,0)
        layout.addWidget(cari_hes_firma,2,1)
        layout.addWidget(cari_hes_yetkili_label,3,0)
        layout.addWidget(cari_hes_yetkili,3,1)
        layout.addWidget(cari_ver_daire_label,4,0)
        layout.addWidget(cari_ver_daire,4,1)
        layout.addWidget(cari_ver_no_label,5,0)
        layout.addWidget(cari_ver_no,5,1)
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
