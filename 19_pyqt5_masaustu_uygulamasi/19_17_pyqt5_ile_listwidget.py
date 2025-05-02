import sys
from PyQt5 import QtWidgets
from ders138_listwidget import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox


class uygulama(QtWidgets.QMainWindow):

    def __init__(self):

        super(uygulama, self).__init__()

        self.arayüz = Ui_MainWindow()

        self.arayüz.setupUi(self)

        self.ogrenciyukle()

        self.arayüz.pushButton.clicked.connect(self.ogrenciekle)

        self.arayüz.pushButton_2.clicked.connect(self.ogrenciguncelle)

        self.arayüz.pushButton_3.clicked.connect(self.ogrencisil)

        self.arayüz.pushButton_4.clicked.connect(self.yukari)

        self.arayüz.pushButton_5.clicked.connect(self.asagi)

        self.arayüz.pushButton_6.clicked.connect(self.sirala)

        self.arayüz.pushButton_7.clicked.connect(self.cikis)



    def ogrenciyukle(self):

        ogrenciler = ["ahmet","mehmet","ali"] 

        self.arayüz.listWidget.addItems(ogrenciler) # böyle de yapabiliriz ..addItems( ["fatih","saliha"] ) böyle de
        self.arayüz.listWidget.setCurrentRow(0)     # başlangıç olarak 0.index yani ilk satır seçili gelicek


    def ogrenciekle(self):
        
        index = self.arayüz.listWidget.currentRow() # hangi satırdakini seçersek onun index ini almış oluyor

        text, ok = QInputDialog.getText(self, "yeni ogrenci ekle ", "ogrencinin adi: ")

        if text and ok is not None: # eğer text ve ok boş değilse 

            self.arayüz.listWidget.insertItem(index,text)  # aldığımız index e text i ekle dedik

    def ogrenciguncelle(self):

        index = self.arayüz.listWidget.currentRow()
        print(index)
        eleman = self.arayüz.listWidget.item(index) # bir listwidget nesnesi döner index e göre eleman aldık
        print(eleman)

        if eleman is not None:

            text,ok = QInputDialog.getText(self,"öğrenci guncelle","öğrenci adi: ", QLineEdit.Normal, eleman.text())

            if text and ok is not None:
                
                eleman.setText(text)


    def ogrencisil(self):

        index = self.arayüz.listWidget.currentRow()

        eleman = self.arayüz.listWidget.item(index)  # index e göre elemanı seçtik

        if eleman is None: # eleman Boşsa değer yoksa
            return
        
        soru = QMessageBox.question(self,"öğrenci sil","silmek istediğinizden emin misiniz? "+eleman.text(),QMessageBox.Yes | QMessageBox.No)
        
        if soru == QMessageBox.Yes:

            item = self.arayüz.listWidget.takeItem(index)

            del item 

    
    def yukari(self):

        index = self.arayüz.listWidget.currentRow()

        if index > 1:

            eleman = self.arayüz.listWidget.takeItem(index)

            self.arayüz.listWidget.insertItem(index-1, eleman) # bir üstteki index e ekledik
            
            self.arayüz.listWidget.setCurrentItem(eleman)
            # ilk seçtiğimiz elemanda hala geçerli kalsın tekrar onu seçmekle uğraşmayalım dedik

    def asagi(self):

        index = self.arayüz.listWidget.currentRow()

        eleman = self.arayüz.listWidget.takeItem(index)

        if index < self.arayüz.listWidget.count() -1: # sayinin 1 eksiği son işte eğer sonsa daha aşağı gidemez

            self.arayüz.listWidget.takeItem(eleman)

            self.arayüz.listWidget.insertItem(index+1,eleman) # bir alttaki index e ekledik

            self.arayüz.listWidget.setCurrentItem(eleman) # yine ilk seçtiğimiz geçerli kalsın dedik


    def sirala(self):
        self.arayüz.listWidget.sortItems() # direkt sıralama metodu varmış uğraşmadık


    def cikis(self):
        quit() # bu da normal çıkış işte


def goster():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())

goster()