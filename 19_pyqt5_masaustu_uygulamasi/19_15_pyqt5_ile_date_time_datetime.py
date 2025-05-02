import sys
from PyQt5 import QtWidgets
from ders137_date_time_datetime import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class uygulama(QtWidgets.QMainWindow):

    def __init__(self):

        super(uygulama, self).__init__()

        self.arayüz = Ui_MainWindow()
        self.arayüz.setupUi(self)

        self.arayüz.pushButton.clicked.connect(self.hesapla)

    
    def hesapla(self):

        baslangic = self.arayüz.dateEdit.date()
        bitis = self.arayüz.dateEdit_2.date()

        print(baslangic, bitis)

        print("aydaki  günler: {0}".format(baslangic.daysInMonth()))
        print("yıldaki günler: {0}".format(baslangic.daysInYear()))

        print("toplam gün farkı: {0}".format(baslangic.daysTo(bitis)))


        simdi = QDate.currentDate()

        print("bugünden toplam gün farkı: {0}".format(baslangic.daysTo(simdi)))

def goster():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())


goster()