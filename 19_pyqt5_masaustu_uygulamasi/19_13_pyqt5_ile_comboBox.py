import sys
from PyQt5 import QtWidgets
from ders135_comboBoxForm import Ui_MainWindow

class Form(QtWidgets.QMainWindow):

    def __init__(self):

        super(Form, self).__init__()

        self.arayüz = Ui_MainWindow()
        self.arayüz.setupUi(self)

        combo = self.arayüz.comboBox #bu şekilde takma ad oluşturabilirz bir daha self.arayüz.comboBox yazmaya gerek yok

        # combo.addItem("ankara")    # takma adı kullanarak yaptık
        # combo.addItem("istanbul")
        #combo.addItems(["izmir","kocaeli","rize"])  # birden fazla da ekleyebiliriz liste şeklinde

        self.arayüz.pushButton_2.clicked.connect(self.yukle)
        self.arayüz.pushButton.clicked.connect(self.getir)
        self.arayüz.pushButton_3.clicked.connect(self.sil)

        self.arayüz.comboBox.currentIndexChanged.connect(self.secilenindex)
        # index değiştiğinde ne yapsın onu söyledik
        self.arayüz.comboBox.currentIndexChanged[str].connect(self.secilentext)
        # index değişicek ama biz string alıcaz
        


    def sil(self):
        self.arayüz.comboBox.clear()  # sildik işte klasik clear metodu


    def yukle(self):

        sehirler = ["izmir","kocaeli","rize"]

        self.arayüz.comboBox.addItems(sehirler)


    def getir(self):

        print(self.arayüz.comboBox.currentText())  # gecerli text i getirir
        print(self.arayüz.comboBox.currentIndex()) # gecerli index i getirir
       
        sayac = self.arayüz.comboBox.count()       # kaç eleman var onu söyler

        for index in range(sayac):
            print(self.arayüz.comboBox.itemText(index)) # index e göre bize text i söyler

    def secilenindex(self, index):
        print(index)

    def secilentext(self, text):
        print(text)





def goster():

    uygulama = QtWidgets.QApplication(sys.argv)

    win = Form()

    win.show()

    sys.exit(uygulama.exec_())


goster()

