# ders131_AnaForm un içinde değişiklik yapma zaten qt designer da değişiklik yaptığında ve pyuic5 i
# çalıştırdığında ordaki kodlar silinecek

import sys
from PyQt5 import QtWidgets
from ders131_AnaForm import Ui_MainWindow

class uygulama(QtWidgets.QMainWindow):

    def __init__(self):
        super(uygulama, self).__init__()
        
        self.arayüz = Ui_MainWindow()  # formdaki label a textbox a artık arayüz üzerinden ulaşıcan mainwindow aynı şey işte
        
        self.arayüz.setupUi(self)  #setupUi yı çağırıcaz ki formu bize getirsin

        self.arayüz.pushButton.clicked.connect(self.hesapla) # aşağı doğru toplama cikarma carpma bolme
        self.arayüz.pushButton_2.clicked.connect(self.hesapla)
        self.arayüz.pushButton_3.clicked.connect(self.hesapla)
        self.arayüz.pushButton_4.clicked.connect(self.hesapla)

    
    def hesapla(self):
        
        sender = self.sender().text()
        sonuc = 0

        if sender == 'Topla':
            sonuc = int(self.arayüz.lineEdit.text()) + int(self.arayüz.lineEdit_2.text())
        elif sender == 'Cikar':
            sonuc = int(self.arayüz.lineEdit.text()) - int(self.arayüz.lineEdit_2.text())
        elif sender == 'Carp':
            sonuc = int(self.arayüz.lineEdit.text()) * int(self.arayüz.lineEdit_2.text())
        elif sender == 'Bol':
            sonuc = int(self.arayüz.lineEdit.text()) / int(self.arayüz.lineEdit_2.text())

        self.arayüz.label_3.setText(str(sonuc))

        


def uygcalistir():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())


uygcalistir()