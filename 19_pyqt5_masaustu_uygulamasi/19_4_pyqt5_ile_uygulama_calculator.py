import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class AnaForm(QMainWindow):

    def __init__(self):
        super(AnaForm, self).__init__()

        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(300,200,500,500)

        self.arayüz()

    def arayüz(self):
        
        self.lblsayi1 = QtWidgets.QLabel(self)
        self.lblsayi1.setText("sayi1: ")
        self.lblsayi1.move(50,30)

        self.txtsayi1 = QtWidgets.QLineEdit(self)
        self.txtsayi1.move(100,30)
        self.txtsayi1.resize(200,32)

        self.lblsayi2 = QtWidgets.QLabel(self)
        self.lblsayi2.setText("sayi2: ")
        self.lblsayi2.move(50,80)

        self.txtsayi2 = QtWidgets.QLineEdit(self)
        self.txtsayi2.move(150,80)
        self.txtsayi2.resize(200,32)

        self.butontopla = QtWidgets.QPushButton(self)
        self.butontopla.setText("Topla")
        self.butontopla.move(150,130)
        self.butontopla.clicked.connect(self.hesapla)

        self.butoncikar = QtWidgets.QPushButton(self)
        self.butoncikar.setText("Cikar")
        self.butoncikar.move(150,170)
        self.butoncikar.clicked.connect(self.hesapla)

        self.butoncarp = QtWidgets.QPushButton(self)
        self.butoncarp.setText("Carp")
        self.butoncarp.move(150,210)
        self.butoncarp.clicked.connect(self.hesapla)

        self.butonbol = QtWidgets.QPushButton(self)
        self.butonbol.setText("Bol")
        self.butonbol.move(150,250)
        self.butonbol.clicked.connect(self.hesapla)

        self.lblsonuc = QtWidgets.QLabel(self)
        self.lblsonuc.setText("sonuc: ")
        self.lblsonuc.move(150,290)

    def hesapla(self):

        sender = self.sender().text()
        sonuc = 0

        if sender == 'Topla':
            sonuc = int(self.txtsayi1.text()) + int(self.txtsayi2.text())
        elif sender == 'Cikar':
            sonuc = int(self.txtsayi1.text()) - int(self.txtsayi2.text())
        elif sender == 'Carp':
            sonuc = int(self.txtsayi1.text()) * int(self.txtsayi2.text())
        elif sender == 'Bol':
            sonuc = int(self.txtsayi1.text()) / int(self.txtsayi2.text())

        self.lblsonuc.setText("sonuc: " + str(sonuc))
        
        



def uygulama():

    app = QApplication(sys.argv)
    pencere = AnaForm()
    pencere.show()

    sys.exit(app.exec_())

uygulama()