import sys
from PyQt5 import QtWidgets
from ders139_tablewidget import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem


class uygulama(QtWidgets.QMainWindow):

    def __init__(self):

        super(uygulama, self).__init__()

        self.arayüz = Ui_MainWindow()

        self.arayüz.setupUi(self)

        self.urunyukle()

        self.arayüz.pushButton.clicked.connect(self.ekle)

        self.arayüz.tableWidget.doubleClicked.connect(self.tikla) 
        # tablewidget a 2 kere tıklandığında ne olsun onu söyledik


    def urunyukle(self):

        ürünler  = [
            {"model": "iphone 11", "fiyat":10000},
            {"model": "iphone 12", "fiyat":20000},
            {"model": "iphone 13", "fiyat":30000},
        ]

        self.arayüz.tableWidget.setRowCount(len(ürünler)) # ürün sayısı kadar satır olması lazım bilmediğinde böyle yap
        self.arayüz.tableWidget.setColumnCount(2)
        self.arayüz.tableWidget.setHorizontalHeaderLabels( ("model","fiyat") ) # sütun başlıklarını ekledik
        self.arayüz.tableWidget.setColumnWidth(0,200) # 0.sütunun genişliğini ayarladık
        self.arayüz.tableWidget.setColumnWidth(1,100) # 1.sütunun genişliğini ayarladık

        satirindex = 0
        for ür in ürünler:
            self.arayüz.tableWidget.setItem(satirindex,0, QTableWidgetItem(ür["model"])) # dönerek ekledik model
            self.arayüz.tableWidget.setItem(satirindex,1, QTableWidgetItem(str(ür["fiyat"]))) #ve fiyatı
            satirindex+=1


        self.arayüz.tableWidget.setRowCount(3)    # kaç tane satır olsun
        self.arayüz.tableWidget.setColumnCount(2) # kaç tane sütun olsun
        self.arayüz.tableWidget.setHorizontalHeaderLabels( ("model","fiyat") ) # sütun başlıklarını ekledik
        self.arayüz.tableWidget.setColumnWidth(0,200)
        self.arayüz.tableWidget.setColumnWidth(1,100)

        self.arayüz.tableWidget.setItem(0,0, QTableWidgetItem("samsung s5")) # 0.satır 0.sütuna ekledik
        self.arayüz.tableWidget.setItem(0,1, QTableWidgetItem("2000"))       # 0.satır 1.sütuna ekledik
        self.arayüz.tableWidget.setItem(1,0, QTableWidgetItem("samsung s6"))
        self.arayüz.tableWidget.setItem(1,1, QTableWidgetItem("3000"))
        self.arayüz.tableWidget.setItem(2,0, QTableWidgetItem("samsung s7"))
        self.arayüz.tableWidget.setItem(2,1, QTableWidgetItem("4000"))


    def ekle(self):

        ad = self.arayüz.label.text()     # ad ve fiyatı aldık line editten
        fiyat = self.arayüz.label_2.text()

        if ad and fiyat is not None:
            satirsayac = self.arayüz.tableWidget.rowCount() # satir sayısını bize söyler
            print(satirsayac)
            self.arayüz.tableWidget.insertRow(satirsayac)   # o kadar satir ekle dedik 

            self.arayüz.tableWidget.setItem(satirsayac,0, QTableWidgetItem(ad))
            self.arayüz.tableWidget.setItem(satirsayac,1, QTableWidgetItem(fiyat))

    def tikla(self):

        for item in self.arayüz.tableWidget.selectedItems(): # bir nesnedir onun üzerinde dolaşıp

            print(item.row(), item.column(), item.text())    # satır sütun ve text bilgilerini aldık


        

def goster():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())

goster()