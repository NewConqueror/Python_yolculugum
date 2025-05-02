import sys
from PyQt5 import QtWidgets
from ders133_checkboxForm import Ui_MainWindow

class uygulama(QtWidgets.QMainWindow):

    def __init__(self):

        super(uygulama, self).__init__()

        self.arayüz = Ui_MainWindow()

        self.arayüz.setupUi(self)

        self.arayüz.checkBox.stateChanged.connect(self.goster)   # checkbox seçildiği zaman ne yapsın onu söyledik
        self.arayüz.checkBox_2.stateChanged.connect(self.goster) # goster fonksiyonuna git dedik
        self.arayüz.checkBox_3.stateChanged.connect(self.goster)

        self.arayüz.pushButton.clicked.connect(self.secildimihobi)   # 1.butona tıklandığı zaman ne olsun onu dedik
        self.arayüz.pushButton_2.clicked.connect(self.secildimiders) # 2.butona tıklandığı zaman ne olsun onu dedik

    def goster(self, deger):
        
        cb = self.sender()    # hangi butona tıklandığını anlıyoruz klasik

        print(deger)          # eğer checkbox seçiliyse 2 değerini alıyoruz seçili değilse 0 değerini
        print(cb.text())      # checkbox üzerinde yazanı söyler sinema matematik vs vs
        print(cb.isChecked()) # seçiliyse True seçili değilse False döndürür

    def secildimihobi(self):
        sonuc =""
        items = self.arayüz.groupBox.findChildren(QtWidgets.QCheckBox) # obje döndürür liste şeklinde

        for cb in items:
            
            if cb.isChecked():
                sonuc+= cb.text() + "\n"
            
            self.arayüz.label.setText(sonuc)

    def secildimiders(self):
        sonuc =""
        items = self.arayüz.groupBox_2.findChildren(QtWidgets.QCheckBox) # groupbox altındakileri yani cocukları buluyoruz

        for cb in items: # liste döndüğü için for kullanıyoruz üzerinde gezinmek için
            
            if cb.isChecked():
                sonuc+= cb.text() + "\n"
            
            self.arayüz.label_2.setText(sonuc)





    


def calistir():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())


calistir()
    